import os
from config import path

print("Enter a path to the directory")
dir = input().strip()
dir = path + way

out = open(dir+".txt", "a")
for file in os.listdir(way):
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
        print(way, file, ": Encoding error")

print("Completed\n")
