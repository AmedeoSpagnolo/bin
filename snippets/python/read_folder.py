import os
import sys

# DEFAULT:
#   folder = current working directory
#   (if other directories are not specified)

folder = os.getcwd()

try:
    folder = sys.argv[1]
except:
    pass

files = os.listdir(folder)

print files
