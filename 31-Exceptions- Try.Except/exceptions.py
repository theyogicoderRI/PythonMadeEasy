
# def addme(y):
#     x = 5
#     return x + y

# #addme('hi')  
# # returns: Exception has occurred: TypeError
# #unsupported operand type(s) for +: 'int' and 'str'
# #program terminates

# # using try/except
# try:
#     addme("hi")
# except TypeError: #catch and recover
#     print("wrong Type Used")  # this  block under except is our exception handler
#     print('I keep going')

# print('Program does not stop')
# # program does not terminate


### raising an error on purpose

# try:
#     raise TypeError
# except TypeError:
#     print("You raised a TypeError")


#different type of errors

# try:
#     list0 = [1,2,3]
#     list1 = {}
#     list1.append(list0)
# except NameError:
#     print("NameError")  
# except SyntaxError:
#     print("This is a syntax error") 
# except TypeError:
#     print("Type Error")
# except AttributeError:
#     print("Attribute Error")
#     print("this one wins") 


# try:
#     hello = 'hello'
#     print(hello[7])
    
# except NameError:
#     print("NameError")  
# except SyntaxError:
#     print("This is a syntax error") 
# except TypeError:
#     print("Type Error")
# except AttributeError:
#     print("Attribute Error")
# except KeyError:
#     print("Key Error")                
# except IndexError:
#     print("Index Error") 
#     print("this one wins") 


# try:
#     hi = 'hi'
#     x = 2
#     print(hi + x)
    
# except NameError:
#     print("NameError")  
# except SyntaxError:
#     print("This is a syntax error") 
# except TypeError:
#     print("Type Error")
#     print("this one wins")  
# except AttributeError:
#     print("Attribute Error")
# except KeyError:
#     print("Key Error")                
# except IndexError:
#     print("Index Error") 

# try:
#     one = 'one'
#     print(One)
    
# except NameError:
#     print("NameError") 
#     print("this one wins")  
# except SyntaxError:
#     print("This is a syntax error") 
# except TypeError:
#     print("Type Error") 
# except AttributeError:
#     print("Attribute Error")
# except KeyError:
#     print("Key Error")                
# except IndexError:
#     print("Index Error")


# try:
#     eval ('a === b')   
# except NameError:
#     print("NameError")   
# except SyntaxError:
#     print("This is a syntax error")
#     print("this one wins")   
# except TypeError:
#     print("Type Error") 
# except AttributeError:
#     print("Attribute Error")
# except KeyError:
#     print("Key Error")                
# except IndexError:
#     print("Index Error")            

# NOTE: you can only catch syntax errors 
# when python is trying to parse something. 
# This includes exec, eval, import

# try:
#     dict2 = {1:"one", 2:"two" }
#     print(dict2[3]) 
# except NameError:
#     print("NameError")    
# except SyntaxError:
#     print("This is a syntax error") 
# except TypeError:
#     print("Type Error") 
# except AttributeError:
#     print("Attribute Error")
# except KeyError:
#     print("Key Error") 
#     print("this one wins")                
# except IndexError:
#     print("Index Error") 
 

# not specified -it catches them all
# try:
#     dict2 = {1:"one", 2:"two" }
#     print(dict2[3]) 
# except:
#     print("All other errors")      

# using the else clause   
# 
# 
# try:
#     y = 1/0
# except ZeroDivisionError:
#     print("You're trying to divide by zero")  
# else:
#     print("else branch")


# try:
#     y = 1/1
# except ZeroDivisionError:
#     print("You're trying to divide by zero")  
# else:
#     print("else branch has been reached - no error to trap")   
# 
#try/finally

# finally no error
# my_file = open('my_file.txt')
# try:
#     data = my_file.read()
#     print(data)
# finally:
#     my_file.close()
#     if my_file.closed:
#         print("No error. File is Closed")

# print("keep going if all is well") 
# print()
# print("Now when error is detected")
# my_file = open('my_file.txt')
# try:
#     data = my_file.read()
#     print(2+ "hi")
    
# finally:
#     my_file.close()
#     if my_file.closed:
#         print("Error File still gets Closed")

# print("keep going if all is well") 


# #unified:
# print("no error in except branch")
# try:
#     print(2+ "hi")
# except TypeError:
#     print("type error caught") 
# else:
#     print("No Error")           
# finally:
#     print("finally always runs")

# print("keep going if all is well") 

# print()
# print("Error in except branch")
# #unified error in except too:

# try:
#     print(2+ "hi")
# except:
#     print("type error caught") 
#     5/0
# else:
#     print("No Error")           
# finally:
#     print("finally always runs")

# print("keep going if all is well") 
  

 #the raise statement
try:
    raise NameError("hello")
except NameError:
    print("Propagating To Default Level")
    raise
  

