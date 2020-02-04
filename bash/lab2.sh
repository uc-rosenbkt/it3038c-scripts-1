#This script will send an email including the IP address, hostname, username, and bash version.
ip=$(ip a | grep 'dynamic ens192' | awk '{print $2}')
username=$USER
hostname=$HOSTNAME
version=$BASH_VERSION
date=$(date +"%m-%d-%Y" at "%H:%M:%S")
emailaddress=maxsayers47@yahoo.com
content="User $username from $ip with hostname $hostname on $date running bash version $version"
mail -s "IT3038C Linux Info" $emailaddress <<< $(echo -e $content)
