# 아이템 공통: 속성(이름, 가격, 무게,) 메서드(판매하기, 버리기)
# 장비 아이템 : 착용효과, 착용하기
# 소모품 아이템 : 사용효과, 사용하기
# (단, 버리기는 버릴 수 있는 아이템만 가능하다)

# 구성안과 설계도를 보고 클래스를 코드로 완성해보자.
# 메서드 구현은 자유롭게 한다.
# Wearable 장비
# Usable 소모품

# 인스턴스 사용
# sword
# potion

class Item:
    def __init__(self, name, price, weight, isdropable):
        self.name =name
        self.price =price
        self.weight= weight
        self.isdropable =isdropable

    def sale(self):
        print(f"[{self.name}]을(를) [{self.price}]에 판매했습니다.")

    def drop(self):
        if self.isdropable:
            print(f"[{self.name}]을(를) 버릴 수 있습니다.")
        else:
            print(f"[{self.name}]을(를) 버릴 수 없습니다.")

class WearableItem(Item):
    # 생성자 초기화
    def __init__(self, name, price, weight, isdropable, skill):
        super().__init__(name, price, weight, isdropable)
        self.skill = skill

    def wear(self):
        print(f"[{self.name}]을(를) 착용했습니다. [{self.skill}]")
























class UsableItem(Item):
    def __init__(self, name, price, weight, isdropable, skill):
        super().__init__(name, price, weight, isdropable)
        self.skill = skill

    def use(self):
        print(f"[{self.name}]을(를) 사용했습니다. [{self.skill}]")

# 인스턴스 생성
sword = WearableItem("왕검", 100000, 100, False, "공격력 + 100, 귀속탬")
sword.wear()
sword.sale()
sword.drop()

posion = UsableItem("힐링포션", 100000, 100, True, "HP + 100")
posion.use()
posion.sale()
posion.drop()





































# class Item:
#     def __init__(self, name, price, weight, isdropable):
#         self.name = name
#         self.price = price
#         self.weight = weight
#         self.isdropable = isdropable

#     def sale(self):
#         print(f"[{self.name}] 판매 가격은 {self.price} 입니다.")
#     def discard(self):
#         if self.isdropable:
#             print(f"[{self.name}]을(를) 버렸습니다.")
#         else:
#             print(f"[{self.name}]을(를) 버릴 수 없습니다.")

# class WearableItem(Item):
#     # 챡용효과 추가 속성 필요해서 생성자함수 초기화
#     def __init__(self, name, price, weight, isdropable, effect):
#         super().__init__(name, price, weight, isdropable)
#         self.effect = effect
#     def wear(self):
#         print(f"[{self.name}] 착용했습니다. [{self.effect}]")

# class UsableItem(Item):
#     # 사용효과 추가 속성 필요해서 생성자함수 초기화
#     def __init__(self, name, price, weight, isdropable, effect):
#         super().__init__(name, price, weight, isdropable)
#         self.effect = effect
#     def use(self):
#         print(f"[{self.name}] 착용했습니다. [{self.effect}]")

# sword = WearableItem("뭘까나ㅋㅋ", 100000, 200, False, "공격력 50 추가, 공격속도 감소")
# sword.wear()
# sword.discard()
# sword.sale()

# potion = UsableItem("힐링포션", 300, 10, True, "HP 1000을 회복합니다.")
# potion.use()
# potion.discard()
# potion.sale()



