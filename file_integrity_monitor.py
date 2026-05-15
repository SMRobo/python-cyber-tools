import hashlib
import os

filename = input("Enter file name to monitor: ")

def calculate_hash(file_path):
    sha256 = hashlib.sha256()

    with open(file_path, "rb") as file:
        while chunk := file.read(4096):
            sha256.update(chunk)

    return sha256.hexdigest()

if os.path.exists(filename):

    original_hash = calculate_hash(filename)

    print("\nOriginal Hash:")
    print(original_hash)

    input("\nPress Enter after modifying the file...")

    new_hash = calculate_hash(filename)

    print("\nNew Hash:")
    print(new_hash)

    if original_hash == new_hash:
        print("\nFile integrity intact. No changes detected.")
    else:
        print("\nWARNING: File has been modified!")

else:
    print("File does not exist.")