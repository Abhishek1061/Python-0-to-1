letter ='''Dear <|Name|>
Your are selected!
have a great day ahead!
Thanks and regards, 
Date: <|Date|>
'''
name = input("Enter Your Name\n")
date= input("Enter Date\n")
letter =(letter.replace("<|Name|>",name))
letter =(letter.replace("<|Date|>",date))
print(letter)