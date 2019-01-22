#files
##new_file = open("new_file.txt", 'w')
##new_file.write("What is up Python Folks?\n")
##new_file.write("Look ma, no hands!\n")
##new_file.close()               

##new_file = open("new_file.txt", 'r')
##print(new_file.readlines())
##print(type(new_file.readlines()))



##print(open('new_file.txt').read())

# using file iterators:

##my_file = "new_file.txt"
##for line in open(my_file):
##    print(line.rstrip())
    
# using file context managers
##with open("new_file.txt") as f:
##    for line in f:
##        print(line.rstrip())

##new_file2 = open("new_file2.txt", 'w')      
##my_num = ("The number of pages is", 1042)
##con_string = str(my_num)
##print(type(con_string))
##new_file2.write(con_string)
##new_file2.close()  
##print(open('new_file2.txt').read())


# getting file objects current position using tell()
# change objects position using seek()
with open("new_file.txt") as f:
    print(f.tell())
    f.seek(44)
    for line in f:
        print(line.rstrip())
    





