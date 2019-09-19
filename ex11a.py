r1=input("enter a matrix rows")
c1=input("enter a matrix columns")
a=[]
for i in range(r1):
 a.append([])
for i in range (r1):
 for j in range(c1):
  a[i].insert(j,input("enter value:"))
for i in range(r1):
 for j in range(c1):
  print(c[i][j],"\t")
  print("")
