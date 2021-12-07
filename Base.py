#Class Base
class Base:
    def __init__(self, type, hp, speed):
        self.type = type
        self.hp = hp
        self.speed = speed

p1 = Base("The Craker,", 105, 8)
p2 = Base("The Ninja", 110, 9)
p3 = Base("The The Warrior", 115, 8)
p4 = Base("The Magician", 120, 10)
p5 = Base("The Berserker", 135, 11)
p6 = Base("Kamakazier", 150, 14)
p7 = Base("The Tank ", 175, 4)
p8 = Base("The Viking", 200, 16)

instances = [p1,p2,p3,p4,p5,p6,p7,p8]
for instance in instances: 
    print(str(instance.type) + "," + instance.hp + "," + instance.speed )


