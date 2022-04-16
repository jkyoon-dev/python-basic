# 제어문 : 조건에 따라 실행할 명령이 달라지는 것
# 조건문, 반복문

# 치킨 or 피자 = 조건문
# 유튜브 연속보기 = 반복문

origin_pass = "1234"
input_pass =input("패스워드를 입력하세요 >>>")

if input_pass == origin_pass:
    print("로그인 됐습니다.")
elif input_pass == "":
    print("비밀번호를 입력하세요")
else:
    print("비밀번호가 다릅니다.")