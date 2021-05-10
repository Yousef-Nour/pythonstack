n = input()
s = set(map(int, raw_input().split()))
for i in range(n):
    j = input().spilt()
    if j[0]=="remove":
        s.remove(int(j[1]))
    elif j[0]=="discard":
        s.remove(int(j[1]))
    else:
        s.pop()
print(sum(list(s)))