from utils import getfile
from config import path
from config import compilation_file
from sort import sort

file = open(compilation_file, "r")
print("Choose output file name:")
print("(This name will be used as a main file title)")
name = input()

print("Enter p-file number:")
p_number = int(input().strip())

print("Enter w-file number:")
w_number = int(input().strip())

out_p = open("../grundkurs/" + name + "p", "a")
out_w = open("../grundkurs/" + name + "w", "a")
p = 0
w = 0

print ("...")

for line in file:
    if not line.strip():
        continue;
    if "►" in line:
        out_p.write(line[1:])
        p += 1
    else:
        out_w.write(line)
        w += 1

print(p, " phrases scanned")
print(w, " words scanned")

p_file = open("../grundkurs/" + name + "p", "r")
w_file = open("../grundkurs/" + name + "w", "r")
sort(name="p", dir="grundkurs", number=p_number, file=p_file, size=30)
sort(name="w", dir="grundkurs", number=w_number, file=w_file, size=20)

print ("Completed")
