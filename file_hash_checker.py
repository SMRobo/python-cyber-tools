import hashlib

filename = input("Enter file name: ")

sha256_hash = hashlib.sha256()

try:
    with open(filename, "rb") as file:
        while chunk := file.read(4096):
            sha256_hash.update(chunk)

    print("\nSHA256 Hash:")
    print(sha256_hash.hexdigest())

except FileNotFoundError:
    print("File not found.")