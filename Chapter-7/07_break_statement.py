# break statement in python

for i in range (10):
    print(i)
    if i == 5:
        break  

    ''' break end the program in between according to code. menas in this problem it has to excicute till 10 but due to (1==5) break 
    it ended there.'''
else:
    print("This is inside else of for") 
    ''' in this the else statement will not be printed cuz the code is not run naturally
    it was interupted with break statement, so the else is not excicuted.'''