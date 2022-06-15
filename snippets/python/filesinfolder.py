import glob

def fileinfolder(path):
    return glob.glob(path)

temp = fileinfolder("./*")


print(temp)
