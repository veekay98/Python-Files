count=int(input())
a=[]
c1=0

while(1):
    c1+=1
    if (c1>count):
        break
    s=input()

    if s.split(' ')[0]=="insert":
        b=[]
        pos=int(s.split(' ')[1])
        elem=int(s.split(' ')[2])
        if len(a)==0 or pos>=len(a):
            a.append(elem)
        else:
            for i in range(pos):
                b.append(a[i])
            b.append(elem)
            for i in range(pos,len(a)):
                b.append(a[i])
            a=b

        print(a)
        continue

    elif s=="print":
        print(a)
        continue

    elif s.split(' ')[0]=="remove":
        b=[]
        c=0
        rem=int(s.split(' ')[1])
        for i in range(len(a)):
            if (a[i]!=rem):
                b.append(a[i])
            else:
                if (c==1):
                    b.append(a[i])
                else:
                    c+=1
        a=b
        print(a)
        continue

    elif s.split(' ')[0]=="append":
        n=int(s.split(' ')[1])
        b=[]
        for i in range(len(a)):
            b.append(a[i])
        b.append(n)
        a=b
        print(a)
        continue

    elif s=="pop":
        b=[]
        for i in range(len(a)-1):
            b.append(a[i])
        a=b
        print(a)
        continue

    elif s=="sort":
        temp=0
        for i in range(len(a)-1):
            for j in range(len(a)-i-1):
                if (a[j]>a[j+1]):
                    temp=a[j]
                    a[j]=a[j+1]
                    a[j+1]=temp
        print(a)
        continue

    elif s=="reverse":
        b=[]
        i=len(a)-1
        while(i>=0):
            b.append(a[i])
            i-=1
        a=b
        print(a)
        continue


