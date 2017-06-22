#!/usr/bin/python
import argparse
import json
import csv

class DataViz:
    def __init__(self, dataset_format = "", description = "", epilog = ""):
        parser = argparse.ArgumentParser(
            add_help=True,
            description=description,
            epilog=epilog)
        parser.add_argument(
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
            help="export pretty json",
            nargs="+",
            default=False,
            required=False)
        parser.add_argument(
            '-ugly',
            help="export pretty json",
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
            print "fields: " + str(self.fields)

        if args.column:
            print self.column(args.column)

        if args.json:
            self.export_json(args.infile[0], args.ugly, args.filter)

        if args.info:
            print "informations"

        if args.columninfo:
            self.print_column_info(args.columninfo)

        if args.csv:
            self.export_csv(args.infile[0], args.filter)

    def print_column_info (self, field):
        empty = 0
        for i in self.data:
            if i[field] ==  "":
                empty += 1
        print str(field) + ":"
        print "    total: " + str(len(self.data))
        print "    empty: " + str(empty)
        print "    populated: " + str(len(self.data) - empty)

    def export_csv (self, _infile, _filters=None):
        name = _infile.split(".")[0]
        _filters = self.fields if _filters < 1 else _filters
        with open(str(name) + '_converted.csv', 'w') as f:
            f.write(",".join(_filters) + "\n")
            for i in self.data:
                line = []
                for j in _filters:
                    line.append(i[j])
                f.write(",".join(line) + "\n")

    def filter_json_obj (self,dataset, filters):
        print "filters"
        print filters
        if filters:
            temp = []
            for i in dataset:
                _obj = {}
                for j in filters:
                    _obj[j] = i[j]
                # print _obj
                temp.append(_obj)
            return temp
        else:
            return dataset

    def export_json (self, _infile, beauty=False, _filters=None):
        _filters = self.fields if _filters < 1 else _filters
        name = _infile.split(".")[0]
        if beauty:
            with open(str(name) + '_converted.json', 'w') as f:
                json.dump(self.filter_json_obj(self.data,_filters), f, sort_keys=True, indent=4)
                print "new file: " + str(name) + "_converted.json saved!"
        else:
            with open(str(name) + '_ugly_converted.json', 'w') as f:
                json.dump(self.filter_json_obj(self.data,_filters), f)
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
