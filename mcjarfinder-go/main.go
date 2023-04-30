package main

import (
	"encoding/json"
	"fmt"
	"io"
	"net/http"
	"os"
)

func main() {
	var versionManifest map[string]interface{}

	resp, err := http.Get("https://launchermeta.mojang.com/mc/game/version_manifest.json")
	if err != nil {
		fmt.Printf("[!] Error occurred while retrieving version_manifest.json:\n%s\n", err.Error())
		os.Exit(1)
	}
	defer resp.Body.Close()

	if err := json.NewDecoder(resp.Body).Decode(&versionManifest); err != nil {
		fmt.Printf("[!] Error occurred while decoding version_manifest.json:\n%s\n", err.Error())
		os.Exit(1)
	}

	var version string
	if len(os.Args) > 1 {
		version = os.Args[1]
	} else {
		version = versionManifest["latest"].(map[string]interface{})["release"].(string)
		fmt.Printf("[!] No version supplied! Defaulting to latest: %s\n", version)
	}

	var filetowrite string
	if len(os.Args) > 2 {
		filetowrite = os.Args[2]
	} else {
		filetowrite = "server-" + version + ".jar"
		fmt.Printf("[!] No filename provided! Defaulting to: %s\n", filetowrite)
	}

	var versionurl string
	var versionJson map[string]interface{}

	fmt.Printf("[*] Operation: Saving %s server jar to \"%s\"\n", version, filetowrite)
	for _, v := range versionManifest["versions"].([]interface{}) {
		if v.(map[string]interface{})["id"].(string) == version {
			versionurl = v.(map[string]interface{})["url"].(string)
			fmt.Printf("[*] Located version %s in version_manifest.json\n", version)
			break
		}
	}
	if versionurl == "" {
		fmt.Printf("[!] Invalid version! %s could not be located in version_manifest.json\n", version)
		os.Exit(1)
	}

	vermanireq, err := http.Get(versionurl)
	if err != nil {
		fmt.Printf("[!] Error occurred while retrieving %s.json:\n%v", version, err)
		os.Exit(1)
	}
	defer vermanireq.Body.Close()

	body, err := io.ReadAll(vermanireq.Body)
	if err != nil {
		fmt.Printf("[!] Error occurred while reading %s.json:\n%v", version, err)
		os.Exit(1)
	}

	err = json.Unmarshal(body, &versionJson)
	if err != nil {
		fmt.Printf("[!] Error occurred while unmarshalling %s.json:\n%v", version, err)
		os.Exit(1)
	}

	jarurl := versionJson["downloads"].(map[string]interface{})["server"].(map[string]interface{})["url"].(string)
	jarsize := versionJson["downloads"].(map[string]interface{})["server"].(map[string]interface{})["size"].(float64)
	jarsha1 := versionJson["downloads"].(map[string]interface{})["server"].(map[string]interface{})["sha1"].(string)
	jarversiontype := versionJson["type"].(string)
	jarjavaversion := int(versionJson["javaVersion"].(map[string]interface{})["majorVersion"].(float64))

	fmt.Printf("[*] Located jar manifest\n")

	jar, err := os.Create(filetowrite)
	if err != nil {
		fmt.Printf("[!] Error occurred while creating %s:\n%v", filetowrite, err)
		os.Exit(1)
	}
	defer jar.Close()

	jarresp, err := http.Get(jarurl)
	if err != nil {
		fmt.Printf("[!] Error occurred while retrieving server.jar:\n%v", err)
		os.Exit(1)
	}
	defer jarresp.Body.Close()

	_, err = io.Copy(jar, jarresp.Body)
	if err != nil {
		fmt.Printf("[!] Error occurred while copying %s to %s:\n%v", jarurl, filetowrite, err)
		os.Exit(1)
	}

	fmt.Printf("[*] Summary:\n     Filename = %s\n    File size = %.0f\n   Version ID = %s\n Version Type = %s\n Java Version = %d\nSHA1 Checksum = %s\n[*] Done!\n", filetowrite, jarsize, version, jarversiontype, jarjavaversion, jarsha1)
	os.Exit(0)
}
