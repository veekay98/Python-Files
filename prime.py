


n=int(input())
print()



def isprime(val):
    for i in range(2,val):
        if (val%i==0):
            return ("Not prime")

    return ("Prime")

print(isprime(n))

while(1):
    s=input()
    if (s!="c"):
        break
    n=int(input())
    print(isprime(n))
