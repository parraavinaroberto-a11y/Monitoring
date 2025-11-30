import os
import platform

def ping(host="8.8.8.8"):
    param = "-n" if platform.system().lower() == "windows" else "-c"
    exit_code = os.system(f"ping {param} 1 {host} > /dev/null 2>&1")
    return exit_code == 0

if __name__ == "__main__":
    host = "8.8.8.8"
    if ping(host):
        print(f"PING OK → {host}")
    else:
        print(f"PING FAIL → {host}")
