#This is a script to send an email with information about our machine.

#A funtion to return the IP address
function getIP {(get-netipaddress).ipv4address | select-string "192*"}


#Set the IP variable
$IP = getIP

#Set the date variable
$date = Get-Date -DisplayHint Date

#Set the name variable
$name = $env:computername

#Set the operating system variable
$os = $env:os

#Set the body variable
$BODY = "This machine's IP is $IP, the date is $date, the name of the machine is $name, and the operating system is $os"

#Build and send the email
Send-MailMessage -To "sayersmx@mail.uc.edu" -From "me@mail.uc.edu" -Subject "IT3038C SysInfo" -Body $BODY -SmtpServer smtp.gmail.com -port 587 -UseSsl -Credential (Get-Credential)

#Confirm the email was sent
Write-Host("Message Sent")