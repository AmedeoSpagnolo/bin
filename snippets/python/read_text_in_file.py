import glob
import sys
import re
import json

def fileinfolder(path):
    return glob.glob(path)

def read_text(file_name):
    with open(file_name, "r") as f:
        return f.read()

print(read_text("./filename.txt"))
