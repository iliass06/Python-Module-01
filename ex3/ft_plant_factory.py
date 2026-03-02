class Plant:
    def __init__(self, name, height, age):
        self.name = name
        self.height = height
        self.age = age

    def display(self):
        print(f"Created: {self.name} ({self.height}cm, {self.age} days)")


def ft_plant_factory():
    names = ["Rose", "Oak", "Cactus", "Sunflower", "Fern"]
    heights = [25, 200, 5, 80, 15]
    ages = [30, 365, 90, 45, 120]
    print("=== Plant Factory Output ===")
    for i in range(5):
        p = Plant(names[i], heights[i], ages[i])
        p.display()
    print()
    print(f"Total plants created: {i + 1}")


if __name__ == "__main__":
    ft_plant_factory()
