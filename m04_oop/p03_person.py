from mypyc.ir.rtypes import bool_rprimitive


class Person:

    def __init__(self, name: str, surname: str, age: int):
        self.name = name
        self.surname = surname
        self.age = age

    def __repr__(self):
        return f"Person(name={self.name}, surname={self.surname}, age={self.age})"

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, age: int):
        if isinstance(age, int) and age >= 0:
            self._age = age
        else:
            raise ValueError("Age must be positive integer.")

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name: str):
        if isinstance(name, str):
            self._name = name.strip().title()
        else:
            raise ValueError("Name must be string.")

    @property
    def surname(self):
        return self._surname

    @surname.setter
    def surname(self, surname: str):
        if isinstance(surname, str):
            self._surname = surname.strip().title()
        else:
            raise ValueError("Surname must be string.")


adam = Person("Adam", "Novák", 12)
print(f"adam: {adam}")
#adam.age = -4  # ValueError: Age must be positive integer.

#borivoj = Person("    borivoj    ", "    svoboda    ", -20)  # ValueError: Age must be positive integer.
borivoj = Person("    borivoj    ", "    svoboda    ", 20)
print(f"borivoj: {borivoj}")
