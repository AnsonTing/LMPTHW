import argparse
import sys

parser = argparse.ArgumentParser(description='concatenate and print files')
parser.add_argument("files", nargs="*")
parser.add_argument("-n", action="store_true", help="Number the output lines, starting at 1.")
parser.add_argument("-b", action="store_true", help="Number the non-blank output lines, starting at 1.")
parser.add_argument("-s", action="store_true", help="Squeeze multiple adjacent empty lines, causing the output to be single spaced.")
p_args = parser.parse_args()
N_OPTION = p_args.n
B_OPTION = p_args.b
S_OPTION = p_args.s

def removeAdjEmptyLines(lines):
    i = 0
    while i < len(lines):
        if lines[i] == '\n':
            while i + 1 < len(lines) and lines[i+1] == '\n':
                lines = lines[:i+1] + lines[i+2:]
        i += 1
    return lines


for file in p_args.files:
    f = open(file, "r")
    if S_OPTION:
        f = removeAdjEmptyLines(list(f))
    if B_OPTION:
        line_number = 1
        for line in f:
            if line != '\n':
                print '      {}  '.format(line_number) + line.rstrip('\n')
                line_number += 1
            else:
                print ''
    elif N_OPTION:
        line_number = 1
        for line in f:
            print '      {}  '.format(line_number) + line.rstrip('\n')
            line_number += 1
    else:
        for line in f:
            print line.rstrip('\n')


# args = sys.argv[1:]
#
# B = False
#
# if p_args.b:
#     B = True
#     print 'b!!!'
#     while '-b' in args:
#         args.remove('-b')
#
# if '>' in args:
#     try:
#         write_file = args[args.index('>') + 1]
#     except IndexError:
#         raise SyntaxError
#     args.remove('>')
#     args.remove(write_file)
#     lines = []
#     for file in args:
#         f = open(file, "r")
#         for line in f:
#             lines.append(line.rstrip('\n'))
#     wf = open(write_file, "rw+")
#     wf.truncate()
#     for line in lines:
#         wf.write(line)
#
#
# else:
#     for file in args:
#         f = open(file, "r")
#         for line in f:
#             print line.rstrip('\n')
