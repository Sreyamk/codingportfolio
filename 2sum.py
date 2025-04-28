list1=list(map(int,input().split()))
target=int(input('enter the sum'))
l=len(list1)
count=0

for i in range (l):    
    for j in range (i+1,l):
        if(list1[i]+list1[j]==target):
            print(i,j)
            count+=1
            

if (count==0):
    print("none")



          