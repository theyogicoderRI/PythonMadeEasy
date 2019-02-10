import datetime
import os
import time
from os.path import getsize, join





my_dir = "/Users/my_tests/"
# intro to os.walk
print("************Start print********")
for root_dir_path, sub_dirs, files in os.walk(my_dir):
    print("Root Directory Path: ", root_dir_path)
    print("Sub Directories: ", sub_dirs)
    print("Files", files)
    print('*' * 25)
print("************End print********")

#print only the files
for dir, sub, files in os.walk(my_dir):
    print("Print Dir: ", dir) # prints out each directory path
    sub = [n for n in sub] # prints each sub folder in each dir
    contents = sub + files # subs and files
    contents.sort() # sorst subs and files
    
    for f in contents:
        if os.path.isfile(f):
            print('\tJust The Files', f)       
    print()    # prints spaces between levels 

#print only the subs
for dir, sub, files in os.walk(my_dir):
    print("Print Dir: ", dir) # prints out each directory path
    sub = [n for n in sub] # prints each sub folder in each dir
    sub.sort() # sort subs
    
    for f in sub:
        print('\tJust The Subs', f)       
    print()    # prints spaces between levels       


#Count number of files in dirs and sub dirs
count_file = 0
dir1 = "/Users/test"

for path, sub, filenames in os.walk(dir1):
    sub = [n for n in sub]
    content = sub + filenames
    for f in content:
        count_file += 1
        print("Count:{} File Name: {}".format(count_file, f))
      
# print("Final count is: ", count_file)


#print paths that dont startwith "--" 
for path, sub_dirs, files in os.walk(my_dir):
    if not path.endswith("__"):
        print("Print Path: ", path)


#print all directories except those that start with "number ." -" (i.e '1.')
for root, dirs, files in os.walk(dir1, topdown=True):
    for dir in dirs:
        if not dir[1] == '.':
            print(dir)

#using os.walk to rename directory
#os.sep is The character used by the operating system to separate pathname components-
#This is '/' for POSIX and '\\' for Windows

for root, dirs, files in os.walk(dir1):
    for d in dirs:
        
        if d.endswith(".test"):
            print(d)
            # must give full path for rename
            os.rename((root + os.sep + d), (root + os.sep + d+"."+"new"))
            

#using os.walk to replace directory name
for root, dirs, files in os.walk(dir1):
    for d in dirs:
        
        if d.endswith(".test"):
            # must give full path for replace
            os.replace((root + os.sep + d), ((root + os.sep + "new"+d[:-5])))            
            
            
print()
#print out files except python files and and
#present their full path
for path, sub_dirs, files in os.walk(my_dir):
    for file in files:
        if not file.endswith(".py") and not file.startswith('.'): 
            file_path = os.path.join(path, file) 
            print("Print files: ", file_path)  

print()
# get size of each file and last modification date
for path, sub_dirs, files in os.walk(my_dir):
    for file in files:
        if not file.endswith(".py") and not file.startswith('.') and not file.endswith(".pyc"): 
            file_path = os.path.join(path, file) 
            file_size = getsize(file_path)
            info = os.stat(file_path) 
            print("File Path: {0:<65} File Size: {1:<10} Last Modified: {2} ".format( file_path, file_size, time.ctime(info.st_mtime)))



   

# get total directory size
my_dir = "/Users/my_tests/"
def get_size(dir):
    size = 0
    for path, sub, filenames in os.walk(dir):
        for f in filenames:
            file_path = os.path.join(path, f)
            size += os.path.getsize(file_path)
    return size
  
dir_size = get_size(my_dir)
print("Total Dir Size:", dir_size)


# function to convert to megabytes for better reading
def con_mb(value):
    '''to convert to magabytes'''
    mb = 1048576
    return round(value/mb, 2)

# #get total directory size in megabytes
my_dir = "/Users/my_tests/"
def get_size(dir):
    size = 0
    for path, sub, filenames in os.walk(dir):
        for f in filenames:
            file_path = os.path.join(path, f)
            size += os.path.getsize(file_path)
            con_size = con_mb(size)
    return con_size
  
dir_size = get_size(my_dir)
print("Total Dir Size MB: ",dir_size)


# get size of directories and individual files within in Bytes
print("************Start print********")
for root_dir_path, sub_dirs, files in os.walk(my_dir, topdown=True):
      #dont want dunders, so we bypass them with this next line
    if root_dir_path.endswith("__"):
        continue
    else:
        size = sum(getsize(join(root_dir_path, name)) for name in files)
        print("Root Directory--"+root_dir_path+"--Directory Size: ",size)
        for f in files: # files need to be in string form for join- wont take list
            fp = os.path.join(root_dir_path, f) 
            print("\tFile: {0:62} -- Size:{1:5} Bytes".format(fp, getsize(fp)))

# print("************End print********")

#sort by reverse order file size recursively through directory structure based on conditions
my_dir2 = "/Users/claudiaacerra/Documents/Yogi-Coder/Classes/Python/For GitHubUpload"
list1 = []
print("************Start print********")
for root_dir_path, sub_dirs, files in os.walk(my_dir2, topdown=True):
    for f in files: # files need to be in string form for join- wont take list
        if not f.endswith("__") and not f.startswith("."):
            fp = os.path.join(root_dir_path, f) 
            mb = 1048576  # to covert to megabytes
            size = os.path.getsize(fp)
            con_size = con_mb(size)
            if fp not in list1 and con_size > 3:
                list1.append((fp, con_size))
list1.sort(key=lambda s: s[1], reverse=True)
for l in list1:
    print("File Name: ", l[0],"File Size: " , str(l[1])+'MB')
print("************End print********")
