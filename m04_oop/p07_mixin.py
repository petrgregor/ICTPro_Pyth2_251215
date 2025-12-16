class FlyingMixin:

    def fly(self):
        print("I can fly.")


class DriveMixin:

    def drive(self):
        print("I can drive.")


class SailMixin:

    def sail(self):
        print("I can sail.")


class Vehicle:

    def __init__(self, speed: int):
        self.speed = speed


class Car(DriveMixin, Vehicle):

    def __init__(self, speed: int, type: str):
        super().__init__(speed)
        self.type = type

    def __repr__(self):
        return f"Car(speed={self.speed}, type={self.type})"

    def move(self):
        self.drive()


class Train(DriveMixin, Vehicle):

    def __init__(self, speed: int, wagons: int):
        super().__init__(speed)
        self.wagons = wagons

    def __repr__(self):
        return f"Train(speed={self.speed}, wagons={self.wagons})"

    def move(self):
        self.drive()


class Plane(FlyingMixin, Vehicle):

    def __init__(self, speed: int, distance: int):
        super().__init__(speed)
        self.distance = distance

    def __repr__(self):
        return f"Plane(speed={self.speed}, distance={self.distance})"

    def move(self):
        self.fly()


class Ship(SailMixin, Vehicle):

    def __init__(self, speed: int, displacement: int):
        super().__init__(speed)
        self.displacement = displacement

    def __repr__(self):
        return f"Ship(speed={self.speed}, displacement={self.displacement})"

    def move(self):
        self.sail()


class Hydroplane(FlyingMixin, SailMixin, Vehicle):

    def __init__(self, speed: int, distance: int, displacement: int):
        super().__init__(speed)
        self.distance = distance
        self.displacement = displacement

    def __repr__(self):
        return f"Hydroplane(speed={self.speed}, distance={self.distance}, displacement={self.displacement})"

    def move(self):
        self.fly()
        self.sail()


def move(vehicle):
    vehicle.move()


if __name__ == "__main__":
    car1 = Car(150, "SUV")
    print(f"car1: {car1}")
    car1.drive()

    hydroplane1 = Hydroplane(650, 300, 50)
    print(f"hydroplane1: {hydroplane1}")
    hydroplane1.fly()
    hydroplane1.sail()

    print("="*80)
    car1.move()
    print("-"*40)
    hydroplane1.move()

    print("="*80)
    ship1 = Ship(40, 20)
    move(ship1)
    move(car1)
    move(hydroplane1)