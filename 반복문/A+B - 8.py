import sys

TestCase = int(input())

for i in range(TestCase):
    a, b = map(int, sys.stdin.readline().strip().split())
    print(f"Case #{i + 1}: {a} + {b} = {a + b}")