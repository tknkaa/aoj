ints = list(map(int, input().split(" ")))
a = ints[0]
b = ints[1]
if a <= b:
    tmp = a
    a = b
    b = tmp
r = a%b
while r != 0:
    a = b
    b = r
    r = a%b

print(b)
