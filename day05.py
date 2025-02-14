class Pokemon:
    def __init__(self, name):
        self.name = name
        print(f"{name} 포켓몬스터 생성")

    def attack(self,target):
        print(f"{self.name}이(가) {target.name}을(를) 공격!")

class Pikachu(Pokemon):
    def __init__(self, name, type):
        super().__init__name()
        #self.name = name
        self.type = type

    def attack(self,target):
        print(f"{self.name}이(가) {target.name}을(를) {self.type} 공격!")

    def electric_info(self):
        print("전기 계열의 공격을 합니다")

charizard = Pokemon("리자몽")
pikachu = Pokemon("피카츄")
squirtle = Pokemon("꼬부기")
charizard.attack(squirtle)