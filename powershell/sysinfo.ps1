Function getIP {(Get-NetIPAddress).IPv4Address | select-string "192*"}
$IP = getIP
Write-Host("This machine's IP is $IP")
Write-Host("This machine's IP is {0}" -f $IP)