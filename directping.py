import requests
from datetime import datetime
import time
from mcstatus import JavaServer
import time
import http.client
import urllib

'''
* Made by NorthernChicken
* Repo: https://github.com/NorthernChicken/MCServerPlayerCountLogger
* Desc: Continutally checks the amount of players on a Minecraft server by pinging the server directly
'''

with open('ip.txt', 'r') as file:
    ip = file.read()

api_base = "https://api.mcstatus.io/v2/status/java/"

api_link = api_base + ip

with open('ip.txt', 'r') as file:
    ip = file.read()
server = JavaServer.lookup(ip)

def ping_server(server_ip):
    current_datetime = datetime.now()
    formatted_datetime = current_datetime.strftime("%Y-%m-%d %H:%M:%S")
    server = JavaServer.lookup(server_ip)
    players = server.status()
    if players.players.online == 0:
        print(formatted_datetime, "No one is online.")
        time.sleep(3)
    elif players.players.online > 0:
        print(formatted_datetime, "There are", players.players.online, "players online.")

while True:
    try:
        ping_server(ip)
        time.sleep(10)
    except Exception as e:
        print("Oops, there was an error. Re-trying in 5 seconds.")
        time.sleep(5)