import sys

content = "new line"

def write_new_line(file_name, content):
    with open(file_name, "a") as out:
        out.write("\n")
        out.write(content)

write_new_line("out.txt", content)
