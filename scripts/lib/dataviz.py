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
            '-c',
            '--column',
            help="print informations given field")
        parser.add_argument(
            '-pc',
            '--printcolumn',
            dest='field',
            help="print all lines of a given field")

        args = parser.parse_args()

        self.data, self.fields = self.infile_convert(args.infile[0], dataset_format)

        if args.lines:
            print self.lines()

        if args.fields:
            print "fields: " + str(self.fields)

        if args.column:
            print self.column(args.column)

    def infile_convert (self, file_name, ext):
        if (ext == "csv"):
            with open(file_name, "r") as f:
                reader = csv.DictReader(f)
                _fields = reader.fieldnames
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
