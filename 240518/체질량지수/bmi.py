h, w = map(int, input().split())
c = (int(10000*w/(h**2)))
print(c)
if c >=25:
    print("Obesity")