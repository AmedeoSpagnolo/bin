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
            '--filter',
            '--filters',
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
            '--ugly',
            help="with --json export without beautify",
            action="store_false",
            default=True)
        parser.add_argument(
            '-C',
            '--column',
            help="print all lines of given field")
        parser.add_argument(
            '-c',
            '--columninfo',
            help="print informations given field")

        args = parser.parse_args()

        self.data, self.fields = self.infile_convert(args.infile[0], dataset_format)

        if args.lines:
            print self.lines()

        if args.fields:
            print "fields: " + str(json.dumps(self.fields))

        if args.column:
            print self.column(args.column)

        if args.json:
            self.export_json(args.infile[0], args.ugly, args.filter, args.add)

        if args.info:
            print "first element: " + str(json.dumps(self.data[0]))
            print "fields: " + str(json.dumps(self.fields))
            print "lines: " + str(len(json.dumps(self.data)))

        if args.columninfo:
            self.print_column_info(args.columninfo, args.occurrence, args.average)

        if args.csv:
            self.export_csv(args.infile[0], args.filter, args.add)

    def print_column_info (self, field, occurrence, average):
        empty = 0
        for i in self.data:
            if i[field] ==  "":
                empty += 1
        populated = len(self.data) - empty
        print str(field) + ":"
        print "    total: " + str(len(self.data))
        print "    empty: " + str(empty)
        print "    populated: " + str(populated)
        if average:
            _average = self.get_average(field, populated)
            print "    average: " + _average
        if occurrence:
            self.print_occurrence_of_field(field)

    def get_array_from_field (self, field):
        arr = []
        for i in self.data:
            arr.append(i[field])
        return arr

    def print_occurrence_of_field (self, field):
        arr = self.get_array_from_field(field)
        temp = Counter(arr)
        print "    occurrence:"
        for attr, value in temp.iteritems():
            print "        " + str(attr) + " - " + str(value)

    def get_average (self, field, total):
        count = 0
        for i in self.data:
            try:
                count += float(i[field])
            except:
                pass
        return str(count / total)

    def export_csv (self, _infile, _filters=None, _add=[]):
        name = _infile.split(".")[0]
        _filters = self.fields if _filters < 1 else _filters
        _add = _add if _add else []
        with open(str(name) + '_converted.csv', 'w') as f:
            f.write(",".join(_filters+_add) + "\n")
            for i in self.data:
                line = []
                for j in _filters:
                    try:
                        line.append(i[j])
                    except:
                        line.append("")
                for r in _add:
                    line.append("")
                f.write(",".join(line) + "\n")
            print "new file: " + str(name) + "_converted.csv saved!"


    def filter_json_obj (self,dataset,filters,add):
        temp = []
        for i in dataset:
            _obj = {}
            for y in add:
                _obj[y] = ""
            for j in filters:
                _obj[j] = i[j]
            temp.append(_obj)
        return temp

    def export_json (self, _infile, beauty=False, _filters=None, _add=[]):
        _filters = self.fields if _filters < 1 else _filters
        _add = _add if _add else []
        name = _infile.split(".")[0]
        if beauty:
            with open(str(name) + '_converted.json', 'w') as f:
                json.dump(self.filter_json_obj(self.data,_filters,_add), f, sort_keys=True, indent=4)
                print "new file: " + str(name) + "_converted.json saved!"
        else:
            with open(str(name) + '_ugly_converted.json', 'w') as f:
                json.dump(self.filter_json_obj(self.data,_filters,_add), f)
                print "new file: " + str(name) + "_ugly_converted.json saved!"

    def infile_convert (self, file_name, ext):
        if (ext == "csv"):
            with open(file_name, "r") as f:
                reader = csv.DictReader(f)
                _fields = [name.strip() for name in reader.fieldnames]
                _data = list(reader)
                return _data, _fields
        elif (ext == "json"):
            with open(file_name) as f:
                _data = json.load(f)
                _fields = _data[0].keys()
                return _data, _fields
        else:
            print "ERROR: invalid format"

    def lines (self):
        return "lines: " + str(len(self.data))

    def column (self, field):
        for i in self.data:
            print i[field]



# name or flags - Either a name or a list of option strings, e.g. foo or -f, --foo.
# action - The basic type of action to be taken when this argument is encountered at the command line.
# nargs - The number of command-line arguments that should be consumed.
# const - A constant value required by some action and nargs selections.
# default - The value produced if the argument is absent from the command line.
# type - The type to which the command-line argument should be converted.
# choices - A container of the allowable values for the argument.
# required - Whether or not the command-line option may be omitted (optionals only).
# help - A brief description of what the argument does.
# metavar - A name for the argument in usage messages.
# dest - The name of the attribute to be added to the object returned by parse_args().
