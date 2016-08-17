import math

class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        
        # add theta, so we can sort by it later
        self.theta = math.atan2(y, x)

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
        # update format, so we can just print the vectors
        return "({0},{1})".format(self.x, self.y)

def parse_point(raw_string):
    x,y = map(int, raw_string.split(','))
    return Vector(x, y)

def turn_direction(p1, p2, p3):
    d1 = p2.subtract(p1)
    d2 = p3.subtract(p1)

    return d1.cross(d2)

def convex_hull(points):
    # first get the point with min y value
    

    # first, sort the points by their angle theta
    sorted_points = sorted(points, key=lambda P : P.theta)

    N = len(points)

    hull = sorted_points

    for i in range(0, N + 1):
        current_point = sorted_points[i % N]
        previous_point = sorted_points[(i + N - 1) % N]
        next_point = sorted_points[(i + 1) % N]

        print(current_point, turn_direction(previous_point, current_point, next_point))
        if turn_direction(previous_point, current_point, next_point) >= 0:
            hull.append(current_point)

    return hull

point_count = int(input().strip())
points = []
for i in range(point_count):
    points.append(parse_point(input()))

hull = convex_hull(points)

# Resort the hull, so the we get the 

print(hull)
