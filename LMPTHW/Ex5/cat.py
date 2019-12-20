import argparse
import sys

parser = argparse.ArgumentParser(description='concatenate and print files')
parser.add_argument("files", nargs="*")
parser.add_argument("-n", action="store_true", help="Number the output lines, starting at 1.")
parser.add_argument("-b", action="store_true", help="Number the non-blank output lines, starting at 1.")
parser.add_argument("-s", action="store_true", help="Squeeze multiple adjacent empty lines, causing the output to be single spaced.")
p_args = parser.parse_args()


def main(p_args):
    for file in p_args.files:
        f = open(file)
        lineNumber = 1
        previousLine = ''
        for line in f:
            if p_args.b:
                if line != '\n':
                    print("{0:6}  ".format(lineNumber), end="")
                    lineNumber += 1
            elif p_args.n:
                print("{0:6}  ".format(lineNumber), end="")
                lineNumber += 1
            if p_args.s and (previousLine == '\n' and line == '\n'):
                continue
            print(line, end="")
            previousLine = line

main(p_args)
