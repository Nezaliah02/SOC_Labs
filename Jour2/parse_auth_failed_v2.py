import re
import csv

# Fichier d'entrée et de sortie
log_file = "/var/log/auth.log"
output_file = "results_auth_failed_v2.csv"

# Regex pour capturer les IP dans "Failed password"
pattern = re.compile(r"Failed password .* from (\d+\.\d+\.\d+\.\d+)")

# Dictionnaire {IP: tentatives}
ip_counts = {}

with open(log_file, "r") as f:
    for line in f:
        match = pattern.search(line)
        if match:
            ip = match.group(1)
            ip_counts[ip] = ip_counts.get(ip, 0) + 1

# Écriture du CSV
with open(output_file, "w", newline="") as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(["IP", "Tentatives"])
    for ip, count in ip_counts.items():
        writer.writerow([ip, count])

print(f"[+] Résultats sauvegardés dans {output_file}")
