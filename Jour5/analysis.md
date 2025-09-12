# Jour 5 – Analyse des événements (Process Monitoring)

## 🎯 Objectif
Analyser les événements Sysmon (EventID 1) collectés dans Splunk et distinguer comportements normaux vs suspects.

---

## ✅ Exemples observés

### Exemple 1 – Normal
- **Heure** : 09:38:18
- **Image** : cmd.exe
- **CommandLine** : /c ver
- **ParentImage** : python3.9.exe (Splunk module)
- **User** : NT\SYSTEM
- **Verdict** : Normal (activité technique Splunk)

### Exemple 2 – À surveiller
- **Heure** : 09:47:53
- **Image** : ping.exe
- **CommandLine** : 8.8.8.8
- **ParentImage** : powershell.exe
- **User** : Windows 10 Lab
- **Verdict** : À surveiller (PowerShell qui déclenche ping.exe → reconnaissance possible)

---

## 📊 Résumé
- Les dashboards permettent de suivre les process normaux (explorer.exe, svchost.exe, etc.).
- Détection possible des comportements suspects (PowerShell → cmd/ping).
- Limite actuelle : uniquement Windows (pas encore Linux/Kali).
