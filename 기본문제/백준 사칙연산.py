"""
문제
// 두 자연수 a와 b가 주어진다. 이때, a+b, a-b, a*b, a/b(몫), a%b(나머지)를 출력하는 프로그램을 작성하시오. //
"""

num1 = int(input("첫 번째 숫자 입력: "))
num2 = int(input("두 번째 숫자 입력: "))

add = num1 + num2       # add = 더하기
minus = num1 - num2     # min = 빼기
mul = num1 * num2       # mul = 곱하기
div = num1 // num2      # div = 나누기 // -> 나누기 몫의 소수점 이하의 수를 버리고 정수만 기입, / -> 나누기 소수점 출력
rem = num1 % num2       # rem = 나머지 %는 나머지만 구함

print("", add, "\n", minus, "\n", mul, "\n", div, "\n", rem)


"""
a,b = map(int, input("숫자 두 개를 입력: ").split())
print(" a: ", a, "\n","b: ", b)

a, b = input().split()으로 받을 수 도 있음
하지만 숫자를 입력해서 계산을 해야 할 경우
다시 int로 초기화를 해주어야 함
ex) c = int(a)

추가적으로 map을 사용할 경우
map은 적용할 함수, 반복 가능한 자료형이다 한줄 코딩을 해야함

a, b = map(int, input("숫자 두 개를 입력: ").split())
print(" a: ", a, "\n","b: ", b)

add = a + b
miu = a - b
mul = a * b
div = a // b
rem = a % b

print("", add, "\n", minus, "\n", mul, "\n", div, "\n", rem)
"""