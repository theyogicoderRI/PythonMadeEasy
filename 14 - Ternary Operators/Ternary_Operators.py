#Ternary Operators aka conditional expressions
##a = 4
##b = 5
##the_value = a if a < b else b
##print(the_value == a)
##print(the_value == b)
##
##print("a" if a<b else "b")

##y = 14
##z = 17
##
##if y > z:
##    print(y)
##else:
##    print(z)
##
##
##y = 14
##z = 17
##print({True: f"y:{y}", False: f"z:{z}"} [y>z])
##

# using contional statements with List comprehensions

foodies = ("tofu", "tempeh", "bean sprouts", "cauliflower-crust Pizza")

foodies_list = [food for food in foodies]
print(foodies_list)
my_food_list = [food for food in foodies if food != 'bean sprouts']

print(my_food_list)


