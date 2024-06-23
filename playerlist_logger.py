'''
* Fork of skok's log on notifier, a fork of this repository
* Desc: Continutally checks the amount of players on a Minecraft server using mcstatus.io's API
'''

import requests
from datetime import datetime
import time
import os

countdown = 0 # refresh countdown

with open('ip.txt', 'r') as file:
    ip = file.read()

api_base = "https://api.mcstatus.io/v2/status/java/"
api_link = api_base + ip
print(api_link)

bold_start = "\033[1m"
bold_end = "\033[0m"

while True:
    response = requests.get(api_link)
    os.system("cls")
    if response.status_code == 200:
        if countdown == 0:
            formatted_player_list = []
            json_data = response.json()
            players_online = json_data.get("players", {}).get("online", 0)
            player_list = json_data.get("players", {}).get("list", 0)
            if len(player_list) > 0:
                for player in player_list:
                    formatted_player_list.append(player["name_raw"])
            online_status = json_data['online']
            if online_status:
                formatted_status = "Online"
            elif not online_status:
                formatted_status = "Offline"
            else:
                formatted_status = "Unknown"
            countdown = 5
        print("*---------------------------------")
        current_datetime = datetime.now()
        formatted_datetime = current_datetime.strftime("%Y-%m-%d %H:%M:%S")
        print(f"{bold_start}{formatted_datetime}{bold_end}")
        print("Server Status:", formatted_status)
        print("Players Online:", players_online)
        if len(player_list) == 0 and players_online > 0:
            print(f"Server Recon is not turned on.")
        else:
            print(f"Player List: {formatted_player_list}")
        print(f"Updating in {countdown} seconds.")
        print("*---------------------------------")
        with open("log.txt", 'a') as file:
            file.write(formatted_datetime + " Server is " + formatted_status + ". " + str(players_online) + f" players, player list: {formatted_player_list}\n")
        time.sleep(1)
        countdown -= 1
    else:
        print("Error:", response.status_code)
        time.sleep(5)