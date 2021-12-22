from Gun import Gun
from ZombieType import ZombieType

class Zombie:
    def __init__(self, zombieType:ZombieType, x, y):
        self.x = x
        self.y = y
        self.hp=zombieType.hp
        self.speed = zombieType.speed
        self.zombieImageName = zombieType.type
        self.coin = zombieType.money
        self.isXForward = True
        self.isYForward = True
        self.damage = zombieType.damage

        