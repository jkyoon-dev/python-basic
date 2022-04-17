# 2. 로또 번호 6개, 로또 번호는 1~45, 6개 숫자 모두 달르게, getRandomNumber() 함수 사용 구현

import random
def getRandomNumber():
    number = random.randint(1, 45)
    return number
