"""
같은눈 3개 10000 + (같은눈) * 1000
같은눈 2개 1000 + (같은눈) * 100
다른눈 (그중 가장 큰눈) * 100

336 -> 1300
222 -> 12000
625 -> 600
"""
a, b, c = map(int, input().split())

if a == b == c:
    d = 10000 + a * 1000
    print(d)

elif a == b or b == c or c == a:
    if a == b or c == a:
        d = 1000 + a * 100
        print(d)
    else:
        d = 1000 + b * 100
        print(d)
else:
    d = max(a, b, c)
    e = d * 100
    print(e)