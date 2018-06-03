s=input()
n1=float(s.split(' ')[0])
m=float(s.split(' ')[1])
a=[]

s=input()
for i in range(n1):
    a.append(float(s.split(' ')[i]))

s=input()
b={}
b=set()
for i in range(m):
    b.add(float(s.split(' ')[i]))

s=input()
c={}
c=set()
for i in range(m):
    c.add(float(s.split(' ')[i]))


sum=0
for i in range(len(a)):
    for elem in b:
        if a[i]==elem:
            sum+=1
    for elem in c:
        if a[i]==elem:
            sum-=1

print(sum)
