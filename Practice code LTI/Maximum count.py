a = "wddihbwduvjdvkkkkkkkkkkkkkkkkkkkkkkkkkkk"

count = 0 
maxcount = 0
lastCharacter = ""
longestcharacter = ""

for ch in a:
    if(ch == lastCharacter):
        count += 1 
        if(count > maxcount):
            maxcount = count
            longestcharacter = ch

    else:
        count = 1 
        lastCharacter = ch

print(longestcharacter)
print(maxcount)