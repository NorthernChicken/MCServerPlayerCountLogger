# Log On Notifier
This is a modified version of NorthChicken's player logger. Changes include a player list/server recon detector, countdown timer until refresh, clearing the console to show a singular message, and desktop notifications. This program was specifically written to notify the user when a certain player amount has been reached on the specified server, and will stop once that number is reached. You can change the player count to a large number if you want to keep the program running. If you would like to see the time/date the player count changed, or would like to see the player list at a certain time, check log.txt. The server IP you are listening for is in the ip.txt file. Change it to whatever server IP you would like.

*Note* Times might be inaccurate up to 30 seconds because Mcstatus's API can take time to update.
*Another note* Servers must have server recon enabled in the config for the player list to work. Large servers usually have this turned off.

# Install
* Requires Python to run
* import the package win10toast for program functionality.
