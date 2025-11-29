import json
from pythonping import ping
import re
import time






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
        "ip": ip,
        "server_conter": serverconter() + 1
        
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
    menu()
# Add server info to servers.json file

def serverconter():
    with open("servers.json", "r") as f:
        servers = json.load(f)

    server_conter = 0
    for server in servers:
        server_conter += 1

    return server_conter


def removeserver():


   
        with open("servers.json", "r") as f:
            servers = json.load(f)

        
        for server in servers:
            server_list = []
            server_list.append( "server: %s, ip: %s" % (server["server"], server["ip"])) 
            
            print(server_list)

            removeserver = input("Enter the server name to remove: ")
            if server["server"] == removeserver:
                servers.remove(server)
                print(f"Server {removeserver} has been removed.")
                menu()
            else:
                print(f"Server {removeserver} not found.")
                menu()
           
            

            print(server_list)

 



    




def pingserver():
    print("show server status")
    try:
        with open("servers.json", "r") as f:
            servers = json.load(f)
        
        for server in servers:
            server_list = []
            server_list.append( "server: %s, ip: %s" % (server["server"], server["ip"]))
            print(server_list)
           

            ping_response = ping(server["ip"], count=1, timeout=2)
            if ping_response.success():
                ping == True
                print(f"Server {server['server']} ({server['ip']}) is reachable.")
            else:
                print(f"Server {server['server']} ({server['ip']}) is not reachable.")
                ping == False
            time.sleep(1)  # Pause for a second between pings

        if ping == True:
            print(ping_response)
            
        elif ping == False:
            print("No response received.")

        menu()    

            
    


    except (FileNotFoundError, json.JSONDecodeError):
        print("No servers found.")
        menu()

# Get server info from servers.json file





def menu():

    print("Select an option:")
    print("1. Add Server")
    print("2. Ping Servers")
    print("3. Remove Server")
    print("4. Exit")
    option = input("Enter option (1 or 2): ")
    
    if option == "1":
     addserver()

    
    if option == "2":
        pingserver()

    if option == "3":
        removeserver()

    if option == "4":
        return

menu()





