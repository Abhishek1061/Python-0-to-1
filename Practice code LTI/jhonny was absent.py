# Johnny was absent in his english class when the vowel topic was taught by the teacher . His english teacher gave him two strings and told him to find the length of the longest common subsequence which contains only vowels, as a punishment for not attending english class yesterday .
# Help Jhonny by writing a code to find the length of the longest common subsequence 
# Input Specification:
# input1: First string given by his teacher
# # input2: Second string given by his teacher.
# Output Specification:
# Return the length of the longest common subsequence which contains only vowels.
# Example 1:
# vowelpunish
# english
# Output : 2
# Example 2:
# # prepinsta
# prepare
# # Output : 

a=input()

b= input()

m,n=len(a),len(b)

vow="aeiou"

DP= [[0 for i in range(n + 1)]for j in range(m + 1)]

i, j = 0, 0

for i in range(m + 1):

    for j in range(n + 1):

        if (i == 0 or j == 0):

            DP[i][j] = 0

        elif ((a[i - 1] == b[j - 1]) and a[i - 1] in vow):

            DP[i][j] = DP[i - 1][j - 1] + 1

        else:

            DP[i][j] = max(DP[i - 1][j],DP[i][j - 1])
print(DP[m][n])