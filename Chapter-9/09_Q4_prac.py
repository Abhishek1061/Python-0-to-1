''' A file contains a word "Donkey" multiple times you
need to write a program which replaces this word
with ###### by updating the same list'''


with open("Donkey.txt") as f:
    content = f.read()

content = content.replace("Donkey", "$%^@$^#")

with open("Donkey.txt", "w") as f:
    f.write(content)