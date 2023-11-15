''' If langauges of two friends are same ;
then what will happen to the program in problem 6?'''

from platform import python_branch


favLang= {}

a=(input("Enter your favourate language Shibham\n"))
b=(input("Enter your favourate language Ankit\n"))
c=(input("Enter your favourate language Sonali\n"))
d=(input("Enter your favourate language Harshita\n"))

favLang['Shubham'] = a
favLang['ankit'] = b 
favLang['sonali'] = c
favLang['harshita'] = d

print(favLang)


# If languages of two friends are same then it will print the values and no chages will occur cuz vlaues can be considered as different.