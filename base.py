import math

n=int(input())

temp=n
rem=0
c=0
bin=0
while(math.floor(temp)>0):
    rem=temp%2

    bin+=rem*(10**c)
    c+=1
    temp=math.floor(temp/2)

print(bin)

c=0
oct=0
temp=n
while(math.floor(temp)>0):
    rem=temp%8

    oct+=rem*(10**c)
    c+=1
    temp=math.floor(temp/8)

print(oct)


c=0
hex=""
temp=n
while(math.floor(temp)>0):
    rem=temp%16
    if (rem==10):
        hex="A"+hex
    elif (rem==11):
        hex="B"+hex
    elif (rem==12):
        hex="C"+hex
    elif (rem==13):
        hex="D"+hex
    elif (rem==14):
        hex="E"+hex
    elif (rem==15):
        hex="F"+hex
    else:
        hex=str(rem)+hex


    c+=1
    temp=math.floor(temp/16)

print(hex)

