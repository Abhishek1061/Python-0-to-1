'''Write a program to create a dictionary of hindi words with values 
as their english translation provide user with an option to look it up! '''

myDict = {
    "Pankha" : "Fan",
    "Dabba": "Box",
    "Vastu":"Things"
}
 
print("Options are",myDict.keys())
a = input ("Enter the Hindi Word\n")
#print("THe meaning of your word is:", myDict[a])


# Below line will not throw an error if the key is not present in dictionary
print("the meaning of your word is :",myDict.get(a))

