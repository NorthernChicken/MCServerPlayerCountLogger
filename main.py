import requests
from datetime import datetime
import time

'''
* Made by NorthernChicken
* Repo: https://github.com/NorthernChicken/MCServerPlayerCountLogger
* Desc: Continutally checks the amount of players on a Minecraft server using mcstatus.io's API
'''

with open('ip.txt', 'r') as file:
    ip = file.read()

bold_start = "\033[1m"
bold_end = "\033[0m"

api_base = "https://api.mcstatus.io/v2/status/java/"

api_link = api_base + ip

while True:
    response = requests.get(api_link)

    if response.status_code == 200:
        json_data = response.json()
        players_online = json_data.get("players", {}).get("online", 0)
        online_status = json_data['online']
        if online_status:
            formatted_status = "Online"
        elif not online_status:
            formatted_status = "Offline"
        else:
            formatted_status = "Unknown"
        current_datetime = datetime.now()
        formatted_datetime = current_datetime.strftime("%Y-%m-%d %H:%M:%S")
        print("*---------------------------------")
        print(f"{bold_start}{formatted_datetime}{bold_end}")
        print("Server Status:", formatted_status)
        print("Players Online:", players_online)
        print("*---------------------------------")
        with open("log.txt", 'a') as file:
            file.write(formatted_datetime + " Server is " + formatted_status + ". " + str(players_online) + " players\n")
        time.sleep(3)
    else:
        print("Error:", response.status_code)
        time.sleep(5)
