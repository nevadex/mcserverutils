# MC Jar Finder (Golang)
same thing as the other mcjarfinder, just rewritten in golang
> this has been tested on `go version go1.18.1 windows/amd64`

## Compiling
1. download and install golang (varies per OS)
2. download `main.go` and `go.mod` to a folder
3. in that folder, run `go build`
4. use the new binary the same way as the python one, just instead of `python3 mcjarfinder.py` you can call the executable directly.  linux: `./main.exe` windows: `.\main.exe`  

the binary can be renamed and moved wherever

## Using as a Library
**for those experienced with golang!**  
1. rename the package to something else (ex. `mcjarfinder`)
2. change the `main` function signature to `main(in1 string, in2 string)`
3. make an array where `a[0]=nil`, `a[1]=in1` and `a[2]=in2`
4. replace all instances of `os.Args` with this array
5. should now work as any old source library
