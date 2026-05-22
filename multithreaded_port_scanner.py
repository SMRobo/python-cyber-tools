import socket
import threading

target = input("Enter the target IP or wesbite: ")

print(f"\nScanning target: {target}\n")

lock = threading.Lock()

def scan_port(port):

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    socket.setdefaulttimeout(0.5)

    result = s.connect_ex((target, port))

    if result == 0:
        with lock:
            print(f"Port {port} is open")
    
    s.close()

threads = []

for port in range(1, 1025):

    thread = threading.Thread(target=scan_port, args=(port,))
    threads.append(thread)

    thread.start()

for thread in threads:
    thread.join()

print("\nScanning completed.")
