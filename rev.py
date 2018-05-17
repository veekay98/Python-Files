s=input()

c=0

for i in range(len(s)):
    if s[i]==' ':
        c+=1

print(c)
s1=""
while(c>=0):
    s1=s1+s.split(' ')[c]+" "
    c-=1

print(s1)
