# Jour 5 – After Action Review (Semaine 1)

## ✅ Forces
- Splunk installé et fonctionnel (VM Windows).
- Sysmon configuré et collecté (EventID 1, 3, 11, 22).
- Dashboards en place (Quickview, Process Monitoring, Alertes).
- Détections et alertes basiques créées (brute force, process suspects).

## ❌ Faiblesses
- Couverture limitée à Windows uniquement.
- Pas encore de simulation d’attaques réelles (Kali → Ubuntu).
- Corrélations multi-sources absentes.

## 🚀 Axes d’amélioration
- Ingestion des logs Linux (auth.log).
- Simulation brute force SSH (Kali).
- Détections multi-sources (SSH fails + activité Windows).
- Automatisation (scripts Python, pipeline GitHub).
