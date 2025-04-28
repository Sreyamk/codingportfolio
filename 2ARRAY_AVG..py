l=int(input('enter size of l1'))
li1=list(map(int,input().split(" ")))
li2=list(map(int,input().split(" ")))
l2=len(li2)
print(li1,li2)
j=0
for i in range (l,l2+l):
    
    li1[i] = li2[j]
    j+=1

print(li1)

