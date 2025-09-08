import csv, re
from pathlib import Path

# Chemin du fichier log Linux
src = Path("/var/log/auth.log")

# Liste des résultats
rows = []

# Regex pour trouver les "Failed password"
rx = re.compile(r"Failed password for (invalid user )?(\S+) from (\d+\.\d+\.\d+\.\d+)")

# Lecture du fichier ligne par ligne
for line in src.open(errors="ignore"):
    m = rx.search(line)
    if m:
        user = m.group(2)     # nom d’utilisateur
        ip = m.group(3)       # adresse IP source
        rows.append({"user": user, "ip": ip, "line": line.strip()})

# Export en CSV
out = Path("results_auth_failed.csv")
with out.open("w", newline="", encoding="utf-8") as f:
    w = csv.DictWriter(f, fieldnames=["user","ip","line"])
    w.writeheader()
    w.writerows(rows)

print(f"[+] Écrit: {out} ({len(rows)} lignes)")
