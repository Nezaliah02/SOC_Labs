# Jour 1 – Lundi

## 🎯 Objectifs
- Mettre en place la collecte de logs Windows (Sysmon, Audit Policy, Firewall).
- Collecter et analyser les logs Linux (auth.log → Failed password).
- Simuler des attaques (SSH brute force + Nmap).
- Corréler les résultats Windows / Linux / Réseau.

---

## 🕘 Matin (Windows)

### Étapes
- Installation de **Sysmon** avec configuration minimale.
- Augmentation de la taille des journaux (Sysmon, Security, PowerShell).
- Activation du logging Firewall (`pfirewall.log`).
- Configuration Audit Policy :
  - Ouverture de session (succès + échec).
  - Fermeture de session (succès).
  - Création de processus (succès + échec).
- Vérification :
  - `notepad.exe` et `calc.exe` visibles en **4688 (Security)** et **Sysmon ID 1**.

### Preuves
- `capture_4688.png`
- `capture_sysmon.png`
- `pfirewall_sample.txt`

---

## 🕛 Après-midi (Linux + Réseau)

### Étapes
- Installation et activation d’OpenSSH sur Ubuntu.
- Génération d’échecs SSH (`ssh invaliduser@127.0.0.1`) → logs “Failed password” dans `/var/log/auth.log`.
- Développement du script Python `parse_auth_failed.py` :
  - Extraction des tentatives SSH échouées.
  - Export en CSV : `results_auth_failed.csv`.
- Scan réseau ciblé depuis Ubuntu → Windows :
  - `nmap -sS -p 22,80,135,139,445,3389 <IP_WINDOWS> -Pn`
- Corrélation :
  - **Wireshark** → SYN captés.
  - **pfirewall.log** → connexions ALLOW/DROP depuis IP Ubuntu.
  - **Sysmon** → pas d’Event ID 3 (trafic entrant uniquement).

### Preuves
- `results_auth_failed.csv`
- `parse_auth_failed.py`
- `jour1_nmap_scan.pcapng`
- `pfirewall_after_nmap.txt`
- `NOTE.md` (explication corrélation Nmap)

---

## ✅ Conclusion
- **Windows** : journaux opérationnels (Sysmon + Audit + Firewall).
- **Linux** : parser Python fonctionnel (SSH échoués exportés en CSV).
- **Réseau** : Nmap détecté dans Wireshark + Firewall, mais pas dans Sysmon → normal et documenté.
- **Livrables complets** disponibles dans ce dossier.

Jour 1 terminé 🚀
