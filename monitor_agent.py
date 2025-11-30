import json
import time
from monitor_ping import ping
from monitor_http import check_http
from monitor_tcp import check_tcp
from monitor_system import get_system_metrics

def monitor():
    data = {
        "timestamp": time.time(),
        "ping_google": ping("8.8.8.8"),
        "http_google": check_http("https://www.google.com"),
        "tcp_mysql": check_tcp("localhost", 3306),
        "system": get_system_metrics()
    }
    return data

if __name__ == "__main__":
    while True:
        result = monitor()
        print(json.dumps(result, indent=2))
        
        # Guardar en archivo
        with open("monitor_log.jsonl", "a") as f:
            f.write(json.dumps(result) + "\n")
        
        time.sleep(10)
