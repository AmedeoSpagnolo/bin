import json

dataset = [
    {"f1": "1", "f2": "2", "f3": "3", "f4": "4"},
    {"f1": "5", "f2": "6", "f3": "7", "f4": "8"}]
fields = dataset[0].keys()

def export_csv (file_name, _dataset, _fields):
    with open(file_name, 'w') as f:
        f.write(",".join(['"'+str(x)+'"' for x in _fields]) + "\n")
        for i in _dataset:
            line = []
            for j in _fields:
                line.append(i[j])
            f.write(",".join(['"'+str(y)+'"' for y in line]) + "\n")

export_csv("outfile.json", dataset, fields)
