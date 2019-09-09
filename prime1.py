q=int(input("enter a value"))
c=2
for p in range(2,int(q/2+1)):
    if q%p==0:
        c=c+1
        break
if c==2:
    print("q is prime")
else:
    print("q is not prime")
