# Find the Position of a Substring within a String
string = 'Geeks'
letter = 'k'
print(string.rfind(letter))


            #### OR #####
import re
string = 'Geeksforgeeks'
pattern = 'for'
match=(re.search(pattern, string))
 
#getting the starting index using match.start()
print ("starting index", match.start())
 
#Getting the start and end index in tuple format using match.span()
print ("start and end index", match.span())