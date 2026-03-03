class Plant:
    def __init__(self, name: str, height: int, plant_age: int) -> None:
        self.name = name
        self.height = height
        self.plant_age = plant_age

    def grow(self) -> None:
        self.height += 6

    def age(self) -> None:
        self.plant_age += 6

    def get_info(self) -> None:
        print(f"{self.name}: {self.height}cm, {self.plant_age} days old")


if __name__ == "__main__":
    p = Plant("Rose", 25, 30)
    print("=== Day 1 ===")
    p.get_info()
    print("=== Day 7 ===")
    p.grow()
    p.age()
    p.get_info()
    print("Growth this week: +6cm")
