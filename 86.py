k=list(input())
p=[]
for i in k:
   if i not in p:
      p.append(i)
if k==p:
   print("Yes")
else:
   print("No")
