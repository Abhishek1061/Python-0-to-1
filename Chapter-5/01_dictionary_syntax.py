# these are the dictionaries in that before elements of colon are keys and after elements are values which we can call out whenever needed. 
# dictionaries are mutable and are unordered.
# it is indexed.
# Cannoot contain duplicate keys.
myDict = {
    "Fast":"In a Quick Manner",
    "Harry": "A Coder",
    "Marks": [1,2,5],
    "anotherdict": {'harry': 'Player' }               
}

# print(myDict['Fast'])
# print(myDict['Harry'])
myDict['Marks']  = [45,78]  # in this it will not add new value in 'Marks but it will change or replace it with new value entered. Cuz muliple or duplicate keys are not allowed in dictionary.
print(myDict['Marks'])
print(myDict['anotherdict']['harry'])
