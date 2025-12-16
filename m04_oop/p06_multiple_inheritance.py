class Bat:

    def __init__(self, sonar=2):
        self.sonar = sonar

    def __repr__(self):
        return f"Bat(sonar={self.sonar})"

    def __lt__(self, other):
        return self.sonar < other.sonar

    @staticmethod
    def fly():
        print("Já si létám, já se vznáším.")


class Man:

    def __init__(self, name: str, height: int = 180):
        self.name = name
        self.height = height

    def __repr__(self):
        return f"Man(name={self.name})"

    def __lt__(self, other):
        return self.height < other.height

    @staticmethod
    def run():
        print("Utíkám.")


class Batman(Bat, Man):  # zde záleží na pořadí při hledání děděných funkcí

    def __init__(self, name: str, sonar=5, height: int = 150):
        Bat.__init__(self, sonar)
        Man.__init__(self, name, height)

    def __repr__(self):
        return f"Batman(name={self.name}, sonar={self.sonar}, height={self.height})"

    @staticmethod
    def make_batman(bat, man):
        return Batman(man.name, bat.sonar)


if __name__ == "__main__":
    bat1 = Bat()
    print(f"bat1: {bat1}")

    man1 = Man("Robert")
    print(f"man1: {man1}")

    batman = Batman("Vladimír")
    print(f"batman: {batman}")
    batman.fly()
    batman.run()

    batman1 = Batman.make_batman(bat1, man1)
    print(f"batman1: {batman1}")

    print(f"bat < batman: {bat1 < batman}")
    batman.height = 190
    batman.sonar = 4
    print(f"man1 < batman: {man1 < batman}")

    batman2 = Batman("Martin", 1, 200)
    print(f"batman: {batman}, batman2: {batman2}")
    print(f"batman < batman2: {batman < batman2}")

    print(f"Batman.mro: {Batman.mro()}")
    # [<class '__main__.Batman'>, <class '__main__.Bat'>, <class '__main__.Man'>, <class 'object'>]
