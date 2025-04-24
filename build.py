import os, sys, shutil, urllib.request

folders = ["src", "bin", "docs", "resrc", "resrc/audio", "resrc/image"]
links = {
    "win32":"https://github.com/love2d/love/releases/download/11.5/love-11.5-win64.zip",
    "linux":"https://github.com/love2d/love/releases/download/11.5/love-11.5-x86_64.AppImage",
    "darwin":"https://github.com/love2d/love/releases/download/11.5/love-11.5-macos.zip" 
}

def init():

    for f in folders:
        if os.path.exists(f):
            print(f"[!] {f} already exists.")
            continue
        os.mkdir(f)
        print(f"[✔] {f} created.")

    _os = sys.platform
    print(f"PLATFORM: {_os}")
    if not os.path.exists("love2d"):
        if _os == "win32":
            urllib.request.urlretrieve(links[_os], "love.zip")
            shutil.unpack_archive("love.zip")
            os.rename("love-11.5-win64", "love2d")
            os.remove("love.zip")
        #elif _os == "linux":
        #    urllib.request.urlretrieve(links[_os], "love.AppImage")
        #elif _os == "darwin":
        #    urllib.request.urlretrieve(links[_os], "love.zip")

    with open("main.lua", "w") as f:
        f.write("function love.draw()\n\tlove.graphics.print(\"Hello World\", 400, 300)\nend")

def run():
    os.system(".\\love2d\\love.exe .")

def main():
    arg_len = len(sys.argv)
    if arg_len < 2 or arg_len > 2:
        print("python build.py [init | run]")
        exit(1)
    cmd = sys.argv[1]
    if cmd == "init":
        init()
    elif cmd == "run":
        run()
    else:
        print(f"Unknown Command: ({cmd})")

if __name__ == "__main__":
    main()