# 함수 define
# 정의하기

# 매개변수가 있는 함수
# 매개변수란 함수 안에 쓰일 데이터를 받는 역할을 하는 변수
# def 함수이름(매개변수1, 매개변수2):
#     # 명령블록
#     print("인자1 =",매개변수1,"인자2 =", 매개변수2)
#     return

# 함수이름()

# 호출하기
# 인자란 매개변수 안에 들어갈 데이터
# 함수이름(인자1, 인자2)

# 반환값이 있는 함수
# def 함수이름2():
    # 명령블록
    # return 반환값2
# 호출
# 함수이름2() 

# 매개변수와 반환값이 있는 경우
# def 함수이름3(매개변수1, 매개변수2)
    # 명령블록
    # return 반환값3
# 호출
# 함수이름(인자1, 인자2)

# 기본형
# 1. 정의하기
def printHello():
    print("Hello")

# 2. 호출하기
printHello()

# 매개변수가 있는 함수
def sum(a, b):
    print(a + b)
sum(1,2)

# 3.  반환값이 있는 함수
import random
def getRandomNumber():
    number = random.randint(1,10)
    return number

print(getRandomNumber())

# 4. 매개변수와 반환값이 있는 함수
def add(a, b):
    result = a + b
    return result

print(add(5,6))