str1=input('enter a string')
words=str1.split()
print(words)
for i in words:
    if (len(i)%2==0):
        print(i)


