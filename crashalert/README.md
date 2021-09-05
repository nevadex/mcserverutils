# Crash Alert and Server Restart Scripts
### Utilities to assist in self-hosted and some commercially hosted servers to notify someone(s) of a server crashing via Discord
---
# Where to Use
These scripts can be used hand-in-hand to alert someone of a server going down, before attempting to start back up. They are both very light scripts, and should not cause harm to your computer.
> Compatible with Windows and Linux. Only works with Minecraft server builds that have an option to execute a script at restart(Spigot, Paper, etc)

> Prerequisites: Python3+, pip3 packages ```requests``` and ```json```, and a text editor(Notepad++, Sublime, etc.) [Prereq. install guide here](#Prerequisites-Installation)
---
# Installation Guide
Assuming the prereqs are already installed, you can continue with the setup.

## Windows Guide

**Initial Setup**
1. Clone the files ```restart.bat``` and ```crash-alert-v2.py``` from github
2. Place both files into the Minecraft server directory, the same folder where the ```.jar``` is
3. Within the server config file(spigot: ```spigot.yml```, etc.), make sure that the server WILL attempt to restart on a crash
4. In the file, set the restart script to ```.\restart.bat```

**Script Setup**
1. Open ```restart.bat``` in a text editor such as Notepad++
2. On Line 8, put your server start command.
*Advanced: If your computer has several python versions installed, change the command on Line 4 to match the latest installed version.*
3. Save and close ```restart.bat```.

> Before continuing, create a Discord webhook in a channel of your choice, and keep the link handy.

**Alert Setup**
1. Open ```crash-alert-v2.py``` in a text editor such as Notepad++
2. On line 7, paste your webhook link inside the doublequotes.
3. On line 10, put your Minecraft server's name inside the doublequotes. If your server has no name, leave blank.
4. On line 18, put any users or roles you want to ping. Follow instructions listed inside the file or [this Reddit post](https://www.reddit.com/r/discordapp/comments/61n0sj/pinging_rolesusers_linking_text_channels_through/dfftv3p/). To ping nobody, leave blank.
5. Save and close ```crash-alert-v2.py```.

The setup and configuration is now complete.
NOTE: When the ```/restart``` command is used, the server will restart using this tool, and will send an alert.

## Linux Guide

**Initial Setup**
1. Clone the files ```restart.sh``` and ```crash-alert-v2.py``` from github
2. Place both files into the Minecraft server directory, the same folder where the ```.jar``` is
3. Within the server config file(spigot: ```spigot.yml```, etc.), make sure that the server WILL attempt to restart on a crash
4. In the file, set the restart script to ```.\restart.sh```

**Script Setup**
1. Open ```restart.sh``` in a text editor such as Notepad++
2. On Line 8, put your server start command.
*Advanced: If your computer has several python versions installed, change the command on Line 5 to match the latest installed version.*
3. Save and close ```restart.bat```.

> Before continuing, create a Discord webhook in a channel of your choice, and keep the link handy.

**Alert Setup**
1. Open ```crash-alert-v2.py``` in a text editor such as Notepad++
2. On line 7, paste your webhook link inside the doublequotes.
3. On line 10, put your Minecraft server's name inside the doublequotes. If your server has no name, leave blank.
4. On line 18, put any users or roles you want to ping. Follow instructions listed inside the file or [this Reddit post](https://www.reddit.com/r/discordapp/comments/61n0sj/pinging_rolesusers_linking_text_channels_through/dfftv3p/). To ping nobody, leave blank.
5. Save and close ```crash-alert-v2.py```.

The setup and configuration is now complete.
NOTE: When the ```/restart``` command is used, the server will restart using this tool, and will send an alert.
--- ---
# Prerequisites Installation
How to install the packages required for this utility

## Windows Guide
If Python is not installed already(check by searching Python):
1. Download the python install executable from [here](https://www.python.org/downloads/). It should be at the top with a yellow button for the latest stable version.
2. Open/Run the executable and follow its instructions to install python

Install packages: 
1. Open CMD as Administrator.
2. Enter ```pip3 help```. This should output a help blob with commands for PyPi, python's package manager. If this does not open, you need to install PyPi using [this guide](https://opensource.com/article/20/3/pip-linux-mac-windows)
3. With CMD still open as administrator, type ```pip3 install requests```. This will install the ```requests``` package.
4. Now enter ```pip3 install json```

## Linux Guide
Most Linux installations come with Python preinstalled. If yours does not, google a tutorial for your flavor of linux.

Install packages:
1. Open terminal
2. Enter ```pip3 help```. This should output a help blob with commands for PyPi, python's package manager. If this does not open, you need to install PyPi using [this guide](https://opensource.com/article/20/3/pip-linux-mac-windows)
3. In the terminal, type ```pip3 install requests```. This will install the ```requests``` package.
4. Now enter ```pip3 install json```
