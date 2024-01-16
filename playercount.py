import requests
from datetime import datetime
import time
import ctypes

'''
* Script by skokcoder (HackerB0i)
* Desc: Continutally checks the amount of players on a Minecraft server using mcstatus.io's API, displays a message when a specified amount of people are online, then stops
'''
  
targetamt = int(input("Target amount of people: "))

bold_start = "\033[1m"
bold_end = "\033[0m"

api_base = "https://api.mcstatus.io/v2/status/java/"

with open('ip.txt', 'r') as file:
    ip = file.read()

api_link = api_base + ip

while True:
    try:
        response = requests.get(api_link)

        current_datetime = datetime.now()
        formatted_datetime = current_datetime.strftime("%Y-%m-%d %H:%M:%S")
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
            print("*---------------------------------")
            print(f"{bold_start}{formatted_datetime}{bold_end}")
            print("Server Status:", formatted_status)
            print("Players Online:", players_online)
            print("*---------------------------------")
            with open("log.txt", 'a') as file:
                file.write(formatted_datetime + " Server is " + formatted_status + ". " + str(players_online) + " players\n")
            if players_online >= targetamt:
                ctypes.windll.user32.MessageBoxW(0, f"Your specified player amount ({targetamt}) has been reached.", "!! TARGET AMOUNT REACHED !!", 0)
                break
            time.sleep(3)
        elif response.status_code == 404:
            print("Minecraft server not found or MCStatus API is down. Check server address and try again.")
            with open("log.txt", 'a') as file:
                file.write(formatted_datetime + " Minecraft server not found or MCStatus API is down.")
            time.sleep(5)
        elif response.status_code == 429:
            print("Too many requests. Please wait...")
            with open("log.txt", 'a') as file:
                file.write(formatted_datetime + " Sent too many requests.")
            time.sleep(10)
        elif response.status_code == 500:
            print("Internal server error. Please wait...")
            with open("log.txt", 'a') as file:
                file.write(formatted_datetime + " Internal server error.")
            time.sleep(10)
        elif response.status_code == 400:
            print("Invalid server IP. Check spelling and try again.")
            with open("log.txt", 'a') as file:
                file.write(formatted_datetime + " Invalid server IP.")
            break
        else:
            print("Error:", response.status_code)
            with open("log.txt", 'a') as file:
                file.write(formatted_datetime + " An error occured. Error code: " + response.status_code)
            time.sleep(5)
    except Exception as e:
        print("Sorry, an unkown error occured. Retrying...")
        with open("log.txt", 'a') as file:
                file.write("An unknown error occured.")
        time.sleep(2)
