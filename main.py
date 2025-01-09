import requests
import socket
import json
from concurrent.futures import ThreadPoolExecutor
import os
from pystyle import Colors, Colorate

os.system('cls')

menu_text1 = r"""     
                                     

                                         
                                                                                 
                                     ░▒▓█▓▒░▒▓███████▓▒░ ░▒▓██████▓▒░░▒▓████████▓▒░▒▓██████▓▒░  
                                     ░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░     ░▒▓█▓▒░░▒▓█▓▒░ 
                                     ░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░      ░▒▓█▓▒░     ░▒▓█▓▒░░▒▓█▓▒░ 
                                     ░▒▓█▓▒░▒▓███████▓▒░░▒▓█▓▒▒▓███▓▒░▒▓██████▓▒░░▒▓█▓▒░░▒▓█▓▒░ 
                                     ░▒▓█▓▒░▒▓█▓▒░      ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░     ░▒▓█▓▒░░▒▓█▓▒░ 
                                     ░▒▓█▓▒░▒▓█▓▒░      ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░     ░▒▓█▓▒░░▒▓█▓▒░ 
                                     ░▒▓█▓▒░▒▓█▓▒░       ░▒▓██████▓▒░░▒▓████████▓▒░▒▓██████▓▒░  
                                                           
                                                           
                                   
                                        
                                     ╔══════════════════════════════════════════════════════╗
                                     ║                                                      ║
                                     ║               Enter Your Ip To Scrape                ║
                                     ║                                                      ║
                                     ╚══════════════════════════════════════════════════════╝ 
                        
"""

menu_text2 = r"""     
                                     

                                         
                                                                                 
                                     ░▒▓█▓▒░▒▓███████▓▒░ ░▒▓██████▓▒░░▒▓████████▓▒░▒▓██████▓▒░  
                                     ░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░     ░▒▓█▓▒░░▒▓█▓▒░ 
                                     ░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░      ░▒▓█▓▒░     ░▒▓█▓▒░░▒▓█▓▒░ 
                                     ░▒▓█▓▒░▒▓███████▓▒░░▒▓█▓▒▒▓███▓▒░▒▓██████▓▒░░▒▓█▓▒░░▒▓█▓▒░ 
                                     ░▒▓█▓▒░▒▓█▓▒░      ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░     ░▒▓█▓▒░░▒▓█▓▒░ 
                                     ░▒▓█▓▒░▒▓█▓▒░      ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░     ░▒▓█▓▒░░▒▓█▓▒░ 
                                     ░▒▓█▓▒░▒▓█▓▒░       ░▒▓██████▓▒░░▒▓████████▓▒░▒▓██████▓▒░  
                                                           
                                                           
                                   
                                        
                                     ╔══════════════════════════════════════════════════════╗
                                     ║                                                      ║
                                     ║               Enter Your Webhook Url                 ║
                                     ║                                                      ║
                                     ╚══════════════════════════════════════════════════════╝ 
                        
"""

print(Colorate.Horizontal(Colors.red_to_yellow, menu_text1,1))
ip = input("> ")
os.system('cls')

print(Colorate.Horizontal(Colors.red_to_yellow, menu_text2,1))
webhook = input("> ")

def scan_port(ip, port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(0.5)  
    result = sock.connect_ex((ip, port))
    sock.close()
    return port if result == 0 else None

def scan_ports(ip, start_port, end_port):
    open_ports = []
    with ThreadPoolExecutor(max_workers=20) as executor:  
        results = executor.map(lambda port: scan_port(ip, port), range(start_port, end_port + 1))
        open_ports = [port for port in results if port is not None]  
    return open_ports


start_port = 20 
end_port = 1024 

open_ports = scan_ports(ip, start_port, end_port)

response = requests.get(f"http://ip-api.com/json/{ip}")
api = response.json()
try:
 if api['status'] == "success": status = "Valid"
 else: status = "Invalid"
except: 
 status = "Invalid"

try:
    country_flag = api['country_flag']
except:
    country_flag = "None"

try:
    country = api['country']
except:
    country = "None"

try:
    country_code = api['countryCode']
except:
    country_code = "None"

try:
    region = api['regionName']
except:
    region = "None"

try:
    region_code = api['region']
except:
    region_code = "None"

try:
    zip = api['zip']
except:
    zip = "None"

try:
    city = api['city']
except:
    city = "None"

try:
    latitude = api['lat']
except:
    latitude = "None"

try:
    longitude = api['lon']
except:
    longitude = "None"

try:
    timezone = api['timezone']
except:
    timezone = "None"

try:
    isp = api['isp']
except:
    isp = "None"

try:
    org = api['org']
except:
    org = "None"

try:
    as_host = api['as']
except:
    as_host = "None"

embed = {
    "title": f"`🔎` IP SIMMER - RESULTS | {ip}",
    "color": 0x00ffee,
    "fields": [
        {
            "name": "`🌍` Country",
            "value": f"```{country}```",
            "inline": True
        },
        {
            "name": "`🔢` Country Code",
            "value": f"```{country_code}```",
            "inline": True
        },
        {
            "name": "`📫` Region",
            "value": f"```{region}```",
            "inline": True
        },
        {
            "name": "`💌` Region Code",
            "value": f"```{region_code}```",
            "inline": True
        },
        {
            "name": "`🔗` Zip",
            "value": f"```{zip}```",
            "inline": True
        },
        {
            "name": "`🏙️` City",
            "value": f"```{city}```",
            "inline": True
        },
        {
            "name": "`🌐` Location",
            "value": f"```{latitude}/{longitude}```",
            "inline": True
        },
        {
            "name": "`⌚` Timezone",
            "value": f"```{timezone}```",
            "inline": True
        },
        {
            "name": "`💊` ISP",
            "value": f"```{isp}```",
            "inline": True
        },
        {
            "name": "`🎯` Latitude Longitude",
            "value": f"```{latitude}, {longitude}```",
            "inline": True
        },
        {
            "name": "`💿` Org",
            "value": f"```{org}```",
            "inline": True
        },
        {
            "name": "`🔓` Open Ports",
            "value": f"```{', '.join(map(str, open_ports))}```" if open_ports else "```No open ports found```",
            "inline": False
        }
    ]
}


payload = {
    "username": "IP SIMMER",  
    "embeds": [embed]  
}

r = requests.post(webhook, json=payload)

option = input("")