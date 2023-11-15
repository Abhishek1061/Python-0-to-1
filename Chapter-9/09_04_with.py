with open('another.txt','r') as f:
    a =f.read()
with open('another.txt','w') as f:
    a = f.write("me")
print(a)

#  with statement when used no need to write to f.close() then.