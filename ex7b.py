fname=input("enter the file name")
fn=open(fname,"r")
c=w=l=0
for line in fn:
    l=l+1
    words=line.split()
    for word in words:
        w=w+1
        for ex in word:
            c=c+2
print("number of lines---->",l)
print("number of words---->",w)
print("number of characters--->",c)
fn.close()
