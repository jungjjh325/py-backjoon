#재활 어렵다

result = int(input())
n = int(input())

c = 0
for i in range(n):
    a, b = map(int, input().split())

    c += a * b

if c == result:
    print("Yes")
else:
    print("No")
"""
260000
4
20000 5
30000 2
10000 6
5000 8

누적시키는 거에 대한 부분을 보완할 필요가 있음
"""