a = int(input())
b = list(map(int,input().split()))
b.sort()
l=[]
for i in range(a):
    l.append(b[i] + b[len(b)-i-1])
print(max(l))