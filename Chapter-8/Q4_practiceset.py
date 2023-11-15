# Write  a recursive function to calculate the sum of first n natural numbers.

def sumN (n):
    if n==1:
        return 1
    return sumN(n-1)+n
    
f = sumN(5)
print(f)       


   


