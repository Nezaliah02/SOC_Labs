# Jour 2 – Mardi

## 🎯 Objectifs
- Observer et analyser des échecs de logon Windows (Event ID 4625).
- Simuler un brute force SSH depuis Kali vers Ubuntu.
- Développer un script Python v2 pour compter les tentatives par IP.
- Exporter les résultats et comparer Windows / Linux.

---

## 🕘 Matin (Windows)

### Étapes réalisées
- Génération volontaire d’échecs de logon (mauvais mot de passe).
- Vérification dans Event Viewer → Event ID **4625** (Failed logon).
- Vérification d’un logon réussi → Event ID **4624** (Successful logon).

### Preuves
- `capture_4625.png` (logon échoué)
- (optionnel) capture 4624 si dispo

---

## 🕛 Après-midi (Linux + Réseau)

### Étapes réalisées
- Activation et configuration de SSH sur Ubuntu (PasswordAuthentication yes, UFW autorisé).
- Lancement d’un brute force depuis Kali avec Hydra :
  ```bash
  hydra -l bootcamp -P rockyou.txt -t 4 192.168.241.130 ssh
