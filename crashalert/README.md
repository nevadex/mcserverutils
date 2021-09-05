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
## Linux Guide
---
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
