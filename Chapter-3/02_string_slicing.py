
greeting = "Good Morning,"
name ="Abhishek"
# print(type(name))

## code for concantenating two strings ##
c =(greeting + name) 
''' in string with help of + you can do concatenation operations 
which means to combine the strings (ie.+)can be used.'''
# print(c) 

# code for accesing initial two characters of string (ie.Abhishek).
name = "Abhishek"
# print(name[0]) 
''' in this code to get the only characters in code the numbering is used which
should start with zero and the numbering should be in Square Bracket (ie.(name[0]))'''
# the Length is 0-1 for accessing the character.
# name[3] = "d" # Does not work, In string the character can be accessed but can't be changed.

# Code For Slicing
# print(name[0:3]) 
'''In slicing if you are typing[0:3] which means that the accessed character will consider from 0 to 2 
the last it will not consider as the input says to asssessed character form 0 upto 3 which means 0,1,2 not 3,
If i had type "print(name[1:4])" which means it will program 'bhi' means it will include first number (ie.1) and 
last number exclude (ie.4). This is called Slicing as it cut the string as required.'''
# print(name[:4]) # it is same as name[0:4} . # if i write the code by not writting any number before : or after then it will consider prefix of : as 0 and Sufix of : as final value of string.
# print(name[1:]) # is same as name[1:5]
c= name[-4:-1] # this is same as name[1:4] but from reverse manner.
# print(c)

## Slicing with skip
d = name[0:9:2] # in this it will skip 2 letter from string.
print(d)