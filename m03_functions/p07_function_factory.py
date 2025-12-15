def make_multiplier(factor: int):

    def multiplier(number: int):
        return number * factor

    return multiplier


double = make_multiplier(2)
triple = make_multiplier(3)
multiplier10 = make_multiplier(10)

print(double(10))
print(triple(10))
print(multiplier10(50))
