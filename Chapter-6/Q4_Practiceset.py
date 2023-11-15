''' Write a program to find whether a given username contains less than 
10 characters or not.'''

name =  input("Enter your name : ")
a = len(name)


if(a<10):
    print("User contains less than 10 characters.")
else:
    print("User dose not contains less than 10 characters.")