from utils import getfile
from config import path

path = ".."

def sort(name, dir, file, number, size):
    """
    Splits a given file (path+dir+name) to a few files, each of them contains a given certain number of not empty
    strings (size).
    Enumeration of files starts with arg number.
    Args: name, dir, file - string, number, size - int.
    """
    while True:
        out = open(path + "/" + dir + "/" + name + str(number), "a")
        for i in range(size):
            s = file.readline()
            if not s:
                break
            out.write(s)
        if not s:
                break
        number += 1
    return number


if __name__ == '__main__':
    print("Enter a name for the pack:")
    name = input()
    
    print("Enter a folder name to put the files in:")
    dir = input()
    
    print("Enter a file to be parsed:")
    file = getfile()
    
    print("Size of one pack (20 by default):")
    try:
        size = int(input().strip())
    except Exception:
        print("Set size 20.")
        size = 20
    
    print("Starting number (1 by default):")
    try:
        file_no = int(input().strip())
    except Exception:
        print("Set no 1.")
        file_no = 1

    sort(name, dir, file, file_no, size)

    print("...")
    print("Completed\n")
