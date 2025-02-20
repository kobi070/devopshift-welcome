from dataclasses import dataclass


@dataclass
class Animal():
    legs : int = 4
    def make_sound(self):
        print("im an animal")
@dataclass
class Mammel(Animal):
    gender: str = 'male'
@dataclass
class Dog(Mammel):
    name: str = "Dog"
    legs: int = 4
    def make_sound(self):
        print("Bark")
@dataclass
class Human(Mammel):
    name: str = "Human"
    legs: int = 2
    def make_sound(self):
        print("Hello World !")