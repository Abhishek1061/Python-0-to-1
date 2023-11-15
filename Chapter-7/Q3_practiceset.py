'''Write  program to print multiplication table of agiven number using while loop.'''

i = 1
num = int(input("Enter the number of table of you want print\n"))

while i<=10:
    print(str(num)+ "X" + str(i) + "=" + str(i*num))
    # or
    # print(f"{num}X{i}={num*i}")  
    i=i+1

