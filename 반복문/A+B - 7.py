"""
T = int(input())

for i in range(0, T):
    a, b = map(int, sys.stdin.readline().strip().split())
    print("Case #", i + 1 ,":", a + b)
"""
import sys

T = int(input())

for i in range(T):
    a, b = map(int, sys.stdin.readline().strip().split())
    print(f"Case #{i+1}: {a + b}")