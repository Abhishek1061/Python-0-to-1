'''Write  program to print multiplication table of agiven number using for loop.'''

num = int(input("Enter the number of table of you want print\n"))

for i in range(1, 11):
    # print(str(num)+ "X" + str(i) + "=" + str(i*num))
    # OR method
    print(f"{num}X{i}={num*i}")     # f is called f-string
 

 