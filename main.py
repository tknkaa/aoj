n = int(input())
a = list(map(int, input().split(" ")))
count = 0
for i in range(n):
    for j in range(n - 1, i, -1):
        if a[j] < a[j-1]:
            count += 1
            tmp = a[j]
            a[j] = a[j-1]
            a[j-1] = tmp

output = ""
for i in range(n):
    output += str(a[i])
    if i != n - 1:
        output += " "
print(output)
print(count)
