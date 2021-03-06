#!/usr/bin/python
import argparse
import os
from nltk import *
from nltk.corpus import stopwords
from termcolor import colored
import re

import sys
reload(sys)
sys.setdefaultencoding('utf8')

class CustomFormatter(argparse.ArgumentDefaultsHelpFormatter, argparse.RawDescriptionHelpFormatter):
    pass

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
        text infile.txt --count word1 word2
        text infile.txt --diversity
        text infile.txt --common 4
        text infile.txt --common 10 --plot
        text infile.txt --contains word
        text infile.txt --find word1 word2
        text infile.txt --similar word
        text comments.txt battery.txt --find_line battery --save
        """,
            formatter_class=CustomFormatter)
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
            '-s',
            '--sort',
            help="with --show sort words",
            action="store_true",
            default=False)
        parser.add_argument(
            '-p',
            '--show',
            help="print words",
            action="store_true",
            default=False)
        parser.add_argument(
            '-u',
            '--unique',
            help="with --show print unique",
            action="store_true",
            default=False)
        parser.add_argument(
            '-d',
            '--diversity',
            help="calculate lexical diversity",
            action="store_true",
            default=False)
        parser.add_argument(
            '--count',
            nargs="+",
            help="count words")
        parser.add_argument(
            '--find',
            nargs="+",
            help="count words")
        parser.add_argument(
            '--find_line',
            nargs="+",
            help="count words")
        parser.add_argument(
            '--context',
            nargs="+",
            help="count words")
        parser.add_argument(
            '--dispersion',
            nargs="+",
            help="show dispersion plot")
        parser.add_argument(
            '-c',
            '--common',
            nargs=1,
            help="show common words")
        parser.add_argument(
            '--similar',
            help="show similar words")
        parser.add_argument(
            '--plot',
            action="store_true",
            default=False)
        parser.add_argument(
            '--long',
            action="store_true",
            default=False)
        parser.add_argument(
            '--save',
            action="store_true",
            default=False)
        parser.add_argument(
            '--wordlist',
            action="store_true",
            default=False)
        parser.add_argument(
            '--contains',
            nargs=1,
            help="show word that contains input")
        parser.add_argument(
            'infile',
            nargs=1)
        parser.add_argument(
            'outfile',
            nargs="?")

        self.args = parser.parse_args()
        self.filename, self.ext = os.path.splitext(self.args.infile[0])
        self.data, self.text, self.token, self.lines, self.tags = self.infile_convert(self.args.infile[0])
        self.outfile = self.args.outfile if self.args.outfile else str(self.filename) + "_converted" + str(self.ext)

        # some fancy code here
        print self.data
        if self.args.lenght:
            print "len: %s" % len(self.data)

        if self.args.unique:
            self.data = set(self.data)

        if self.args.sort:
            self.data = sorted(self.data)

        if self.args.count:
            for i in self.args.count:
                print "%s: %s" % (i, self.data.count(i))

        if self.args.diversity:
            if len(self.data) != 0:
                print float(len(set(self.data))) / float(len(self.data))

        if self.args.common:
            fdist1 = FreqDist(self.data)
            i = int(self.args.common[0])
            count = i if i > 0 else len(self.data) - 1
            if self.args.plot:
                fdist1.plot(count)
            else:
                for i in fdist1.most_common(count):
                    print "%s: %s" % (i[0], i[1])

        if self.args.long:
            long_words = [w for w in self.data if len(w) > 10]
            for i in sorted(set(long_words)):
                print i

        if self.args.find:
            for i in self.args.find:
                self.token.concordance(i)

        if self.args.contains:
            for i in [x for x in set(self.data) if self.args.contains[0].upper() in x.upper()]:
                print self.colour(i,self.args.contains[0])

        if self.args.similar:
            self.token.similar(self.args.similar)

        if self.args.dispersion:
            self.token.dispersion_plot(self.args.dispersion)

        if self.args.find_line:
            temp = []
            for i in self.args.find_line:
                for j in self.lines:
                    if i in j:
                        temp.append(j)
                        print self.colour(j,i)
            self.text = "\n".join(temp)

        if self.args.context:
            self.token.common_contexts(self.args.context)

        if self.args.show:
            print self.data

        if self.args.save:
            self.export_txt()

        if self.args.wordlist:
            self.export_wordlist()

    def infile_convert (self, file_name):
        text = ""
        tag = []
        # stop = set(stopwords.words('english'))
        try:
            with open (self.args.infile[0], "r") as myfile:
                text = myfile.read()
                lines = [x.strip() for x in text.splitlines()]
        except:
            pass
        data = [w for w in word_tokenize(text) if w.lower() not in stopwords.words('english')]
        token = Text(tokenize.WhitespaceTokenizer().tokenize(text))
        tags = "pos_tag(data)"
        return data, text, token, lines, tags

    def export_txt (self):
        with open(self.outfile, 'w') as f:
            f.write(self.text)
            print "new file: " + str(self.outfile) + " saved!"

    def export_wordlist (self):
        with open(self.outfile, 'w') as f:
            for i in self.data:
                f.write(i+"\n")
            print "new file: " + str(self.outfile) + " saved!"

    def colour (self, text, highlight, color = "red"):
        return colored(highlight, color).join(re.split(highlight,text,flags=re.IGNORECASE))


# text from html
