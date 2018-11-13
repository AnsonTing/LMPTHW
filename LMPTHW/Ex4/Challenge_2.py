import argparse

parser = argparse.ArgumentParser(description="process arguments")
parser.add_argument("-e", "--eat", help="eat a lot")
parser.add_argument("-d", "--drink", help="drink a lot")
parser.add_argument("-p", "--play", help="play a lot")
args = parser.parse_args()

if args.eat:
    print "I eat a lot"
if args.drink:
    print "I drink a lot"
if args.play:
    print "I play a lot"
