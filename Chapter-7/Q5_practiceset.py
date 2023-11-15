'''Write a program to find the sum of first n natural numbers using while loop.'''

i = 0

num=int(input('Enter the number : '))

if num<i:
    print('enter the positive number')
else:
    sum= 0
    while  (num>i):
        sum += num
        num -= 1
print(sum)

