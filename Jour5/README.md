# Jour 5 – Analyse & Clôture Semaine 1 (Vendredi)

## 🎯 Objectifs
- Approfondir l’analyse des événements Sysmon (EventID 1 – Process Create).
- Créer un dashboard dédié au monitoring des processus.
- Rédiger une note d’analyse sur les comportements observés.
- Réaliser l’After Action Review de la semaine.
- Planifier la semaine 2 (ingestion Linux, attaques Kali).

---

## ✅ Étapes réalisées

### 1. Recherches avancées EventID 1
- Liste brute des processus créés.
- Top 15 des processus exécutés.
- Détection de processus suspects (PowerShell, cmd, mimikatz).
- Process rares (anomalies potentielles).
- Exemples analysés manuellement :
  - `cmd.exe` lancé par Splunk Python → **normal**.
  - `ping.exe` lancé par PowerShell → **à surveiller**.

### 2. Dashboard Process Monitoring
- Créé un nouveau dashboard `process_monitoring.xml`.
- Panels :
  - Derniers processus créés.
  - Top 15 processus.
  - Process suspects connus.
  - Process rares.
- Capture ajoutée dans `/screens/`.

### 3. Note d’analyse
- Fichier : `analysis.md`
- Contient l’étude de cas (logs normaux vs suspects).

### 4. After Action Review
- Fichier : `review.md`
- Forces : Splunk + Sysmon opérationnels, détections basiques en place.
- Faiblesses : logs Linux absents, pas d’attaques simulées.
- Améliorations : ingestion Ubuntu/Kali, corrélations multi-sources.

### 5. Planification Semaine 2
- Fichier : `plan_next_week.md`
- Prévoit l’ingestion des logs Linux, brute force SSH depuis Kali, corrélations et hunting.

---

## 📂 Contenu du dossier
- `analysis.md` → Note d’analyse (EventID 1).
- `review.md` → After Action Review (semaine 1).
- `plan_next_week.md` → Plan de la semaine 2.
- `process_monitoring.xml` → Dashboard Splunk (process).
- `/screens/` :
  - Captures des requêtes Splunk EventID 1.
  - Capture du dashboard Process Monitoring.

---

## ✅ Validation Jour 5
La semaine 1 est bouclée avec succès :
- Splunk opérationnel.
- Sysmon collecté et analysé.
- Dashboards et alertes fonctionnels.
- Première analyse SOC L1 rédigée.
- Semaine 2 planifiée (extension vers Linux + Kali).
