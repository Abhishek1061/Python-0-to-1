story = "Once upon a time there was a youtuber named harry who uploaded python course with notes"

# String Functions
print(len(story)) ## to know the how much charaectors are present in the string this function is used.
## this len function returns the length  of the string, as above string lenght is of 87 characters.
print()

# in this story is defined as string.
''' String.endswith ("rry") = this feture tells whether the variable stringends with the string "rry" or not,
 if string is  is "Harry" , it returns true for "rry" since harry end with rry '''
print(story.endswith("notes"))

print(story.count("me")) #it counts the total number of occurance of any characters.

print(story.capitalize()) ## this function capitalize the first character of a given string.

print(story.find("Once")) # this function finds a word and returns the index of first occurance of that word in the string. means it tell at what number the word is present.

print(story.replace("harry", "Abhi")) # This function replace the oldword with newword in the entire string.


