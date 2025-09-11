# Détections Jour 3 (Mercredi)

## 1. Brute force (échecs multiples de login - 4625)
```spl
index=main sourcetype="WinEventLog:Security" EventCode=4625
| stats count by Account_Name, host
| where count > 5

index=main sourcetype="WinEventLog:Security" (EventCode=4625 OR EventCode=4624)
| transaction Account_Name maxspan=5m
| search EventCode=4625 EventCode=4624

index=main (EventCode=4688 OR (sourcetype="WinEventLog:Microsoft-Windows-Sysmon/Operational" EventCode=1))
| search New_Process_Name="*powershell.exe" OR Image="*mimikatz.exe"

index=main sourcetype="WinEventLog:Microsoft-Windows-Sysmon/Operational" EventCode=1
| where like(ParentImage,"%winword.exe%") AND like(Image,"%powershell.exe%")

index=main sourcetype="WinEventLog:Microsoft-Windows-Sysmon/Operational" EventCode=22
| regex QueryName="(\.ru$|\.cn$|\.xyz$)"

