import sys

T = int(input())
a = list(map(int, sys.stdin.readline().split()))
b = int(input())

r = a.count(b)

print(r)
"""
11
1 4 1 2 4 2 4 2 3 4 4
2

= 3

총 N개의 정수가 주어졌을 때, 정수 v가 몇 개인지 구하는 프로그램을 작성하시오.
"""