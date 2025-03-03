T, X = map(int, input().split())

a = [int(x) for x in input().split()]
# a = list(map(int, input().split()))
n = [i for i in a if i < X]

print(*n)