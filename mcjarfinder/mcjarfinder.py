#!/usr/bin/python

# usage: python mcjarfinder.py [ver] [filetowrite]
# ex: python mcjarfinder.py 1.8.9 server.jar
# written in python 3.8, tested on 3.8, 3.9

import sys
import requests
import urllib.request

try:
    versmanireq = requests.get("https://launchermeta.mojang.com/mc/game/version_manifest.json")
    versmanireq.raise_for_status()
    versionManifest = versmanireq.json()
except Exception as ex:
    print(f"[!] Error occurred while retrieving version_manifest.json:\n{ex}")
    sys.exit()

try:
    version = sys.argv[1]
except:
    print(f"[!] No version supplied! Defaulting to latest: " + versionManifest["latest"]["release"])
    version = versionManifest["latest"]["release"]

try:
    filetowrite = sys.argv[2]
except:
    print(f"[!] No filename provided! Defaulting to \"server-{version}.jar\"")
    filetowrite = "server.jar"

versionurl = None
print(f"[*] Operation: Saving {version} server jar to \"{filetowrite}\"")
for key in versionManifest["versions"]:
    if key["id"] == version:
        versionurl = key["url"]
        print(f"[*] Located version {version} in version_manifest.json")
        break
else:
    print(f"[!] Invalid version! {version} could not be located in version_manifest.json")
    sys.exit()

try:
    vermanireq = requests.get(versionurl)
    vermanireq.raise_for_status()
    versionJson = vermanireq.json()
except Exception as ex:
    print(f"[!] Error occurred while retrieving {version}.json:\n{ex}")
    sys.exit()

try:
    jarurl = versionJson["downloads"]["server"]["url"]
    jarsize = versionJson["downloads"]["server"]["size"]
    jarsha1 = versionJson["downloads"]["server"]["sha1"]
    jarversiontype = versionJson["type"]
    jarjavaversion = versionJson["javaVersion"]["majorVersion"]
    print(f"[*] Located jar manifest")
except:
    print(f"[!] Error occurred while processing {version}.json")

try:
    print(f"[*] Downloading jarfile")
    jar = urllib.request.urlretrieve(jarurl, filetowrite)
except Exception as ex:
    print(f"[!] Error occurred while retrieving server.jar:\n{ex}")

print(f"[*] Summary:\n     Filename = {filetowrite}\n    File size = {jarsize}\n   Version ID = {version}\n Version Type = {jarversiontype}\n Java Version = {jarjavaversion}\nSHA1 Checksum = {jarsha1}")
print("[*] Done!")
sys.exit()
