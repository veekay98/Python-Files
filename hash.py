a=[]
c=int(input())
for i in range(c):
    a.append(int(input()))
print(hash(tuple(a)))
