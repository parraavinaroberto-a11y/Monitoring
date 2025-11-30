import socket

def check_tcp(host, port, timeout=3):
    try:
        with socket.create_connection((host, port), timeout=timeout):
            return True
    except Exception:
        return False

if __name__ == "__main__":
    print("MySQL:", check_tcp("localhost", 3306))
    print("Redis:", check_tcp("localhost", 6379))
