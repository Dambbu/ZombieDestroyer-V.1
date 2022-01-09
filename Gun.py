

class Gun:
    def __init__(self, damage, ammo, delay):
        self.damage = damage
        self.ammo = ammo
        self.delay = delay


gun1 = Gun(5, 3, 300)
gun2 = Gun(3, 20, 1400)
gun3 = Gun(6, 50, 1200)
gun4 = Gun(10, 70, 10000)
gun5 = Gun(40, 3, 15000)
gun6 = Gun(100,1, 13000)
gun7 = Gun(150, 10, 14000)

instances = [gun1,gun2,gun3,gun4,gun5,gun6,gun7]




class Level:
    def __init__(self, threshold):
        self.threshold = threshold
