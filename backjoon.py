a = int(input())
stack = []

for i in range(a):
    num = int(input())
    if num == 0:
        stack.pop()
    else:
        stack.append(num)
    
print(sum(stack))

