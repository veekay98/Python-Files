n1=int(input())
a=[]

s=input()
for i in s.split(' '):
    a.append(i)
a=set(a)

n2=int(input())
b=[]

s=input()
for i in s.split(' '):
    b.append(i)
b=set(b)


print(len(a | b))
