# use the line that starts with FILE as output file name
# every time a line starts with FILE, it will be a separator line and the line content will be used as a file name.
# if there is a duplicate in file name the content will be appended.
# check filenames.log for any duplicate file names.

import re

with open("filenames.log", 'a') as flog:
   with open("sample.txt") as fin:
      for line in fin:
        if re.match("FILE", line):
           flog.write(line)
           filename = line.rstrip()
        else:
           with open(filename + '.txt', 'a') as fout:
              fout.write(line)
