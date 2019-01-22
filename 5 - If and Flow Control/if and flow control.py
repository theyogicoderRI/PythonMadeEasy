# basic if statement

# 1 is boolean True. So this test will alwyas succeed
##if 1:
##    print('It\'s true')
##
##
### example # 2. 0 is boolean False
##if 0:
##    print('It\'s true')
##else:
##    print('Nope!')
##    

##
###multiway branch
##
##choices = {'XL': 20.00, 'L': 15.00, 'M': 10.00, 'S': 5.00, 'XS': 2.50}
##
##print("Your Choice of Sizes are:  XL, L, M, S and XS")
##input_1 = input("Please Type one of these 5 sizes and see how much they cost: ")
##
##if input_1 == 'XL':
##    print('That cost: ', choices['XL'])
##elif input_1 == 'L':
##    print('That cost: ' , choices['L'])
##elif input_1 == 'M':
##    print('That cost: ' , choices['M'])
##elif input_1 == 'S':
##    print('That cost: ',  choices['S'])
##elif input_1 == 'XS':
##    print('That cost: ', choices['XS'])
##else: 
##    print('Invalid Choice')    


# guess the number
##number = 4
##print('''You have one try to guess  the magic number between 0 and 10.
##I will give you some help along the way. You can play the game as 
##many times as you want.''')
##guess = int(input ("Now, type a number between 0 and 10 to guess: "))
##               
##if guess > 4:
##    print("You Guessed: ", guess, "Ewww, that number is too high. Sorry")
##elif guess < 4:
##    print("You Guessed: ",guess,"Darn, that number is too low. Sorry, but you can play again")      
##else:
##    print("You guessed the magic number: ", number,"Congrats player.")

import sys
import datetime
now = datetime.datetime.now()
this_year = now .year
year_born = 0

print("Please enter the year you were born: ")
year_born = input()
if year_born.isalpha():
      print("Sorry you entered letters instead of numbers")
      sys.exit()
else:
    year_born = int(year_born)
    if year_born > 1900 and year_born < this_year:
        age = this_year - year_born
        if age < 50:
            years_left = (50 - age)
            print("Not eligible. You have: ",  years_left, " more years to go!")
        elif age > 50:
            been_aarp = age - 50
            print("You have been eligible for : ", been_aarp, " year(s)")
        elif age == 50:
            print("You became eligible this year. Congrats!")
    else:
        print("Your birth year may not be before 1900 or after the current year.")


    
