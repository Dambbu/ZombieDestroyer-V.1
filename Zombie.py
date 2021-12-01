
#Class Zombie
class Zombie:
    def __init__(self, type, hp, speed, money):
        self.type = type
        self.speed = speed
        self.hp = hp
        self.money = money

p1 = Zombie("Type 1", 3, 6, 1)
p2 = Zombie("Type 2", 9, 4, 3)
p3 = Zombie("Type 3", 12, 5, 5)
p4 = Zombie("Type 4", 16, 7, 10)
p5 = Zombie("Type Boss 1", 30, 6, 20)
p6 = Zombie("Type Boss 2", 45, 6, 30)
p7 = Zombie("Type Boss 3", 60, 5, 45)
p8 = Zombie("Type Mega Boss 1", 100, 5, 80)
p9 = Zombie("Type Mega Boss 2", 150, 4, 130)
p10 = Zombie("Type Heavy Boss 1", 300, 4, 280)
p11 = Zombie("Type Extreme Heavy Boss", 800, 3, 780)
p12 = Zombie("Type Fast Boss", 100, 6, 80)

instances = [p1,p2,p3,p4,p5,p6,p7,p8,p9,p10,p11,p12]
for instance in instances: 
    print(str(instance.type) + "," + instance.hp + "," + instance.speed + "," + instance.money)