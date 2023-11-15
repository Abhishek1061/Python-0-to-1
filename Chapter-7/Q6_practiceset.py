''' Write a program to calcuate the factorial of a given number using for loop.'''

# n! = 1 X 2 X 3 X 4 X 5 X 6 .....n


num = int(input("Enter the number: "))
factorial = 1
for i  in range(1,num+1):
    factorial = factorial * i

print(f"The factorial of this number is {factorial} ")

