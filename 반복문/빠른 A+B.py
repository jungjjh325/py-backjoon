#뇌가 살살녹ㄴㄴ다

import sys

testcase = int(input())

for i in range(testcase):
    a, b = map(int, sys.stdin.readline().split())
    print(a + b)

"""
5
1 1
12 34
5 500
40 60
1000 1000
"""