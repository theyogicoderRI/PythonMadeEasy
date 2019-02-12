import datetime
import os
import time
# from os.path import getsize, join
# from shutil import get_terminal_size

dir_1 = "/Users/my_tests/"
my_dir = "/Users/my_tests/testing1"
my_dir2 = "Users/my_tests/testing1"
my_dir3 = "Users/my_tests/testing1/testing2"
my_file = "/Users/my_tests/testing1/testing2/my_file2.txt"
my_file3 = "/Users/my_tests/testing1/testing2/my_file2.txt"
my_file2 = "Users/my_tests/testing1/testing2/my_file2.txt"
fake_file = "/Users/my_tests/testing1/testing2/my_file42.txt"
up_path = "/ONE/TWO/THREE/FOUR"

#name of OS
print()
print("Name of my operating System is: ", os.name)
print()
print("My Home dir: ", os.environ['HOME'])
print()
print("Get current dir: ", os.getcwd())
print()
print("Get user group: ", os.getgid())
print()
print("Who is logged-in?: ", os.getlogin())
print()
print("Terminal size: ", os.get_terminal_size())
print()
#test file access
if os.access("my_file.txt", os.R_OK):
    print("You have access")
else:
    print("no access")

print()
#print out objects (directories and files) in a location
data = (os.path.join(my_dir, fn) for fn in os.listdir(my_dir))
for d in data:
    print("my dirs: ", d)
print()    

x = os.listdir(my_dir)
print("PRINTING X ", x)

make a new directory
try:
    os.mkdir("new_dir")
except:
    print("This dir already exists, moving on")    

# print()
# objects = (fn for fn in sorted(os.listdir(dir_1), reverse = True)) #generator expression
# print()
# print("New object listing: ", list(objects))
# print()
object_info = os.stat(dir_1)
print("Size is:", object_info.st_size)
print()
print("Birthtime is:", time.ctime(object_info.st_birthtime))
print()
print("Device is:", object_info.st_dev)
print()
print()

print("Absolute: ", os.path.abspath(my_dir))
print("Basename:'", os.path.basename(my_dir))
print("Split: ", os.path.split(my_dir))
print("Split File: ", os.path.split(my_file))
print("Dirname Dir: ", os.path.dirname(my_dir))
print("Dirname File: ", os.path.dirname(my_file))
print("Exists Dir: ", os.path.exists(my_dir))
print("Exists file: ", os.path.exists(my_file)) 
# use utcfromtimestamp to convert from seconds to datetime - last access
print("Last access time File: ", datetime.datetime.utcfromtimestamp(os.path.getatime(my_file)))

# last modification
print("Last mod time File: ", datetime.datetime.utcfromtimestamp(os.path.getmtime(my_file)))
print("Get Size Dir:", os.path.getsize(my_dir)) #does not get content within
print("Get Size File:", os.path.getsize(my_file)) # works for file
print("Is abs:", os.path.isabs(my_dir)) #needs to start with "/" to be abs
print("Is abs:", os.path.isabs(my_dir2)) #false no'/'
print("Is file?: ", os.path.isfile(my_file)) #true
print("Is file2?: ", os.path.isfile(my_file2)) #false needs "/'"
print("Is file?: ", os.path.isfile(fake_file)) # false
# print("Is dir?: ", os.path.isdir(my_file)) # false 




print("Is dir?: ", os.path.isdir(my_dir)) # true starts with "/"
print("Is dir?: ", os.path.isdir(my_dir2)) #false no'/'
#joins
my_paths = "/"
my_paths2 = ["foo", "bar", "who", "ha"]
for x in my_paths2:
    print("I Join: ", os.path.join(my_paths, x))
print("Are we the same?: ", os.path.samefile(my_file,my_file3))
file22 = "/hello/hiya/foo.txt"
#Split the pathname path into a pair (root, ext) such that root + ext == path
print("Splitme: ", os.path.splitext(file22))
print(os.getcwd())
os.chdir("new_dir")
print(os.getcwd())
