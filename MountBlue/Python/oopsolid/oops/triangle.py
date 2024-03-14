import math


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


class Triangle:
    def __init__(self):
        self.points = []

    def add_point(self, x, y):
        point = Point(x, y)
        self.points.append(point)

    def perimeter(self):
        if len(self.points) != 3:
            return "Invalid triangle: Three points are needed to calculate the perimeter."

        distance1 = math.sqrt((self.points[1].x - self.points[0].x)**2 + (self.points[1].y - self.points[0].y)**2)
        distance2 = math.sqrt((self.points[2].x - self.points[1].x)**2 + (self.points[2].y - self.points[1].y)**2)
        distance3 = math.sqrt((self.points[0].x - self.points[2].x)**2 + (self.points[0].y - self.points[2].y)**2)

        return distance1 + distance2 + distance3

    def is_equal(self, other_triangle):
        if not isinstance(other_triangle, Triangle):
            return False

        return self.points == other_triangle.points

    # Renaming is_equal to __eq__
    def __eq__(self, other_triangle):
        return self.is_equal(other_triangle)


t1 = Triangle()
t1.add_point(0, 0)
t1.add_point(0, 3)
t1.add_point(4, 0)


print("Perimeter of t1:", t1.perimeter())

t2 = Triangle()
t2.add_point(1, 2)
t2.add_point(2, 1)
t2.add_point(1, 5)

print("Perimeter of t2:", t2.perimeter())
print("Are t1 and t2 equal?", t1.is_equal(t2))

t3 = Triangle()
t3.add_point(1, 2)
t3.add_point(2, 1)
t3.add_point(1, 5)

print("t1 == t3:", t1 == t3)
print("t1.is_equal(t3):", t1.is_equal(t3))
print("t3.is_equal(t1):", t3.is_equal(t1))

# Using __eq__ method
print("t1 == t3 (using __eq__):", t1 == t3)
print("t1 == t3 (using __eq__):", t1.__eq__(t3))