
class tanks:
    country = ""
    name = ""
    hp = 0   # Прочность
    dmg = 0  # Урон

    def __init__(self, country_, name_):
        self.country = country_
        self.name = name_


    def add_hp(self, increase):
        self.hp += increase


    def add_dmg(self, incr):
        self.dmg += incr

    def in_game(self):
        print(f"In Game {self.name} from {self.country}")



t1 = tanks("rus", "T-90M «Прорыв»")
t1.add_hp(90)
t1.add_dmg(30)

t2 = tanks("ger","Leopard" )
t2.add_hp(60)
t2.add_dmg(20)

t3 = tanks("usa","M1 Abrams" )
t3.add_hp(50)
t3.add_dmg(10)

t1.in_game()
print(f"{t1.hp = },{t1.dmg = }")
print("**********************")
t2.in_game()
print(f"{t2.hp = },{t2.dmg = }")
print("**********************")
t3.in_game()
print(f"{t3.hp = },{t3.dmg = }")