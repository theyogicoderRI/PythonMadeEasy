##my_sep = "==>"
##list1 = ["Batman", "Superman", "Wonder Woman", "RBG"]
##print(my_sep.join(list1))
##
### output: Batman==>Superman==>Wonder Woman==>RBG
##
##
##list2 = ["Pizza", "Cheese", "Bread", "Tofu"]
##print(", ".join(list2))
##
### output: Pizza, Cheese, Bread, Tofu
##
##list2 = ["Pizza", "Cheese", "Bread", "Tofu"]
##print("".join(list2))
##
### output: PizzaCheeseBreadTofu
##
##list2 = ["Pizza", "Cheese", "Bread", "Tofu"]
##print("\n".join(list2))
##
##''' output:
##Pizza
##Cheese
##Bread
##Tofu '''

#The os.path.join() function is helpful if you need to create strings for filenames
import os

my_dir = "/Users/test"
my_files = ['.DS_Store', 'test.ser', 'testing123', 'test.txt', 'hello.txt']

for files in my_files:
    
    my_join = os.path.join(my_dir, files)
    print(my_join)

# output:
/Users/test/.DS_Store
/Users/test/test.ser
/Users/test/testing123
/Users/test/test.txt
/Users/test/hello.txt
