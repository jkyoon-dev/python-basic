# 리스트 기차에 비유
animals = ["사자","호랑이","고양이","강아지"]
# print(animals[0])
# 데이터 조작하기
# 추가 append
# 할당
# 삭제 del del animals[1]
# b = [3,4,2,1]
# 슬라이싱
# print(b[1:3])
# 리스트 길이 len(리스트)
# 정렬 .sort

# 데이터 접근하기
# print(animals[0])
# print(animals[-1]) # 젤 끝 요소에 접근 (많이 쓰임)

# 데이터 추가하기
# animals.append("고라니")
# print(animals)

# 데이터 할당하기
# animals[1] = "청개구리"
# print(animals)

# 데이터 삭제하기
# del animals[0]
# print(animals)

# 리스트 슬라이싱
print(animals)
print(animals[1:3]) # [시작 인덱스:끝 인덱스 +1]
print(animals[:]) # 전체
print(animals[:3])
print(animals[1:])

# 리스트 길이
print(len(animals))

# 정렬
animals.sort() # 오름차순
print(animals)
animals.sort(reverse=True) # 내림차순
print(animals)