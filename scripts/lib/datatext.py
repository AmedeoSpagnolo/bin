#!/usr/bin/python
import argparse
import os
import nltk

class DataText:
    def __init__(self):
        parser = argparse.ArgumentParser(
            add_help=True,
            description="Do crazy stuff with txt files",
            epilog="""examples:
    # title
        text infile.txt -v
        text infile.txt -l
        text infile.txt --show
        text infile.txt --show --sort
        text infile.txt --show --sort --unique
        """)
        parser.add_argument(
            '-v',
            '--version',
            action='version',
            version='%(prog)s 1.0')
        parser.add_argument(
            '-l',
            '--lenght',
            help="print number of words",
            action="store_true",
            default=False)
        parser.add_argument(
            '--sort',
            help="print number of words",
            action="store_true",
            default=False)
        parser.add_argument(
            '--show',
            help="print words",
            action="store_true",
            default=False)
        parser.add_argument(
            '--unique',
            help="print words",
            action="store_true",
            default=False)
        parser.add_argument(
            '--count',
            nargs="+",
            help="count words")
        parser.add_argument(
            'infile',
            nargs=1)

        self.args = parser.parse_args()
        self.filename, self.ext = os.path.splitext(self.args.infile[0])
        self.data = self.infile_convert(self.args.infile[0])

        # some fancy code here

        if self.args.lenght:
            print "len: %s" % len(self.data)

        if self.args.unique:
            self.data = set(self.data)

        if self.args.sort:
            self.data = sorted(self.data)

        if self.args.count:
            for i in self.args.count:
                print "%s: %s" % (i, self.data.count(i))

        if self.args.show:
            print self.data

    def infile_convert (self, file_name):
        text = "Lorem"
        try:
            with open (self.args.infile[0], "r") as myfile:
                text = myfile.read()
        except:
            pass
        return text.split()
