n = int(input())
l=[]
for i in range(n):
    a = input()
    l.append(a)
l.sort()
for i in range(n):
    print(l[i])