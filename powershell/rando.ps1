$RANDO=0
$LogFile = 'c:\logs\rando.log'

for($i=0; $i -lt 5; $i++){
    $RANDO=GET-Random -Maximum 1000 -Minimum 1
    Write-Host($RANDO)
    Add-Content $LogFile "Info: Random number is ${RANDO}"
}