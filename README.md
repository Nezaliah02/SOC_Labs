# SOC_Labs

## 🛡️ Présentation
Ce dépôt contient un laboratoire pratique orienté **SOC (Security Operations Center)** et **DevSecOps**.  
L’objectif : monter un environnement complet, simuler des attaques, collecter les logs et développer des scripts d’analyse.  

Chaque journée correspond à un module d’apprentissage avec ses propres livrables (README, scripts, logs, captures).  

---

## 📂 Structure
- **Jour 1** : 
  - Mise en place du lab (VM Windows + Ubuntu + Kali).
  - Installation Sysmon + Audit Policy + Firewall logging.
  - Premier parsing Python (`auth.log` → Failed password SSH).
  - Scan Nmap depuis Ubuntu → Windows, corrélation (Wireshark + Firewall + Sysmon).
- **Jour 2** :
  - Échecs de logon Windows (Event ID 4625).
  - Simulation brute force SSH depuis Kali.
  - Parsing amélioré (compter tentatives par IP).
- **Jour 3** :
  - Corrélation multi-sources (Windows, Linux, Réseau).
  - Enrichissement des scripts Python.
  - Organisation et publication GitHub (version finale pro).
- *(et ainsi de suite…)*

---

## 🎯 Objectifs pédagogiques
- Comprendre la collecte de logs Windows/Linux.  
- Mettre en place une stratégie de détection (Sysmon, Audit Policy, Firewall).  
- Simuler des attaques réseau et système (SSH brute force, Nmap, logon fail).  
- Développer des scripts Python pour automatiser l’analyse et l’export des résultats.  
- Structurer et publier un portfolio technique sur GitHub.

---

## 🚀 Prochaines étapes
- Continuer la documentation jour par jour.
- Ajouter des scripts Python avancés (alerte brute force, parsing Sysmon).
- Mettre en place des corrélations multi-logs (Windows ↔ Linux ↔ Réseau).
- Préparer une présentation finale type “rapport SOC”.

---

## 👨‍💻 Auteur
Projet personnel d’apprentissage et de portfolio SOC/DevSecOps.  
>>>>>>> 2bae4fa (feat: ajout livrables Jour 1 + README global)
