# 1. 세개 정수를 인자로 받아 합계 60 평균 20이 나오도록 함수를 정의해보자

from calendar import c

# 문자열 포매팅
def sumAvg(a,b,c):
    # docstring: 설명문
    """
    세수의 합과 평균
    """
    sum = a+b+c
    avg = int(sum/3)
    # print("합계:", sum)
    # print("평균:", avg)
    print(f"합계 : {sum} 평균 : {avg}")
    
sumAvg(20,20,20)