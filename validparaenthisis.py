stack=[]
s='[()]'
for i in range (len(s)):
    if (s[i]='('):
        stack.append(s[i])
        elif (s[i]=')'):
if s[i] == '(':
    stack.append(s[i])
elif s[i] == ')':
    if stack and stack[-1] == '(':
        stack.pop()
    else:
        stack.append(s[i])
  