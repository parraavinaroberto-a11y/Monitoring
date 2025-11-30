import psutil
import json
import time

def get_system_metrics():
    return {
        "timestamp": time.time(),
        "cpu_percent": psutil.cpu_percent(interval=1),
        "memory_percent": psutil.virtual_memory().percent,
        "disk_percent": psutil.disk_usage("/").percent,
        "load_avg": psutil.getloadavg() if hasattr(psutil, "getloadavg") else None
    }

if __name__ == "__main__":
    metrics = get_system_metrics()
    print(json.dumps(metrics, indent=2))
