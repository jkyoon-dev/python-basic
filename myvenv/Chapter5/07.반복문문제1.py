# 문제 1
# 구구단 출력 프로그램 사용자로부터 출력할 단을 입력 받고, 해당 구구단을 출력하는 프로그램이다.

# input_number = int(input("구구단 할 숫자를 입력하세요."))

# for in

# for i in range(1, 10):
#     print(input_number, " X ", i, "=", input_number * i)

# while

# i = 0
# while i < 9:
#     i += 1
#     print(input_number, " X ", i, "=", input_number * i)

# 문제 2
# 숫자 1 입력: 게임을 시작합니다. 숫자 2 출력: 실시간 랭킹 출력, 숫자3 입력: 게임을 종료합니다.
# 단, 3 입력할때까지 프로그램은 계속 실행, 1~3외 다른 숫자 입력 시 다시 입력해 주세요 출력

while True:
    input_game = int(input("[메뉴를 입력하세요]\n1.게임 시작 2. 랭킹보기 3. 게임종료"))
    if input_game == 1:
        print("게임을 시작합니다.")
    elif input_game == 2:
        print("실시간 랭킹")
    elif input_game == 3:
        print("게임을 종료합니다.")
        break
    else:
        print("다시 입력해 주세요.")