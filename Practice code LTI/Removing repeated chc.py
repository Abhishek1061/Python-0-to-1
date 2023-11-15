# i/p = Abhishekkadam
# o/p = Abhisekadm

def RemovingChars(n):
    s=""
    for i in n:
        if i in s:
            pass
        else:
            s+=i
    return s

n = "Abhishekkadam"
print(RemovingChars(n))