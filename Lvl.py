#Class Lvl
class Lvl:
    def __init__(self, lvl, type, zombies, coins):
          self.type = type
          self.lvl = lvl
          self.zombies = zombies
          self.coins = coins

p1 = Lvl("Lvl 1", 1, 20, 20)
p2 = Lvl("Lvl 2", (1,2), (15,5), 30)
p3 = Lvl("Lvl 3", (1,2), (15,10), 45)

instances = [p1,p2,p3]
for instance in instances: 
    print(str(instance.type) + "," + instance.lvl + "," + instance.zombies + "," + instance.coins)




# The code here is wrong. I tried to group the two zombie and type factors together except they didn't work out...






#    p4 = Lvl("Lvl",)
#    p5 = Lvl("Lvl",)
#    p6 = Lvl("Lvl",)
#    p7 = Lvl("Lvl",)
#    p8 = Lvl("Lvl",)
#    p9 = Lvl("Lvl",)
#    p10 = Lvl("Lvl",)
#    p12 = Lvl("Lvl",)
#    p13 = Lvl("Lvl",)
#    p14 = Lvl("Lvl",)
#    p15 = Lvl("Lvl",)
#    p16 = Lvl("Lvl",)
#    p17 = Lvl("Lvl",)
#    p18 = Lvl("Lvl",)
#    p19 = Lvl("Lvl",)
#   p20 = Lvl("Lvl",)
#    p21 = Lvl("Lvl",)
#    p22 = Lvl("Lvl",)
#    p23 = Lvl("Lvl",)
#    p24 = Lvl("Lvl",)
#    p25 = Lvl("Lvl",)
#    p26 = Lvl("Lvl",)
#    p27 = Lvl("Lvl",)
#    p28 = Lvl("Lvl",)
#    p29 = Lvl("Lvl",)
#    p30 = Lvl("Lvl",)