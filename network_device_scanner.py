import os

network = input("Enter network base (example 192.168.1): ")

print("\nScanning network...\n")

for i in range(1, 255):

    ip = f"{network}.{i}"

    response = os.system(f"ping -n 1 -w 100 {ip} > nul")

    if response == 0:
        print(f"{ip} is online")