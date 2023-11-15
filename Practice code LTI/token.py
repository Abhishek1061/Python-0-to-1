n=int(input())

arr = sorted(list(map(int,input().split())))

s=abs(arr[0]-arr[1])+abs(arr[-1]-arr[-2])

for i in range(1,n-1):

    s+=min(abs(arr[i]-arr[i-1]),abs(arr[i]-arr[i+1]))

print(s)
