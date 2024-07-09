# MCServerPlayerCountLogger
The first script will get the number of players on a Minecraft server and log it in the console and a text file. Uses Mcstatus.io's API.
The second will notify you in the terminal if the player count reaches a certain amount.
directping.py will do the same as main.py except using direct pings instead of an API. Usually this results in faster updates.

```pll.py``` and ```pll.sh``` are shortcut scripts for ```playerlist_logger.py```, working universally and only on Linux, respectively. ```pll.sh``` sets ```pll``` as an alias for the script.

*Note* Times might be inaccurate up to 30 seconds because Mcstatus's API can take time to update.

# Install
* Requires git and python
* Download repo: ```git clone github.com/NorthernChicken/MCServerPlayerCountLogger```
* Change to the directory ```cd MCServerPlayerCountLogger``` from wherever it was downloaded to
* run ```python main.py``` for the playercountlogger or ```python playercount.py``` for the player amount notifier.
* the log is stored in ```log.txt```

# Example output
![Screenshot 2024-01-12 121501](https://github.com/NorthernChicken/MCServerPlayerCountLogger/assets/144752748/17134a2e-422a-4175-8b00-671f6e421e27)

# Example log
![Screenshot 2024-01-12 123143](https://github.com/NorthernChicken/MCServerPlayerCountLogger/assets/144752748/7f2a9c28-e4ce-47fb-a952-03e2bd67db4d)
