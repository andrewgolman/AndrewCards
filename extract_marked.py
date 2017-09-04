""""Script"""

from utils import getfile


def extract():
    """Extracts from a given file all strings containing a substring s
        Strings will be written without their first symbol.
        Data will be extracted from compilation.txt file."""
    file = open("compilation.txt", "r")
    print("Choose a marking symbol (substring):")
    c = input().strip()
    print("Choose output file path:")
    name = input()
    out = open(name, "a")
    print ("...")

    for line in file:
        if c in line:
            out.write(line[1:])

    print ("Completed")


if __name__ == '__main__':
    extract()
