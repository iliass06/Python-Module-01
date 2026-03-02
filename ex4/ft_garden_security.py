class SecurePlant:
    def __init__(self, name: str, height: int, age: int) -> None:
        self.name = name
        self.__height = height
        self.__age = age

    def set_height(self, h):
        if h >= 0:
            self.__height = h
        else:
            print(f"Invalid operation attempted: height {h}cm [REJECTED]")
            print("Security: Negative height rejected")

    def set_age(self, a):
        if a >= 0:
            self.__age = a
        else:
            print(f"Invalid operation attempted: age {a} days [REJECTED]")
            print("Security: Negative age rejected")

    def get_height(self):
        return self.__height

    def get_age(self):
        return self.__age


def ft_garden_security():
    print("=== Garden Security System ===")
    p = SecurePlant("Rose", 0, 0)
    print(f"Plant created: {p.name}")
    p.set_height(25)
    print(f"Height updated: {p.get_height()}cm [OK]")
    p.set_age(30)
    print(f"Age updated: {p.get_age()} days [OK]")
    print()
    p.set_height(-5)
    print()
    print(f"Current plant: {p.name} ({p.get_height()}cm, {p.get_age()} days)")

if __name__ == "__main__":
    ft_garden_security()
