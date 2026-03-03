class Plant:
    def __init__(self, name: str, height: int, age: int) -> None:
        self.name = name
        self.height = height
        self.age = age

    def display(self) -> None:
        print(f"Created: {self.name} ({self.height}cm, {self.age} days)")


if __name__ == "__main__":
    names = ["Rose", "Oak", "Cactus", "Sunflower", "Fern"]
    heights = [25, 200, 5, 80, 15]
    ages = [30, 365, 90, 45, 120]
    print("=== Plant Factory Output ===")
    for i in range(5):
        p = Plant(names[i], heights[i], ages[i])
        p.display()
    print()
    print(f"Total plants created: {i + 1}")
