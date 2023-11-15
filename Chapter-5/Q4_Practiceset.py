'''What will be the length of following set s
s = set()
s.add(20)
s.add(20.0)
s.add("20")'''
s = {20,20.0,"20"}  # as both values (20,20.0) are equal then it is printed as single element.
print(s)
print(len(s))