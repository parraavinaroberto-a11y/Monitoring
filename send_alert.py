import requests
import json

def send_alert(message, webhook_url):
    payload = {"text": message}
    resp = requests.post(
        webhook_url,
        data=json.dumps(payload),
        headers={"Content-Type": "application/json"},
    )
    return resp.status_code

if __name__ == "__main__":
    send_alert("⚠️ CPU alta en el servidor", "TU_WEBHOOK")
