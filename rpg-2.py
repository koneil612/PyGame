"""
In this simple RPG game, the hero fights the goblin. He has the options to:

1. fight goblin
2. do nothing - in which case the goblin will attack him anyway
3. flee

"""
class Character(object):
    def attack(self, enemy):
        enemy.health -= self.power
    def alive(self):
        if self.health > 0:
            return True
    def print_status(self):
        print "You have %d health and %d power" % (self.health, self.power)

class Hero(Character):
    def __init__(self):
        self.health = 10
        self.power = 5

class Goblin(Character):
    def __init__(self):
        self.health = 6
        self.power = 2
    def print_status(self):
        print "The goblin does %d damage to you." % self.power


# class Zombie(Character):
#     def alive(self):
#         super(Zombie, self).alive:
#             return True

def main():
    goblin = Goblin()
    hero = Hero()
    # zombie = Zombie()
    # while goblin.health > 0 and hero.health > 0:
    while goblin.alive() and hero.alive():
        hero.print_status()
        goblin.print_status()

        print "What do you want to do?"
        print "1. fight goblin"
        print "2. do nothing"
        print "3. flee"
        print "> ",
        input = raw_input()
        if input == "1":
            # ***hero attacks goblin calling from the attack function in hero
            hero.attack(goblin)
            # zombie.attack(hero)
            if not goblin.alive():
                print "The goblin is dead."
        elif input == "2":
            pass
        elif input == "3":
            print "Goodbye."
            break
        else:
            print "Invalid input %r" % input

        if goblin.alive():
            # Goblin attacks hero. calling from the attack function in goblin
            goblin.attack(hero)
            print "The goblin does %d damage to you." % goblin.power
            if not hero.alive():
                print "You are dead."

main()
