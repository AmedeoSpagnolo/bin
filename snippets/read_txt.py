import sys

def read_text(file_name):
    with open(file_name, "r") as f:
        return f.read()

text = read_text(sys.argv[1])

print "text: %s" % text[0]
