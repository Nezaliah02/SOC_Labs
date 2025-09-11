# Jour 3 – Détection & Corrélation (Mercredi)

## 🎯 Objectifs
- Activer et vérifier la collecte **Sysmon** dans Splunk.
- Importer et tester le **dashboard Sysmon Quickview**.
- Créer des recherches de **détection et corrélation** sur les événements Windows et Sysmon.

---

## ✅ Étapes réalisées

### 1. Ajout de Sysmon dans Splunk
Modification du fichier `inputs.conf` :
```ini
[WinEventLog://Microsoft-Windows-Sysmon/Operational]
disabled = 0
index = main
```
Puis redémarrage du service Splunkd :
```cmd
net stop Splunkd
net start Splunkd
```

### 2. Vérification de l’ingestion Sysmon
Recherche Splunk :
```spl
index=main sourcetype="WinEventLog:Microsoft-Windows-Sysmon/Operational"
| stats count by EventCode
```
→ Résultats observés : EventCode 1 (Process Create), 3 (Network Connection), 11 (File Create), 22 (DNS Query).

### 3. Import du Dashboard Sysmon Quickview
- Fichier : `sysmon_quickview.xml`
- Fonctionnalités :
  - Processus créés (EventID=1)
  - Connexions réseau (EventID=3)
  - Requêtes DNS (EventID=22)
  - Fichiers créés (EventID=11)
- Dashboard accessible via **Search & Reporting → Dashboards**.

### 4. Création de recherches de détection
- **Brute force (4625 répétés)**  
```spl
index=main sourcetype="WinEventLog:Security" EventCode=4625
| stats count by Account_Name, host
| where count > 5
```

- **Succès après plusieurs échecs (4625 → 4624)**  
```spl
index=main sourcetype="WinEventLog:Security" (EventCode=4625 OR EventCode=4624)
| transaction Account_Name maxspan=5m
| search EventCode=4625 EventCode=4624
```

- **Process suspects (PowerShell, Mimikatz)**  
```spl
index=main (EventCode=4688 OR (sourcetype="WinEventLog:Microsoft-Windows-Sysmon/Operational" EventCode=1))
| search New_Process_Name="*powershell.exe" OR Image="*mimikatz.exe"
```

- **Parent → Child suspects (Word → PowerShell)**  
```spl
index=main sourcetype="WinEventLog:Microsoft-Windows-Sysmon/Operational" EventCode=1
| where like(ParentImage,"%winword.exe%") AND like(Image,"%powershell.exe%")
```

- **DNS suspects (TLD exotiques)**  
```spl
index=main sourcetype="WinEventLog:Microsoft-Windows-Sysmon/Operational" EventCode=22
| regex QueryName="(\.ru$|\.cn$|\.xyz$)"
```

---

## 📂 Contenu du dossier
- `sysmon_quickview.xml` → dashboard Sysmon  
- `detections.md` → requêtes de détection Splunk  
- `/screens/` :
  - `sysmon_ingestion.png` → preuve ingestion Sysmon  
  - `quickview_dashboard.png` → dashboard Sysmon Quickview  
  - `brute_force_search.png` → recherche brute force (4625)  
  - `process_suspects.png` → recherche process suspects  

---

## ✅ Validation Jour 3
Les objectifs de **détection & corrélation** sont atteints :
- Ingestion Sysmon opérationnelle dans Splunk.  
- Dashboard Sysmon Quickview fonctionnel.  
- Détections de base créées et testées (brute force, process suspects, DNS exotiques, etc.).  
