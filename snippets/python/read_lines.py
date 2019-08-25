import sys
import os

def read_lines(file_name):
    with open(file_name, "r") as f:
        return f.read().splitlines()

lines = read_lines(sys.argv[1])

for line in lines:
    command = "echo ___" + str(line) + "_asd"
    os.system(command)
