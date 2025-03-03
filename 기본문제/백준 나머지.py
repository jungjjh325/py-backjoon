"""
a = int(input())
b = int(input())
c = int(input())

fir = (a + b) % c
sec = ((a % c) + (b % c)) % c
thi = (a * b) % c
fou = ((a % c) * (b % c)) % c

print(fir, "\n", sec, "\n", thi, "\n", fou)
"""
a, b, c = map(int, input().split())

print((a + b) % c)
print(((a % c) + (b % c)) % c)준
print((a * b) % c)
print(((a % c) * (b % c)) % c)
