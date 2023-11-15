'''Write aprogram to read the text from a given  file 'poems.txt'
 and find out whether it contains the word 'twinkle.'''

f = open('poems.txt')
t = f.read()
if 'Twinkle' in t:
    print("Twinkle is present")
else: 
    print("Twinkle is not present")
f.close()