import random

with open('foot.txt') as f:
	words = list(f)
org=random.choice(words).strip()

new=[]
for i in range(len(org)):
    new.append('_')

cw=0
bw=""

while (1):
    f=0
    aap=0
    print("Enter a letter")
    ch=input()
    for i in range(len(bw)):
        if ch[0]==bw[i]:
            aap=1
    if aap==1:
        print("Already entered")
        print()
        continue
    else:
        bw=bw+ch
    for i in range(len(org)):
        if org[i]==ch[0]:
            new[i]=ch[0]
            f=1
    if f!=1:

        print("Not present")
        cw+=1



    if cw==5:
        print("Game over")
        break
    print(new)
    c=0
    for i in range(len(org)):
        if new[i]=='_':
            c+=1
    if c==0:
        print()
        print(org.upper())
        print()
        print("BINGO!!")
        break
    print()


