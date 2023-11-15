# Use open function to read the content of a file
 
filename="sample.txt"
# f = open(filename , 'r')  # by default the mpde is r
f= open('sample.txt')
# data = f.read()
data = f.read(5) #reads first 5 characters from yhe file
print(data)
f.close()

    