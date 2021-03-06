import collections
import math
import os
import re

#src_folder = "../input"
src_folder = "../temp"
dst_folder = "../temp/pp"

link_regex = re.compile(r"file:///C:\\work\\Temp\\HM\\HTML\\([a-z_\-]+)\.htm", re.IGNORECASE)
img_regex = re.compile(r"\(([a-z0-9_\-]+)/media/image([0-9]+\.[a-z]+)", re.IGNORECASE)
size_regex = re.compile(r"{width=\"[0-9\.]+in\" height=\"[0-9\.]+in\"}", re.IGNORECASE)

size1_regex = re.compile(r"{width=\"[0-9\.]+in\"", re.IGNORECASE)
size2_regex = re.compile(r"height=\"[0-9\.]+in\"}", re.IGNORECASE)

def main():
    file_name = "analog_recording.md"
    #process(file_name)
    process_all()

def process_all():
    files = os.listdir(src_folder)
    for f in files:
        if f.endswith(".md"):
            process(f)

def process(file_name):
    print(file_name)
    with open(dst_folder +"/" + file_name, "w+", encoding='utf-8') as output:
        with open(src_folder + "/" + file_name, encoding='utf-8') as input:
            count = 0
            for line in input:
                if line == "\n":
                     output.write(line)
                     count += 1
                     continue
                l = line.lstrip()
                if l.startswith("---") is False:
                    if count == 0:
                        ind = l.find("**   [Top]")
                        if ind > 0:
                            l = l[:ind] + "\n\n"
                        l = l.replace("**", "# ")
                    if l.startswith("[Top](file") or l.startswith("[Previous](file") or l.startswith("[Next](file"):
                        continue
                    l = link_regex.sub("../\\1/", l)
                    l = img_regex.sub("(./img/\\1\\2", l)
                    l = size_regex.sub("\n", l)
                    l = size1_regex.sub("\n", l)
                    l = size2_regex.sub("\n", l)
                    output.write(l)
                    count += 1

main()