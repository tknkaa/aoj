pair = list(map(int, input().split(" ")))
pair = sorted(pair)
ans = ""
for i in range(len(pair)):
    if i != len(pair) - 1:
        ans += str(pair[i]) + " "
    else:
        ans += str(pair[i])
print(ans)
