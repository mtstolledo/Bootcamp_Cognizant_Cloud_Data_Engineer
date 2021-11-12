n = int(input())

fib_list = []

for i in range(n):

    if i > 1:
        fib_list.append(fib_list[i-1] + fib_list[i-2])
    else:
        fib_list.append(i)

print(' '.join(map(str, fib_list)))