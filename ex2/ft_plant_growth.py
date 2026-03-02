class Plant:
    def __init__(self, name, height, plant_age):
        self.name = name
        self.height = height
        self.plant_age = plant_age

    def grow(self):
        self.height += 6
        
    def age(self):
        self.plant_age += 6

    def get_info(self):
        print(f"{self.name}: {self.height}cm, {self.plant_age} days old")


def ft_plant_growth():
    p = Plant("Rose", 25, 30)
    print(f"=== Day 1 ===")
    p.get_info()
    print(f"=== Day 7 ===")
    p.grow()
    p.age()
    p.get_info()
    print(f"Growth this week: +6cm")


if __name__ == "__main__":
    ft_plant_growth()
