"""
print(15 / 2)

num1 = int(input("1번 숫자: "))
num2 = int(input("2번 숫자: "))

print(num1 / num2 * (num2 + num2))
"""

# -> 한 줄 주석으로 단축키 (컨트롤 + /)
# -> """ """ ''' ''' 큰,작은 따음표 3개시 여러줄 주석
"""
import math -> math를 불러와서 math.sqrt를 사용할 수 있음 제곱을 의미

num1 = int(input("a의 값: "))
num2 = int(input("b의 값: "))
num3 = num1 + num2

print("거리: ", num1, " + ", num2, " = ", num3)

d = math.sqrt(550 ** 2 + 600 ** 2)
print("직선의 거리: ", d)
"""