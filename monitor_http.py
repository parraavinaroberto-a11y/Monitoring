import requests
import time

def check_http(url, timeout=3):
    start = time.time()
    try:
        r = requests.get(url, timeout=timeout)
        latency = (time.time() - start) * 1000
        return {
            "up": r.status_code < 500,
            "status": r.status_code,
            "latency_ms": latency
        }
    except requests.RequestException:
        return {"up": False, "status": None, "latency_ms": None}

if __name__ == "__main__":
    result = check_http("https://www.google.com")
    print(result)
