## Creating an empty set 

b = set()
print(type(b))

## Adding values to an empty set.
b.add(7)
b.add(5)
b.add(5) # it will not print repeatitive elements cuz set is non repeatative elements.
b.add(5) # adding the value repeatedly dose not changes a set.

##Accessing elements.
#b.add([4, 5, 6 ]) # we cannot put the hashable content like list or dictionary in to the set.
b.add((4, 5, 6))# Only tupple can be added in the set cuz it cannot be chaged and list and dictionary can be chaged or edited.
# b.add({4:5}) # cannot add list or dictionary to sets.

print(b)  

##Length of the set
print(len(b)) # prints the length of this set.

## Removal of an Item.
b.remove(5) # this command removes 5  from the set b .
#b.remove(15 ) # Throws an erroww while trying to remove 15 ( which is not present in the set).
print (b)

print(b.pop())
print(b)

