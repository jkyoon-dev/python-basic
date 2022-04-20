# 클래스를 사용하는 이유
champion1_name = "이즈리얼"
champion1_health = 700
champion1_attack = 90

print(f"{champion1_name}님 소환사의 협곡에 오신것을 환영합니다.")

champion2_name = "리신"
champion2_health = 800
champion2_attack = 100

print(f"{champion2_name}님 소환사의 협곡에 오신것을 환영합니다.")

champion3_name = "야수오"
champion3_health = 700
champion3_attack = 70

print(f"{champion3_name}님 소환사의 협곡에 오신것을 환영합니다.")

def basic_attack(name, attack):
    print(f"{name} 기본공격 {attack}")

basic_attack(champion1_name, champion1_attack)
basic_attack(champion2_name, champion2_attack)
basic_attack(champion3_name, champion3_attack)


print("================클래스를 사용한 경우================")

# class 클래스이름:
#     def 메서드이름(self):
#         명령블록

class Monster:
    def say(self):
        print("나는 몬스터다")

# class 호출
# 인스턴스 = 클래스이름()
# 인스턴스.메서드()

goblin = Monster() # 고블린 객체
goblin.say()


class monster:
    def say(self):
        print("나는 몬스터다!")

goblin = monster() # 인스턴스 변수에 담아줌
goblin.say()


# 파이썬은 자료형도 클래스다

a = 10
b = "문자열객체"
c = True

print(type(a)) # 클래스 int형
print(type(b)) # 클래스 문자형
print(type(c)) 

print(b.__dir__()) # 문자형에서 사용할 수 있는 메서드

# 클래스 만들때 2가지 필요
# 속성 :특징
# 메서드 : 동작

# Monster 클래스에 속성을 추가
class Monster:
    #__init__ 메서드 : 인스턴스를 만들때 반드시 호출되는 메서드
    # 가장먼저 호출되는 메서드라 init
    def __init__(self, health, attack, speed):
        # self 란 인스턴스 자기 자신
        self.health = health
        self.attack = attack
        self.speed = speed
# 몬스터 클래스가 호출 될 때 () init 메서드를 호출되고 매개변수로 들어가게 됨
goblin = Monster(800,120,300)
wolf = Monster(1500,200,350)













# 생성자 __init__(self,)
#: 인스턴스를 만들 때 호출되는 메서드

class Monster:
    # 몬스터 클래스 만들때 넘겨주는 3가지 데이터
    def __init__(self, health, attack, speed):
        # self : 인스턴스 자기 자신의
        self.health = health
        self.attack = attack
        self.speed = speed
    # 메서드 생성 
    # 1 체력 감소하기
    def decrease_health(self, num):
        self.health -= num
    # 2 체력 가져오기
    def get_health(self):
        print(self.health)
        return self.health



# 고블린 인스턴스 생성
# goblin = Monster()
# 클래스 설계도를 참고해서 객체를 만든다 health, attack, speed
goblin = Monster(800, 120, 300) # 고블린 인스턴스
# 고블린 메서드 사용
goblin.decrease_health(100)
# goblin.get_health()
print(goblin.get_health())

# 늑대 인스턴스 생성
wolf = Monster(1500, 200, 350)
# 속성 추가는 init 함수 안에 인자를 넘겨주는 방식으로 추가한다.
# wolf 인스턴스에 .을 찍으면 메서드를 사용할 수 있음
wolf.decrease_health(100)
wolf.get_health()
print(wolf.get_health())