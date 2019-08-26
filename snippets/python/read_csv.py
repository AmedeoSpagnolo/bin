import sys
import csv

def read_csv(file_name):
    with open(file_name, "r") as f:
        reader = csv.DictReader(f)
        fields = [name.strip() for name in reader.fieldnames]
        dataset = list(reader)
        return dataset, fields

data, fields = read_csv(sys.argv[1])

print "fields: %s" % fields
print "data[0]: %s" % data[0]
