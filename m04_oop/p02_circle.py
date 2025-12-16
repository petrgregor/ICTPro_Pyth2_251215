import math


class Circle:

    def __init__(self, center: tuple[float, float], radius: float, color: str):
        self.center = center
        self.radius = radius
        #self.set_radius(radius)
        self.color = color

    def __repr__(self):
        return f"Circle(center={self.center}, radius={self.radius}, color={self.color})"

    def __eq__(self, other):
        return (self.center == other.center and self.radius == other.radius
                and self.color == other.color)

    def __add__(self, other):
        return Circle((self.center[0]+other.center[0], self.center[1]+other.center[1]),
                      self.radius+other.radius,  # new radius
                      self.color)                # new color

    def __sub__(self, other):
        #if self.radius < other.radius:
        if self < other:
            return Circle((0, 0), 0, "white")
        return Circle((self.center[0]-other.center[0], self.center[1]-other.center[1]),
                      self.radius-other.radius,
                      other.color)

    def __lt__(self, other):
        return self.radius < other.radius

    """def __gt__(self, other):
        return super().__gt__(other)"""

    def __len__(self):
        return math.ceil(2 * math.pi * self.radius)

    @property  # geeter
    def center(self):
        return self._center

    @center.setter
    def center(self, center: tuple[float, float]):
        if ((isinstance(center[0], float) or isinstance(center[0], int))  # x coordinate
                and (isinstance(center[1], float) or isinstance(center[1], int))):  # y coordinate
            self._center = center
        else:
            raise ValueError("Center must be defined as tuple of floats.")

    @property
    def radius(self):
        return self._radius

    @radius.setter
    def radius(self, radius: float):
        if (isinstance(radius, float) or isinstance(radius, int)) and radius >= 0:
            self._radius = radius
        else:
            raise ValueError("Radius can not be negative.")

    """def get_radius(self):
        return self.radius

    def set_radius(self, radius):
        if radius < 0:
            raise ValueError("Radius can not be negative.")
        self.radius = radius"""

    @classmethod
    def circle_from_string(cls, string: str) -> Circle:
        # string = x, y, r, color
        items = string.split(",")  # list: [x, y, r, color]
        return Circle((float(items[0]), float(items[1])), float(items[2]), items[3])

    @staticmethod
    def count_circumference(radius):
        return 2 * math.pi * radius


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

    circle4 = Circle.circle_from_string("5, 3, 8, green")
    print(f"circle4 = {circle4}")

    print(f"Circumference = {Circle.count_circumference(5)}")

    circle5 = Circle((1, 5), 5, "blue")
    # circle5.radius = -7  # ValueError: Radius can not be negative.
    print(f"circle5: {circle5}")
    #circle5.set_radius(-10)  # ValueError: Radius can not be negative.
    print(f"circle5: {circle5}")

    #circle6 = Circle(("a", "b"), 5, "yellow")  # ValueError: Center must be defined as tuple of
                                                # floats.
    #print(f"circle6 = {circle6}")
    #circle6._center = ("a", "b")

    circle5.radius = 3
    #circle5._radius = -2
    print(f"circle5: {circle5}")
