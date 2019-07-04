from utils import getfile
import re

file = getfile()
print("Output name:")
name = input()
out = open("../" + name + ".txt", "a")

k = False
in_numbering = False
for line in file:
    if not in_numbering or not (line[0] in "1234567890"):
        k = not k
    in_numbering = (line[0] in "1234567890")
    if k:
        out.write("\n" + line[:-1] + " - ")
    else:
        out.write(line[:-1])

print("Completed\n")
