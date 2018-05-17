def selectionSort(arr):
    n = len(arr)


    for i in range(n):
        small=i
        for j in range(i+1,n):


            if arr[j] < arr[small] :
                small=j
        arr[i], arr[small] = arr[small], arr[i]

# Driver code to test above
arr = [64, 34, 25, 12, 22, 11, 90]

selectionSort(arr)

print ("Sorted array is:")
for i in range(len(arr)):
    print ("%d" %arr[i])

def reverse(string):
    if len(string) == 0:
        return string
    else:
        return reverse(string[1:]) + string[0]
a = str(input("Enter the string to be reversed: "))
print(reverse(a))

s=""
for ch in range(97,123):
    lett=chr(ch)
    for i in range(len(a)):

        if (a[i]==lett):
            s=s+lett
print(s)

s=""
for i in range(len(a)):
    v=ord(a[i])
    v2=96+(v-96)*2
    if v2>122:
        v2=96+(v2-122)
    s=s+chr(v2)

print(s)

n=int(input())
b=[[0 for j in range(n)] for i in range(n)]
for i in range(n):
    for j in range(n):
        b[i][j]=int(input())
print()
for i in range(n):
    for j in range(n):
        print(b[i][j],)


