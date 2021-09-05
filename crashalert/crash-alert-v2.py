import requests
import json

# Configuration

# Create a webhook in a discord channel, and put the URL here.
webhookUrl = ""

# If your server has a name, place here. If not, leave blank.
serverName = ""

# List any discord Users or Roles to ping in the list below.
# You need the user ID or role ID to ping them. These can be
# found by typing the ping out in the chat box, and then
# placing a backslash( \ ) before it, ex. \@User or \@Moderator
# User ID: <@123...> Role ID: <@&123...>
# These IDs can be put in the string separated by whitespace
pingList = "" # leave empty to ping nobody

# End Configuration



# License

#   MIT License
#
#   Copyright (c) 2021 Nevadex
#
#   Permission is hereby granted, free of charge, to any person obtaining a copy
#   of this software and associated documentation files (the "Software"), to deal
#   in the Software without restriction, including without limitation the rights
#   to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
#   copies of the Software, and to permit persons to whom the Software is
#   furnished to do so, subject to the following conditions:
#
#   The above copyright notice and this permission notice shall be included in all
#   copies or substantial portions of the Software.
#
#   THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
#   IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
#   FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
#   AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
#   LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
#   OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
#   SOFTWARE.

# End License



# Note:
# Hey, I know you wanna see the code, so here it is. Please leave the branding in the code, as it can help others discover the other useful tools I have created.
# But, according to the license, you can modify it. So go ahead, modify if you want. But please leave branding alone. Thanks for using MCServerUtils! - nevadex

template = "{\"content\":\"add_pings\",\"embeds\":[{\"title\":\":warning: Server Crashed! :warning:\",\"description\":\"A Minecraft server has crashed! The server may have been restarted by this utility.\",\"color\":13512495,\"author\":{\"name\":\"server_name\"},\"footer\":{\"text\":\"MC Server Utils by Nevadex\"}}],\"username\":\"Server_Crash_Alert\"}"
data = json.loads(template) # create dict based on template

pingDict = []

if pingList == "":
    data["content"] = "" # make the msg content empty if no pings are defined
else:
    pingDict = pingList.split()
    data["content"] = ""
    for i in pingDict: # add each ping to the msg content
        data["content"] = data["content"] + i + " "

if serverName == "":
    data["embeds"][0]["author"]["name"] = "Minecraft Server" # make the server name in msg embed empty if no name is defined
else:
    data["embeds"][0]["author"]["name"] = serverName # set the server name in msg embed to one defined in config

output = requests.post(webhookUrl, data=json.dumps(data), headers={"Content-Type": "application/json"}) # send request
try:
    output.raise_for_status()
except requests.exceptions.HTTPError as err:
    print(err)
else:
    print("Successfully sent alert")
