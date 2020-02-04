#This script will send an email with system information.
emailaddress=maxsayers47@yahoo.com
today=
a=$(ip a |
content="my 
mail -s "IT3038C linux info" $emailaddress <<< $(echo -e $content) 
echo My IP is $a
