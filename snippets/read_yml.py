import sys
import yaml

def read_yml(file_name):
    with open(file_name, 'r') as f:
        dataset = yaml.load(f)
        return dataset

data = read_yml(sys.argv[1])

print "yml: %s" % data
