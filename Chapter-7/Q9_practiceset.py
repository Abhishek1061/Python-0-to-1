''' Write a program to print the following star pattern

* * *
*   *
* * *

for n = 3 '''

n = 3

for i in range (3):
  print(" " * (i+2), end = "")
  print("*" * (2*i+1), end = "")
  print(" " * (3-i-1))

