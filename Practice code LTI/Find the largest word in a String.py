# Find the largest word in a String
# def longestword(x):
#       alist = []
#       length = 0
#       for letter in x:
#              if letter != " ":
#                      length += 1
#              else:
#                      alist.append(length)
#                      length = 0
#       return alist

# n =('my name is abhishek ')
# print(longestword(n))

########## OR ############

print("Enter the String: ")
text = input()
text = text.split()
bigWordLen = 0

for wrd in text:
  wrdLen = len(wrd)
  if wrdLen>bigWordLen:
    bigWordLen = wrdLen

print("\nLargest Word: ")
for wrd in text:
  wrdLen = len(wrd)
  if wrdLen==bigWordLen:
    print(wrd)