"""
Definujeme třídu Person, která reprezentuje člověka.
"""


class Person:
    # name: str = ""
    # surname: str = ""
    # age: int = None

    # Konstuktor
    def __init__(self, name: str, surname: str, age: int):
        # print(f"Vytvářím objekt třídy Person.")
        self.name = name
        self.surname = surname
        self.age = age

    # "Technický" výpis pro programátora
    def __repr__(self):
        return f"Person(name={self.name}, surname={self.surname}, age={self.age})"

    # Lidsky čitelný výpis pro koncového uživatele
    def __str__(self):
        return f"{self.name} {self.surname} ({self.age} let)"

    def __len__(self):
        return self.age

    def to_string(self):
        return f"Jméno: {self.name}, příjmení: {self.surname}, age: {self.age}"


person = Person("Adam", "Bernau", 12)
print(f"person.name = {person.name}")
# person.name = "Adam"
# person.surname = "Bernau"
# person.age = 12
print(f"person = {person}")
print(f"person.__repr__ = {person.__repr__()}")
print(f"person.to_string() = {person.to_string()}")
print(f"Person: name={person.name}, surname={person.surname}, age={person.age}")

person1: str = str(person)
print(f"type(person1): {type(person1)}")
print(f"person1 = {person1}")

# Můžeme atributy vytvářet i za běhu => není to dobrá praxe!
person.height = 153
print(f"person.height = {person.height}")

person2 = Person("Bedřich", "Smetana", 64)
print(f"person = {person}")  # __str__
print(f"person2 = {person2}")  # __str__
persons = [person, person2]
print(f"persons = {persons}")  # __repr__ (objekty jsou vnořené)
for person_ in persons:
    print(person_)
print("-"*80)
list(map(print, persons))
print('-'*80)
print(*persons, sep="\n")
print("="*80)
print(f"len(person) = {len(person)}")

# del person
# print(f"person = {person}")  # NameError: name 'person' is not defined. Did you mean: 'Person'?
