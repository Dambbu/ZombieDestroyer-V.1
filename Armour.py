#Class Armour
class Armour:
    def __init__(self, type, hp):
        self.type = type
        self.hp = hp

p1 = Armour("Basic", )
p2 = Armour("Noob")
p3 = Armour("Pro")
instances = [p1,p2,p3]
for instance in instances: 
    print(str(instance.type) + "," + instance.hp )





