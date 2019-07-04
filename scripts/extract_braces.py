""""Script"""

from utils import getfile
import re


def extract():
    """Extracts from a given file all substrings between brackets
        Data is taken from compilation.txt ."""
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
