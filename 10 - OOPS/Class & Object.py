'''
here we are creating a class which is a blueprint for making an object
'''
class character:
    def __init__(self, name, attack, health, blood):
        self.name = name
        self.health = health
        self.attack = attack
        self.blood = blood

    def attack_enemy(self):
        print(f'{self.name} attacked with a power {self.attack} and opponent drew his {self.blood} Blood')

'''
using the above class, ill now create characters as Object 'thor','ironman','hulk'
'''
thor = character('Thor', 25, 100, 'White')
ironman = character('ironman', 30, 98, 'Red')
hulk = character('hulk', 15, 95, 'Green')

thor.attack_enemy()
ironman.attack_enemy()
hulk.attack_enemy()