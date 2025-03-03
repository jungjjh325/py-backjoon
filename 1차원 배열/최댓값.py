a = [int(input()) for i in range(9)]

m = max(a)
mm = a.index(m) + 1

print(m)
print(mm)

"""
int(input())으로 한 번 입력받으면 줄바꿈 되니까 그걸 이용
map(int, input()) 이렇게 했으면 줄바꿈 없이 그냥 입력 받아야하니 오류

범위를 9로 제한 시켜서 9개까지만 입력 되게
"""