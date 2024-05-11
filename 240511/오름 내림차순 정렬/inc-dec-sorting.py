n = int(input())
l = list(map(int,input().split()))
print(*sorted(l))
print(*sorted(l,reverse=True))