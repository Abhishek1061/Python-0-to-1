# Write a python function to remove a given word from a string and strip it at the same time
 
#  Strip function is the function in which it removes any extraspaces into the code and print the statement
# for example
'''  this = "   helllo Abhishek        "
print(this)
print(this.strip()) '''


#  now solution for the question


def remove_and_strip(string, word):
    newStr = string.replace(word,"")
    return newStr . strip()

this = "   Abhishek is a good       "
n = remove_and_strip(this, "Abhishek")
print(n)
# print(n.strip())

