# general format
##
##a = 0
##b = 5
##while a < b:
##   a += 1
##   print (a)
##else:
##    print("Does the else print?")
##    print("Yes. Yes it does, because it never hit a break")


##a = 0
##b = 5
##while a < b:
##   a += 1
##   print (a)
##   break
##else:
##    print("Does the else print?")
##    print("Yes. Yes it does, because it never hit a break")
##
##print("I am  the first piece of code outside the whlle loop. I thought you'd never get to me")    


# parse out odd numbers

##x = 10
##count = 0
##odds = []
##while x:
##     x = x -1
##     count = count + 1
##     if x % 2 == 0:
##         continue
##     odds.append(x)      
##     print("Which interation? ", count, "Odd Number: ", x)
##         
##print("Here are all the odds numbers: ", odds)


# The magic number tp guess is 6
while True:
    user_guess = int(input("Guess a number between 1 and 10: "))
    if user_guess < 6:        
        print("Sorry that number is too low, try again.")
    elif user_guess > 6:  
       print("Sorry that number is too high, try again.")
    else:
       print('You guess right. The magic number is 6!!')
       break

print("Game over!")             
                     
