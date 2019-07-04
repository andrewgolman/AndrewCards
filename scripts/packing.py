"""

This script packs all strings from files from a certain directory into one file.

"""

import os
from config import path

print("Enter a path to the directory")
dir = input().strip()
dir = path + dir

out = open(dir+".txt", "a")
for file in os.listdir(dir):
    if file[0] == ".":
        continue

    lines = open(dir+"/"+file, "r")
    encoding = True
    try:
        for line in lines:
            out.write(line)
    except (UnicodeError, UnicodeDecodeError):
        encoding = False
    if not encoding:
        print(dir, file, ": Encoding error")

print("Completed\n")
