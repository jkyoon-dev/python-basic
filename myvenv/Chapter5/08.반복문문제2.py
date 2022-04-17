# 문제 3
# 1. 연습할 한국어가 담긴 리스트를 만든다
# 2. 리스트에서 순서대로 단어를 가져와 화면에 출력한다.
# 3. 프로그램 사용자는 단어를 그대로 입력하고
# 4. 맞추면 다음 단어를 가져온다. 틀리면 프로그램 종료

# korean_list = ["안녕","잘지내","고마워","사랑해"]
# print("Let's Learning Korean.")
# for word in korean_list:
#     print(word)
#     data = input()
#     if data != word:
#         break


# 문제 4
# 1. 연습할 한국어가 담긴 리스트를 만든다
# 2. 리스트에서 순서대로 단어를 가져와 화면에 출력한다.
# 3. 프로그램 사용자는 단어를 그대로 입력하고
# 문제 3에서 전체 문제 개수 출력, 맞춘 개수 출력, 틀린 개수

# 내가 푼 문제
# korean_words = ["형님","잘지내지","행복하자","사랑한다"]
# pass_words = []
# fail_words = []

# for word in korean_words:
#     print(word)
#     data = input()
#     if word == data:
#         pass_words = pass_words.append(data)
#     else:
#         fail_words = fail_words.append(data)

# print("전체 문제 개수 :", len(korean_words))
# print("맞춘 문제 개수 :", len(pass_words))
# print("틀린 문제 개수 :", len(fail_words))

korean_words = ["형님","잘지내지","행복하자","사랑한다"]
score = 0

for word in korean_words:
    print(word)
    data = input()
    if word == data:
        score += 1

print("총 문제 수", len(korean_words))
print("맞춘 문제 수", score)
print("틀린 문제 수", len(korean_words)-score)