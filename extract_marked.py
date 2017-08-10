from utils import getfile

def extract():
    file = open("compilation.txt", "r")
    print("Choose a marking symbol (subline):")
    c = input().strip()
    print("Choose output file name:")
    name = input()
    out = open("../" + name, "a")
    print ("...")

    for line in file:
        if c in line:
            out.write(line[1:])

    print ("Completed")


if __name__ == '__main__':
    extract()
