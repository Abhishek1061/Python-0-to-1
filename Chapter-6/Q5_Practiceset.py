''' Write a program which finds out whether a given name is present in a list or not.'''
names = ["abhishek", 'himanshu', 'suraj','anarghya','atnarv']

name = input("Enter the name to check\n")

if name in names:
    print("Your name is present in the list")
else:
    print("Your name is not present in the list")

