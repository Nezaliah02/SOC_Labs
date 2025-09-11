# Jour 4 – Alertes & Dashboard Global (Jeudi)

## 🎯 Objectifs
- Transformer les recherches de détection en **alertes programmées**.
- Créer un **Dashboard SOC – Alertes** pour centraliser la visibilité.

---

## ✅ Étapes réalisées

### 1. Conversion des recherches en alertes
Les recherches créées lors du Jour 3 ont été sauvegardées en **alertes Splunk** (Scheduled Alerts) :
- Alerte brute force (4625 multiples).
- Alerte succès après plusieurs échecs (4625 → 4624).
- Alerte processus suspects (PowerShell / Mimikatz).
- Alerte parent→child suspects (Word → PowerShell).
- Alerte DNS suspects (TLD exotiques).
- Alerte création de compte (4720).

Paramètres :
- **Scheduled** : toutes les 5 minutes.
- **Trigger condition** : résultat > 0.
- **Trigger actions** : *Add to Triggered Alerts*.

---

### 2. Création du Dashboard SOC – Alertes
- Fichier : `soc_alertes.xml`.
- Contenu :
  - **Table** → liste des alertes déclenchées.
  - **Bar chart** → top alertes par type.
  - **Timeline** → volume d’alertes dans le temps.

---

## 📂 Contenu du dossier
- `soc_alertes.xml` → dashboard des alertes.
- `alertes.md` → requêtes Splunk utilisées comme alertes.
- `/screens/`
  - `alert_creation.png` → preuve de création d’une alerte.
  - `alerts_list.png` → liste des alertes dans Splunk.
  - `dashboard_alertes.png` → dashboard SOC-Alertes (même vide).

---

## ✅ Validation Jour 4
Les alertes sont configurées et centralisées dans le dashboard SOC.  
Même si aucune alerte ne s’est encore déclenchée, la configuration est prête à être testée.  
