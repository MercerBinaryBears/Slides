class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def add(self, other):
        return Vector(self.x + other.x, self.y + other.y)
    
    def negate(self):
        return Vector(-self.x, -self.y)

    def subtract(self, other):
        return self.add(other.negate())

    def dot(self, other):
        return self.x * other.x + self.y * other.y

    def magnitude(self):
        return (self.dot(self)) ** 0.5

    def cross(self, other):
        return self.x * other.y - self.y * other.x

    def __repr__(self):
        return "{0},{1}".format(self.x, self.y)

v = Vector(1, 0)
w = Vector(0, 1)

print(v.dot(w))
print(v.cross(w))
print(v.add(w))
print(v.negate())
print(v.add(w).magnitude())
