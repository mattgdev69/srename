# Strips all chars out of a file name for a TV series and leaves series info
# Does this for all files in a directory

import os
import re
import sys
import pathlib
import string

if len(sys.argv) > 1:
    folder = pathlib.Path(sys.argv[1])
    print(folder)
else:
    folder = os.getcwd()

filenames = os.listdir(folder)
for filename in filenames:

    # Break out file name from extension
    fname = pathlib.Path(filename).stem.upper()
    ext = pathlib.Path(filename).suffix.upper()

    match = re.search(r'S..E..', fname)
    if match:
        os.rename(filename, match.group()+ext)
