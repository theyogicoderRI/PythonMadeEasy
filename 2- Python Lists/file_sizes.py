import os
import os.path
import sys
from hurry.filesize import size # had to import this from hurry.filesize 0.9-Python library for human readable file sizes 
from hurry.filesize import alternative # this is from that same package but it allows the size print out to look nicer

def file_size(directory):
    '''
    This function will enable you to list the names of files/directories and get the size
    of files in a path you specify at the command line
    
    To run this code, go to the command line and run the following:
    $ python3 file_sizes.py "<add your directory path here>"
    '''
    basedir = directory
    names = os.listdir(basedir)
    paths = [os.path.join(basedir, name) for name in names]
    sizes = [(path, os.stat(path).st_size) for path in paths]
    pairs = []   
    print()
    print("Folder Sizes Print")
    print("=" *80)
    for f, s in sizes:
         pairs.append((f, s))   
    pairs.sort(key=lambda s: s[1])
    count = 0
    for x, y in pairs:
        output = ("File Name: {0:<75} - File size: {1:<10}".format(x,y))
        print(output)
        print("File Size Translate: ", size(y, system=alternative)) # 'size' function if from the hurry.filesize library
        count = count + 1
    print("Total number of records: ", str(count))
# this is the caller of this function. You will supply the path at the command line
file_size(sys.argv[1])
print("Docstring for this function")
print(file_size.__doc__) 


