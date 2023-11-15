myDict = {
    "fast":"In a Quick Manner",
    "harry": "A Coder",
    "marks": [1,2,5],
    "anotherdict": {'harry': 'Player' },
    1:2               
 }

 # Dictionary Methods
# print(type(myDict.keys())) # Typecasing tell the type of syntax.
# print(myDict.keys()) # Prints the keys of the dictionary.
# print(list(myDict.keys())) # it converts the di ct_keys  into list format.
# print(myDict.items()) # it shows all the items in the dictionary.
print(myDict.values()) # it prints the values of the dictionaries.
print(myDict)
updateDict={
    "Lovish":"Friend",
    "Shubham":"Friend",
    "Divya":"Friend",
    "harry": "A Dancer"
}
myDict.update(updateDict) # this helps to update the Dictionary. # Updates the dictionary by adding  key-value pairs from updateDict
print(myDict)


#  The Different between .get and [] snytax in Dictionaries.?
print(myDict.get("harry2")) # When runed then it will not show error but it will show it as a None (means the character is not present in list).
# print(myDict["harry2"]) # This will throw an error as harry2 is not present in the dictionary.

print(myDict.get("harry")) # this will call out the value of  Harry , for that get function is used.
 
