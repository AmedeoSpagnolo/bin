#!/usr/bin/python
import argparse
import json
import csv
from collections import Counter

class CustomFormatter(argparse.ArgumentDefaultsHelpFormatter, argparse.RawDescriptionHelpFormatter):
    pass

class DataViz:
    def __init__(self, dataset_format = ""):
        parser = argparse.ArgumentParser(
            add_help=True,
            description="Do crazy stuff with csv files",
            epilog="""examples:
    # export json
        {dataset_format} infile.{dataset_format} --json
        {dataset_format} infile.{dataset_format} --json -ugly
    # general
        {dataset_format} infile.{dataset_format} -i # print general info
        {dataset_format} infile.{dataset_format} -l # print lines number
    # export
        {dataset_format} infile.{dataset_format} --csv
        {dataset_format} infile.{dataset_format} --csv --filter field1 field2 field3
        {dataset_format} infile.{dataset_format} --csv --filter field1 field2 field3 --add newfield
        {dataset_format} infile.{dataset_format} --json
        {dataset_format} infile.{dataset_format} --json --filter field1 field2 field3
        {dataset_format} infile.{dataset_format} --json --filter field1 field2 field3 --add newfield
    # info column
        {dataset_format} infile.{dataset_format} -c field -o # get info from field with occurrence
        {dataset_format} infile.{dataset_format} + -c field -a # get info from field with average
        {dataset_format} infile.{dataset_format} -c field -oa # get info from field with occurrence and average""".replace("{dataset_format}",dataset_format),
            formatter_class=CustomFormatter)
        parser.add_argument(
            '-v',
            '--version',
            action='version',
            version='%(prog)s 1.0')
        parser.add_argument(
            'infile',
            nargs=1)
        parser.add_argument(
            '-l',
            '--lines',
            help="print number of lines",
            action="store_true",
            default=False)
        parser.add_argument(
            '-i',
            '--info',
            help="print general info",
            action="store_true",
            default=False)
        parser.add_argument(
            '-f',
            '--fields',
            help="print list of fields",
            action="store_true",
            default=False)
        parser.add_argument(
            '-o',
            '--occurrence',
            help="with -c get occurrence",
            action="store_true",
            default=False)
        parser.add_argument(
            '-a',
            '--average',
            help="with -c get average",
            action="store_true",
            default=False)
        parser.add_argument(
            '--json',
            help="export pretty json",
            action="store_true",
            default=False)
        parser.add_argument(
            '--csv',
            help="export pretty json",
            action="store_true",
            default=False)
        parser.add_argument(
            '--only',
            help="with --csv or --json export only given fields",
            nargs="+",
            default=False,
            required=False)
        parser.add_argument(
            '--add',
            help="with --csv or --json export add fields",
            nargs="+",
            default=False,
            required=False)
        parser.add_argument(
            '--remove',
            help="with --csv or --json export without given fields",
            nargs="+",
            default=False,
            required=False)
        parser.add_argument(
            '--ugly',
            help="with --json export without beautify",
            action="store_false",
            default=True)
        parser.add_argument(
            '-C',
            '--column',
            nargs="+",
            help="print all lines of given field")
        parser.add_argument(
            '-c',
            '--columninfo',
            nargs="+",
            help="print informations given field")

        self.args = parser.parse_args()
        self.data, self.fields = self.infile_convert(self.args.infile[0], dataset_format)

        # some fancy code here

        if self.args.lines:
            print "lines: %s" % len(self.data)

        if self.args.fields:
            print "fields: %s" % json.dumps(self.fields)
            print "fields lenght: %s" % len(self.fields)

        if self.args.info:
            print "first element: %s" % json.dumps(self.data[0])
            print "fields: %s" % json.dumps(self.fields)
            print "lines: %s" % len(self.data)

        if self.args.columninfo:
            for col in self.args.columninfo:
                empty,populated,total,count,average = self.get_column_info(col)
                print "%s:" % col
                print "    total: %s" % total
                print "    empty: %s" % empty
                print "    populated: %s" % populated
                if self.args.average:
                    print "    sum: %s" % count
                    print "    average: %s" % average
                if self.args.occurrence:
                    temp = Counter(self.get_array_from_field(col))
                    print "    occurrence:"
                    for attr, value in temp.iteritems():
                        print "        '%s'  -  %s" % (attr, value)

        if self.args.column:
            print ",".join(self.args.column)
            for i in self.data:
                print ",".join(list(map(lambda x: i[x], self.args.column)))

        if self.args.add:
            self.add_field()

        if self.args.remove:
            self.remove_field()

        if self.args.only:
            self.only_field()

        if self.args.json:
            self.export_json()

        if self.args.csv:
            self.export_csv()


    def add_field (self):
        self.fields += self.args.add
        for i in self.data:
            for att in self.args.add:
                i[att] = ""

    def remove_field (self):
        for att in self.args.remove:
            self.fields.remove(att)
            for i in self.data:
                del i[att]

    def only_field (self):
        self.fields = [x for x in self.fields if x in self.args.only]
        for i,s in enumerate(self.data):
            el = {}
            for key in s:
                if key in self.args.only:
                    el[key] = s[key]
            self.data[i] = el

    def get_column_info (self,field):
        empty = 0
        count = 0
        for i in self.data:
            if i[field] ==  "":
                empty += 1
            else:
                try:
                    count += float(i[field])
                except:
                    pass
        valid = len(self.data)-empty
        if valid != 0:
            average = count/valid
        return empty,valid,len(self.data),count,count/valid

    def get_array_from_field (self, field):
        arr = []
        for i in self.data:
            arr.append(i[field])
        return arr

    def export_csv (self):
        name = self.args.infile[0].split(".")[0]
        with open(str(name) + '_converted.csv', 'w') as f:
            f.write(",".join(self.fields) + "\n")
            for i in self.data:
                line = []
                for j in self.fields:
                    line.append(i[j])
                f.write(",".join(line) + "\n")
            print "new file: " + str(name) + "_converted.csv saved!"

    def export_json (self):
        name = self.args.infile[0].split(".")[0]
        if self.args.ugly:
            with open(str(name) + '_ugly_converted.json', 'w') as f:
                json.dump(self.data, f)
                print "new file: " + str(name) + "_ugly_converted.json saved!"
        else:
            with open(str(name) + '_converted.json', 'w') as f:
                json.dump(self.data, f, sort_keys=True, indent=4)
                print "new file: " + str(name) + "_converted.json saved!"

    def infile_convert (self, file_name, ext):
        with open(file_name, "r") as f:
            if (ext == "csv"):
                reader = csv.DictReader(f)
                _fields = [name.strip() for name in reader.fieldnames]
                _data = list(reader)
                return _data, _fields
            elif (ext == "json"):
                _data = json.load(f)
                _fields = _data[0].keys()
                return _data, _fields
            else:
                print "ERROR: invalid format - '" + str(ext) + "'"
                quit()
