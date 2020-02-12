import socket, sys
def getHostnameBYIP(h):
    try:
        hostname = str(h)
        ip = socket.gethostbyname(hostname)
        print (hostname +' has an IP of ' + ip)
    except:
        print("Oops, something is wrong with that host")
getHostnameBYIP(sys.argv[1])

hosts = ['www.uc.edu', 'www.google.com', 'www.reddit.com']

##print ('Working from host: ' + socket.getfqdn())
for h in hosts:
    print (h + ": " + socket.gethostbyname(h))

