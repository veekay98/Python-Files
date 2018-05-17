a=[3,2,3,4,5]


while(1):
    s=input()
    if s=="insert":
        pos=int(input())
        elem=int(input())
        a[pos]=elem
        print(a)
        continue

    elif s=="print":
        print(a)
        continue

    elif s=="remov":
        b=[]
        c=0
        rem=int(input())
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

    elif s=="append":
        n=int(input())
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

    elif s=="rev":
        b=[]
        i=len(a)-1
        while(i>=0):
            b.append(a[i])
            i-=1
        a=b
        print(a)
        continue


    elif s=="stop":
        break
