from utils import getfile
import re

def extract():
    file = open("compilation.txt", "r")
    print("Output name:")
    name = input()
    out = open("../" + name + ".txt", "a")

    text = " ".join(file.readlines())
    res = re.findall("\[([^\[\]]*)\]", text)

    for i in res:
        out.write(i + '\n')

    print("Completed\n")

if __name__ == '__main__':
    extract()
