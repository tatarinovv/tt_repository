class Vector:
    def __init__(self, x, y=None, z=None):
        if isinstance(x, str):
            x, y, z = map(float, x.strip('{}').split(','))
        assert isinstance(x, (int, float)) and isinstance(y, (int, float)) and isinstance(z, (int, float))
        self.x, self.y, self.z = x, y, z

    def __repr__(self):
        return f"Vector({self.x}, {self.y}, {self.z})"

    def __abs__(self):
        return (self.x**2 + self.y**2 + self.z**2) ** 0.5

    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y, self.z + other.z)

    def __sub__(self, other):
        return Vector(self.x - other.x, self.y - other.y, self.z - other.z)

    def __mul__(self, other):
        if isinstance(other, (int, float)):
            return Vector(self.x * other, self.y * other, self.z * other)
        return self.x * other.x + self.y * other.y + self.z * other.z

v1 = Vector(1, 2, 3)
v2 = Vector("{4, 5, 6}")

print(v1 + v2)  # Vector(5, 7, 9)
print(v1 - v2)  # Vector(-3, -3, -3)
print(v1 * v2)  # 32 (скалярное произведение)
print(v1 * 3)   # Vector(3, 6, 9)
print(abs(v1))  # 3.7416573867739413 (модуль вектора)