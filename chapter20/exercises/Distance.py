class Distance:
    def __init__(self, value=0):
        self.value = value

    def __add__(self, other):
        new_value = self.value + other.value
        return Distance(new_value)

    def __sub__(self, other):
        new_value = self.value - other.value
        return Distance(new_value)

    def __truediv__(self, amount):
        new_value = self.value / amount
        return Distance(new_value)

    def __floordiv__(self, amount):
        new_value = self.value // amount
        return Distance(new_value)

    def __mul__(self, amount):
        new_value = self.value * amount
        return Distance(new_value)

    def __str__(self):
        return 'Distance[' + str(self.value) + ']'


d1 = Distance(6)
d2 = Distance(3)

print( d1 + d2)
print (d1 - d2)
print (d1 / 2)
print(d2 // 2)
print(d2 * 2)
