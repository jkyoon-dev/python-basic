import random
# 부모 클래스
class Monster():
    def __init__(self, name, health, attack):
        self.name = name
        self.health = health
        self.attack = attack
    def move(self):
        print(f"[{self.name}] 지상에서 이동하기")

# 자식 클래스
class Wolf(Monster):
    pass

class Shark(Monster):
    def move(self):
        print(f"[{self.name}] 헤엄치기")

# 드레곤만 스킬
class Dragon(Monster):
    # 생성자 오버라이딩
    def __init__(self, name, health, attack, skills):
        super().__init__(name, health, attack)
        self.skills = ("불뿜기", "꼬리치기", "날개치기")

    def move(self):
        print(f"[{self.name}] 날기")

    def skill(self):
        print(f"[{self.name}] 스킬 사용 {self.skills[random.randint(0,2)]}")
wolf = Wolf("울프", 1500, 200)
wolf.move()

shark = Shark("샤크", 3000, 300)
shark.move()

# 스킬은 고정된 값이니 튜플로
dragon = Dragon("드레곤", 5000, 500)
dragon.move()
dragon.skill()