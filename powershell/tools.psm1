Function getIP {
    (Get-NetIPAddress).IPv4Address | select-string "192*"
}