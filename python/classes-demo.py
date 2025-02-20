class Animal:
    legs = 4

    def make_sound(self):
        print("im an animal")
class Mamal(Animal):
    def __init__(self, gender="females"):
        self.gender = gender
    def make_sound(self):
        print("Mamal sound")

class Dog(Mamal):
    def __init__(self, name, legs):
        super(self).__init__(name)
        self.name = name
        self.legs = legs
    
    def make_sound(self):
        print("Bark")

class Human(Mamal):
    def __init__(self, name, legs):
        self.name = name
        self.legs = legs

    def make_sound(self):
        print("Hello World !")

