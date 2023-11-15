'''Write a program to greet all the persons names stored in a list l1 and  which starts with S
l1=["Abhishek","Soham", "Sachin", "Rahul"]'''

l1=["Abhishek","Soham", "Sachin", "Rahul"]

for name in l1:
    if name.startswith("S"):
        print("Hello " + name)
   