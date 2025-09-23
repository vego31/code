import json
from pythonping import ping


print("Welcome to server pinger")
print("1. Add server")
print("2. show servers status")
option = input("Choose an option:")

def addserver():
    print("add server")
    
    server = input("server name:")
    print("server name is %s" % server)
    ip = input("server ip:")
    print("server ip is %s" % ip)
    
    jsondata = {}
    jsondata["id"] = server
    jsondata["server"] = server
    jsondata["ip"] = ip
    
    with open("servers.json", "a") as f:
        json.dump(jsondata, f)
        f.write("\n")














if option == "1":
    addserver()

