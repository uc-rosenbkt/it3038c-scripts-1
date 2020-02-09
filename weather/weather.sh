#This script is meant to email the current weather conditions in Cincinnati, OH everyday at 7:00 AM.

#Declaring temp veriable to retreive current temperature
temp=$(inxi -xxxW Cincinnati,Ohio | grep 'Temperature')

#Declaring wind variable to retrieve current wind conditions
wind=$(inxi -xxxW Cincinnati,Ohio | grep 'Wind')

#Email address variable to send the message to
emailaddress=sayersmx@mail.uc.edu

#Message variable including the temp and wind variables
message="$temp $wind"

#The email message and subject to be sent
mail -s "Weather Forecast" $emailaddress <<< $(echo -e "Current weather conditions in Cincinnati, OH: $message")

#Confirmation that the script ran successfully
echo 'Message sent successfully'
