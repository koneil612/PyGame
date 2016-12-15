class Animal(object):
    def breed(self):
        return Animal()
    def makeNoise(self):
        print "I am an animal"

class Dog(Animal):
    def makeNoise(self):
        print "Woof"
    def breed(self):
        return Dog()

class Cat(Animal):
    def makeNoise(self):
        print "Meow"
    def breed():
        return Cat()

class Pomeranian(Dog):
    def woof(self):
        print "woof woof woof woofwoofwoof"

class EagerDog(Dog):
    def woof(self):
        Dog.woof(self)
        Dog.woof(self)

c = Cat()
d = Dog()
c.makenoise()
d.makeNoise()
p = Pomeranian
p.woof()

# kitten = c.breed()
# kitten.makeNoise()
# puppy = d.breed()
# puppy.makeNoise()
