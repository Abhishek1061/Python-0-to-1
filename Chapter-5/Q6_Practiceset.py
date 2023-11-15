''' Create an empty dictionary. Allow 4 friends to enter their favourite language as values
 and use keys as their names. Assume that the names are unique.'''

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