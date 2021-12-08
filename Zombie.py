from ZombieType import ZombieType

class Zombie():
    def __init__(self, zombieType:ZombieType, x, y):
        self.x = x
        self.y = y
        self.hp=zombieType.hp
        self.speed = zombieType.speed
        self.zombieImageName = zombieType.type
        self.isXForward = True
        self.isYForward = True
