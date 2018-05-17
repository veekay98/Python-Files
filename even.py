print("Enter the size of the array")

n=int(input())

a=[]

print("Enter the elements of the array")
for i in range(n):
    a.append(int(input()))
print("The elements at even positions are")

b=[]
for i in range(n):
    if (i%2==1):
        b.append(a[i])

print(b)
