# Alertes Splunk configurées (Jour 4)

## 1. Brute force (échecs multiples de login - 4625)

index=main sourcetype="WinEventLog:Security" EventCode=4625
| stats count by Account_Name, host
| where count > 5

2. Succès après plusieurs échecs (4625 → 4624)

index=main sourcetype="WinEventLog:Security" (EventCode=4625 OR EventCode=4624)
| transaction Account_Name maxspan=5m
| search EventCode=4625 EventCode=4624

3. Process suspects (PowerShell, Mimikatz)

index=main (EventCode=4688 OR (sourcetype="WinEventLog:Microsoft-Windows-Sysmon/Operational" EventCode=1))
| search New_Process_Name="*powershell.exe" OR Image="*mimikatz.exe"

4. Parent → Child suspects (Word → PowerShell)

index=main sourcetype="WinEventLog:Microsoft-Windows-Sysmon/Operational" EventCode=1
| where like(ParentImage,"%winword.exe%") AND like(Image,"%powershell.exe%")

5. DNS suspects (TLD exotiques)

index=main sourcetype="WinEventLog:Microsoft-Windows-Sysmon/Operational" EventCode=22
| regex QueryName="(\.ru$|\.cn$|\.xyz$)"

6. Création de compte (4720)

index=main sourcetype="WinEventLog:Security" EventCode=4720