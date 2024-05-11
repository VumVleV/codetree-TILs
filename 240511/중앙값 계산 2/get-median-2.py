a = int(input())
l1 = list(map(int,input().split()))
l2 = []
l3 = []
for i in range(a):
    l2.append(l1[i])
    l2.sort()
    if i%2==0:
        l3.append(l2[int(i/2)])
print(*l3)