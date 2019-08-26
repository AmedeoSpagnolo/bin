import sys
import json

def read_json(file_name):
    with open(file_name, "r") as f:
        dataset = json.load(f)
        fields = dataset[0].keys()
        return dataset, fields

data, fields = read_json(sys.argv[1])

print "fields: %s" % fields
print "data[0]: %s" % data[0]
