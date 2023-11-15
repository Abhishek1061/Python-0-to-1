''' Write a program to print multiple table of n using for loop in reversed order.'''

from audioop import reverse


num = int(input("Enter the number of table of you want print\n"))

for i in range(1, 11):
    # print(str(num)+ "X" + str(i) + "=" + str(i*num))
    # OR method
    T  = ((f"{num}X{i}={num*i}"))
    print(T)
print("reverse table",reverse(T))
   # f is called f-string
    

 

