from config import path

def getfile(default=None):
    formats = ["", ".txt", ".doc", ".docx"]
    if not default:
        print("Enter the file")
        s = input().strip()
        file = None
    else:
        file = open(default, "r")
    while not file:
        for i in formats:
            try:
                file = open(path + s + i, "r")
            except OSError:
                pass
            else:
                break
        if not file:
            print("File not found")
            s = input().strip()
    return file
