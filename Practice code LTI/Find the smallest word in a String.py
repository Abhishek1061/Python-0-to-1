# Find the lsmallest word in a String

print(end="Enter the String: ")
text = input()

text = text.split()
smallWordLen = len(text[0])

for wrd in text:
  wrdLen = len(wrd)
  if wrdLen<smallWordLen:
    smallWordLen = wrdLen

print("\nSmallest Word(s): ", end="")
for wrd in text:
  wrdLen = len(wrd)
  if wrdLen==smallWordLen:
    print(end=wrd +" ")
print()