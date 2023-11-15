# Remove brackets from an algebraic expression
#take user input
Exp = "(a-b)+[c*d]+{e/f}"
#initialize an empty string 
Equation = ''
#traversing through string
for i in Exp:
    #checking for brackets
    if ord(i) == 41 or ord(i) == 40 or ord(i) == 91 or ord(i) == 93 or ord(i) == 123 or ord(i) == 125:
        #If True
        pass
    else:
        #if False
        #add it to empty String
        Equation = Equation + i
 #print the string
print(' String without bracket is ' + Equation)