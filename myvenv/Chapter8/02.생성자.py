# 클래스
# 속성 체력 공격력 이동속도
# 메서드 동작

class Monster:
    # 1 인스턴스를 만들때 반드시 호출되는 메서드 가장먼저 호출되는 메서드라 init
    # 2 self는 매개변수로 치지 않는다.
    # self 인스턴스 자기 자신
    # 3 속성값을 저장해라
    def __init__(self, health, attack, speed):
        self.health = health
        self.attack = attack
        self.speed = speed
    def decrease_health(self, num):
        self.health = self.health - num
    def get_health(self):
        return self.health

# 고블린 인스턴스
goblin = Monster(800, 120, 300)# 인스턴스 생성 시점 => Monster 클래스 이름을 쓰고() 이 시점에 ()안에 들어가는 데이터들은 init 메서드의 인자 매개변수
goblin.decrease_health(100)
print(goblin.get_health())