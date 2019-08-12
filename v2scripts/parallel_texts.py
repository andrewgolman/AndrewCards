import argparse


def main(working_file, rev=False):
    with open(working_file) as input_file:
        data = input_file.read()
        if "=" not in data:
            raise RuntimeError("'=' separator is not found")
        first, second = data.split("=", maxsplit=1)
        first = first.split(".")
        second = second.split(".")
        if len(first) != len(second):
            raise RuntimeError("Different number of sentences")
        print(f"{len(first)} sentences parsed.")
        for i, s in enumerate(zip(first, second)):
            print(f"{i}. {s[rev].strip()}", end="")
            input()
            print("...............", s[not rev].strip())
            print()


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("file")
    parser.add_argument("-r", action="store_true")
    args = parser.parse_args()
    main(working_file=args.file, rev=args.r)
