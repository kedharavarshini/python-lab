a=int(input("enter a number"))
for b in range(2,a):
    if a%b==0:
        break
if b<a:
 print(a,"is prime")
else:
 print(a,"is not prime")   
