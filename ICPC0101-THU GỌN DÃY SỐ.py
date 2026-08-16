num = int(input())

arr = list(map(int, input().split()))

stack =[]

for x in arr : 
    stack.append(x)

    if len(stack) >= 2 and (stack[-1] + stack[-2])%2 == 0:
        stack.pop()
        stack.pop()

print(len(stack))