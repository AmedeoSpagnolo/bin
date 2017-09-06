import sys

name = sys.argv[1]
colors = [
    "rgb(254,186,53)",
    "rgb(244,121,32)",
    "rgb(223,22,43)",
    "rgb(166,34,142)",
    "rgb(121,33,131)",
    "rgb(126,130,133)"
]

docHeight = 700
space = 150

svg = ('<?xml version="1.0" encoding="iso-8859-1"?>\n'
    '<!DOCTYPE svg PUBLIC "-//W3C//DTD SVG 1.1//EN" "http://www.w3.org/Graphics/SVG/1.1/DTD/svg11.dtd">\n'
    '<svg version="1.1" id="Layer_1" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" x="0px" y="0px"\n'
    'viewBox="0 0 {{width}} {{height}}" style="enable-background:new 0 0 {{width}} {{height}};" xml:space="preserve">{{content}}\n'
    '</svg>\n')

rect = '<rect style="fill:{{fill}};" x="{{x}}" width="{{width}}" height="{{height}}"/>\n'

def string_to_ascii(mystr):
    return [ord(x) for x in mystr]

def encrypt(arr):
    # get an array of decimals (ascii converted)
    # and return a converted array
    return [{"width": a/3 * a/3 / 3, "color": colors[a%6]} for a in arr]

def generateSvg(arr):
    lenshift = [a["width"] for a in arr]
    shift = [lenshift[:a[0]] for a in enumerate(arr)]
    _shift = [sum(a) + len(a) * space for a in shift]
    content = [rect
        .replace("{{x}}", str(_shift[a[0]]))
        .replace("{{fill}}", a[1]["color"])
        .replace("{{width}}", str(a[1]["width"]))
        .replace("{{height}}", str(docHeight)) for a in enumerate(arr)]
    # print [x for x in enumerate(content)]
    mywidth = sum([a["width"] + space for a in enc]) - space
    mySvg = svg.replace("{{content}}", ''.join(content)).replace("{{height}}", str(docHeight)).replace("{{width}}", str(mywidth))

    return mySvg

def write_new_file(file_name, content):
    with open(file_name, "w+") as out:
        out.write(content)

dec = string_to_ascii(name)
enc = encrypt(dec)
content = generateSvg(enc)

write_new_file("file.svg", content)
