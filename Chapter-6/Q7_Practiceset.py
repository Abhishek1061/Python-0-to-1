'''Write a program to find out whether a given post is talking about "Harry" or not.'''

text= input("Enter the post comment : ")

if("harry" in text):
    print("Post is talking about harry")
elif("Harry" in text):
    print("Post is talking about harry")
elif("HARRY" in text):
    print("Post is talking about harry")
else:
    print("Post is not talking about harry")

