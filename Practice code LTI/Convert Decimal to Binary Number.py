# Convert Decimal to Binary Number


# Function to convert decimal number
# to binary using recursion
def DecimalToBinary(num):
     
    if num >= 1:
        DecimalToBinary(num // 2)
    print(num % 2, end = '')
 
# Driver Code
if __name__ == '__main__':
     
    # decimal value
    dec_val = 24
     
    # Calling function
    DecimalToBinary(dec_val)


            ######  OR ##########
# Python program to convert decimal to binary
   
# Function to convert Decimal number
# to Binary number
def decimalToBinary(n):
    return "{0:b}".format(int(n))
   
# Driver code
if __name__ == '__main__':
    print(decimalToBinary(8))
    print(decimalToBinary(18))
    print(decimalToBinary(7))