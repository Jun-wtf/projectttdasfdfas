# Made IN Korea
class Roblox:
    def __init__(self, name, r, color, sex):
        self.name = name
        self.r = r
        self.color = color
        self.Gender = Gender
    def print_info(self):
        print(f"system : 당신의 이름은... {self.name} 입니다.")
        print(f"system : {self.name}님의 r 버전은 {self.r} 입니다.")
        print(f"system : {self.name}님의 몸의 색은 {self.color}입니다.")
        print(f"system : {self.name}님의 성별은 {self.sex} 입니다.")
    # def __del__(self):
    #     print(f"Server : {self.name}님 이/가 삭재되었습니다.")
# [name] = Roblox('[name]', '[r6 / r15]', '[color]', '[Gender]')
# [name].print_info()
Owner = Roblox('HD', '6', 'black', 'man')

Owner.print_info()
