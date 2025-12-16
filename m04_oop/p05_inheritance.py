class Animal:

    def __init__(self, species, habitat):
        self.species = species
        self.habitat = habitat

    def __repr__(self):
        return f"Animal(species={self.species})"

    def __str__(self):
        return f"Animal: {self.species}"

    @staticmethod
    def make_sound():
        print("?")


class Mammal(Animal):

    def __init__(self, species: str, fur: str, legs: int, habitat: str):
        super().__init__(species, habitat)
        self.fur = fur
        self.legs = legs

    def __str__(self):
        return f"Mammal: {self.species}, habitat: {self.habitat}"


class Bird(Animal):

    def __init__(self, species: str, habitat: str, can_fly: bool):
        super().__init__(species, habitat)
        self.can_fly = can_fly


class Dog(Mammal):

    def __init__(self, fur: str, breed: str):
        super().__init__("Dog", fur, 4, "domestic")
        self.breed = breed

    def __str__(self):
        return (f"Dog: fur: {self.fur}, breed: {self.breed}, legs: {self.legs}, "
                f"habitat: {self.habitat}")

    @staticmethod
    def make_sound():
        print("HAF HAF VRRRR")


if __name__ == "__main__":
    dog1 = Dog("long", "shepard")
    print(f"dog1: {dog1}")
    dog1.make_sound()

    print(f"Dog.mro(): {Dog.mro()}")
