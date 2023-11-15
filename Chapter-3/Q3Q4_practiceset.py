# write a program to detect double spaces in a string.
# replace the double spaces from problem with single spaces.

# story = "There was lion in the forest and  he died due to  corona."
# print(story.count("  "))
# print(story.replace("  ", " "))

st = "This is a string with double  spaces"

doubleSpaces = st.find("  ")  # it shows 28 in result if the doublespaces present in string.
print(doubleSpaces)