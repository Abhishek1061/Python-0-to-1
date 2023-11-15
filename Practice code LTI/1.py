# l1=[1, 1,2,3,4,5,5,7,6,9,10]
# l2=[11,12,13,4,5,6,7,18,19,20]
# ans=[]
# for i in l1:
#         if i not in l2:
#             ans.append(i)
# for i in l2:
#         if i not in l1:
#             ans.append(i)
            
# print(len(ans))

def memServer1(req):
    sum = 0
    n = len(req)
    for i in range (0, n):
        if(i%2 == 0):
            sum += req[i]
        return sum

req = 1
req_size = int(input("Enter the size:-\t"))
req = list(map(int, input().split())

result = memServer1(req)
print(result)