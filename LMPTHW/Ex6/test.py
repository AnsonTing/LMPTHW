import sys

name = raw_input()
if len(name) < 3:
    print >> sys.stderr, "Name is too short"
else:
    print "Hello %s" % name
