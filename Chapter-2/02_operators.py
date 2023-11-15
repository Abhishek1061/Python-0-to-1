from ast import operator


a = 3
b = 4 

# Arithmetic operators
print ("the value of 3+4 is ", 3+4)
print ("the value of 3-4 is ", 3-4)
print ("the value of 3*4 is ", 3*4)
print ("the value of 3/4 is ", 3/4)

# Assignment Operators
a = 34 
a += 2
a -= 12
a *= 12
a /= 2       # if you divide the digit in python then the soution of that code gets in floating point number.
print (a)

# Comparison operators
b = (14>=7) # this means that 14 is greater than and  equal to seven which is True accoroing to boolen
b1 = (14<=7) # this means that 14 is less than and equal to seven which is false accoroing to boolen
b2 = (14>7)  # this means that 14 is greater than  seven which is True accoroing to boolen
b3 = (14<7)  # this means that 14 is less than  seven which is false accoroing to boolen
b4 = (14==7) # this means that 14 is equal to seven which is false accoroing to boolen
b5 = (14!=7) # this means that 14 is not equal to 7 which is ture 
print (b)
print (b1)
print (b2) 
print (b3)
print (b4)
print (b5)

# Logical Operators
bool1 = True
bool2 = False
print("the value of bool1 and bool2 is",(bool1 and bool2)) #  this makes false cuz both should be true to get output true or else it will show flase like (+- is - ans -+ is - but ++ is +)
print("the value of bool1 or bool2 is",(bool1 or bool2)) # this makes the output true cuz among both one should be true and bool1 is true so it makes it true.
print("the value of bool1 not bool2 is", (not bool2)) #this not alters the value of boolen as value od bool2 is false but the output is now true cuz of not function.