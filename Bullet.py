class Bullet:
    def __init__(self, amo):
        self.amo = amo


bullet1 = Bullet(3)
bullet2 = Bullet(2)
bullet3 = Bullet(15)

instances = [bullet1, bullet2, bullet3]
for instance in instances: 
    print(str(instance.type) + "," + instance.hp + "," + instance.speed )
