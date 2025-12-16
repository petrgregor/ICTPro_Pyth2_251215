import math


class Circle:

    def __init__(self, center: tuple[float, float], radius: float, color: str):
        self.center = center
        self.radius = radius
        self.color = color

    def __repr__(self):
        return f"Circle(center={self.center}, radius={self.radius}, color={self.color})"

    def __eq__(self, other):
        return self.center == other.center and self.radius == other.radius and self.color == other.color

    def __add__(self, other):
        return Circle((self.center[0]+other.center[0], self.center[1]+other.center[1]),
                      self.radius+other.radius,
                      self.color)

    def __sub__(self, other):
        #if self.radius < other.radius:
        if self < other:
            return Circle((0, 0), 0, "white")
        return Circle((self.center[0]-other.center[0], self.center[1]-other.center[1]),
                      self.radius-other.radius,
                      other.color)

    def __lt__(self, other):
        return self.radius < other.radius

    def __len__(self):
        return math.ceil(2 * math.pi * self.radius)


if __name__ == "__main__":
    circle1 = Circle((0, 0), 5, "red")
    circle2 = Circle((1, 2), 3, "blue")
    circle3 = Circle((0, 0), 5, "red")
    print(f"Circle1 = {circle1}")

    if circle1 == circle3:
        print("circle1 == circle3")
    else:
        print(f"Circle1: {id(circle1)}, circle3: {id(circle3)}")

    print(f"circle1 + circle2 = {circle1 + circle2}")
    print(f"circle1 - circle2 = {circle1 - circle2}")

    if circle1 < circle2:
        print("circle1 < circle2")
    elif circle2 < circle1:
        print("circle1 > cirlce2")
    else:
        print("circles has same radius")

    print(f"len(circle1) = {len(circle1)}")

    if circle1:
        print(f"circle1: {circle1}")
