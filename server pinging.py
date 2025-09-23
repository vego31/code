import json
from pythonping import ping
import re


print("Welcome to server pinger")
print("1. Add server")
print("2. show servers status")
option = input("Choose an option:")


def is_valid_ip(ip):
    # Regular expression for IPv4 validation
    pattern = r'^(\d{1,3}\.){3}\d{1,3}$'
    if not re.match(pattern, ip):
        return False
    # Check if each octet is between 0 and 255
    octets = ip.split('.')
    return all(0 <= int(octet) <= 255 for octet in octets)

def addserver():
    print("add server")
    
    server = input("server name:")
    print("server name is %s" % server)
    
    while True:
        ip = input("server ip:")
        if is_valid_ip(ip):
            print("server ip is %s" % ip)
            break
        else:
            print("Invalid IP address. Please enter a valid IPv4 address (e.g., 192.168.1.1)")
    
    new_server = {
        "id": server,
        "server": server,
        "ip": ip
    }
    
    try:
        # Read existing servers
        with open("servers.json", "r") as f:
            servers = json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        servers = []
    
    # Add new server to array
    servers.append(new_server)
    
    # Write back entire array
    with open("servers.json", "w") as f:
        json.dump(servers, f, indent=4)








def getserverinfo():
    print("show server status")
    try:
        with open("servers.json", "r") as f:
            servers = json.load(f)
        server_list = []
        for server in servers:
            server_list.append( "server: %s, ip: %s" % (server["server"], server["ip"]))
        return server_list
        
    except (FileNotFoundError, json.JSONDecodeError):
        print("No servers found.")
        return




def pingserver():
    server_list = getserverinfo()
    if server_list is None:
        return
    for server in server_list:
        ip = server.split("ip: ")[1]
        ping_response = ping(ip, count=1, timeout=2)
        
        if ping_response.success():
            print("Server %s is online." % server)
        return ping_response
        

def showserverstaus():
    pingserver()
    print (pingserver())





if option == "1":
    addserver()

if option == "2":
    print(pingserver())