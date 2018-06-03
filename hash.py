a=[]
c=int(input())
s=input()
for i in range(c):
    a.append(int(s.split(' ')[i]))

print(hash(tuple(a)))
