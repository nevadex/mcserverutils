# MC Jar Finder
Command line vanilla-minecraft server jar download utility, written in Python  
## Dependencies
Modern version of python, preferably >= 3.8  
Run `pip3 install requests`
## Usage
On command line:  
`python3 mcjarfinder.py [ver] [fileToWrite]`  
Example:  
`python3 mcjarfinder.py 1.8.9 server189.jar`  
Example output:
```
[*] Operation: Saving 1.8.9 server jar to "server189.jar"
[*] Located version 1.8.9 in version_manifest.json
[*] Located jar manifest
[*] Downloading jarfile
[*] Done!
[*] Summary:
     Filename = server189.jar
    File size = 8320755
   Version ID = 1.8.9
 Version Type = release
 Java Version = 8
SHA1 Checksum = b58b2ceb36e01bcd8dbf49c8fb66c55a9f0676cd
```
