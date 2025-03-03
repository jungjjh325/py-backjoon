import sys

while True:
    try:
        a, b = map(int, sys.stdin.readline().strip().split())
        print(a + b)
    except:
        break

"""        
for input_line in sys.stdin:
    a, b = map(int, input_line.split())
    print(a + b)
"""