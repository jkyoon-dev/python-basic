# 실습문제
# 회사를 그만두게 된 유진이는 유튜브를 시작하게 됐다. 그리고 유튜브를 통해 수익창출을 하려고 한다. 프로그램 사용자로부터 현재 구독자 수를 입력 받으면, 수익 창출이 가능한지 불가능한지 알려주는 프로그램을 작성해보자.
# 단 수익창출은 구독자가 1000명 이상일 경우 가능하다.

# 표준입력 현재 구독자 수를 입력하세요 >>> 1200
# 표준출력 수익 창출이 가능합니다! 수익 창출이 불가능합니다.

# money_count = 1000
# if money_count > int(input("현재 구독자 수를 입력하세요>>>")):
#     print("수익 창출이 불가능합니다.")
# else:
#     print("수익 창출이 쌉가능합니다.")

# 실습문제 2
# 조건 10시간 이상 핸드폰 잠금 해제, 5시간 이상 휴대폰 30분 사용가능 나머지 불가능

# input_time = int(input("공부시간을 입력하세요."))
# if input_time >= 5 and input_time < 10: # true and false > 10 false
#     print("핸드폰 30분 사용")
# elif input_time >= 10: # 10시간 이상 잠금 해제
#     print("핸드폰 잠금해제")
# else: # 나머지는 불가
#     print("핸드폰 사용불가")

# 실습문제 3
# 조건 20000원 이상 치킨, 10000원 이상 떡볶이, 2000원 이상: 편의점 김밥

# money = int(input("가진돈을 입력하세요."))
# if money >= 20000: # 10시간 이상 잠금 해제
#     print("치킨")
# elif money >= 10000 and money < 20000: # true and false > 10 false
#     print("떡볶이")
# elif money >= 2000 and money < 10000: # true and false > 10 false
#     print("편의점 김밥")
# else: # 나머지는 불가
#     print("굶어")

# 실습문제 4
# 평균 80점 이상 합격 아니면 불합격 단 점수는 0점에서 100점 사이
# korean = int(input("국어 점수를 입력하세요."))
# if 0 < korean > 100:
#     print("점수를 다시 입력하세요.")
    
# math = int(input("수학 점수를 입력하세요."))
# english = int(input("영어 점수를 입력하세요."))
# if 0 < korean > 100:
#     print("점수를 다시 입력하세요.")

# avg = (korean + math + english)/3
# if avg >= 80 or avg <= 100:
#     print("합격")
# else:
#     print("불합격")

# 풀이

korean = int(input("국어 >>>"))
math = int(input("수학 >>>"))
english = int(input("영어 >>>"))
avg = (korean + math + english)/3

# 방법1
if 0 <= korean <= 100 and 0 <= math <= 100 and 0 <= english <= 100:
    print("입력이 정확함")
    if avg >= 80:
        print("합격")
    else:
        print("탈락")
else:
    print("잘못 입력했습니다")

# 방법2
if korean < 0 or korean > 100 or math < 0 or math > 100 or english < 0 or english > 100:
    print("잘못입력하셨습니다.")
elif avg >= 80:
    print("합격")
else:
    pring("불합격")
