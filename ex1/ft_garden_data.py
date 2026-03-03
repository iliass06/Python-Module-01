class Plant:
    def __init__(self, name: str, height: int, age: int) -> None:
        self.name = name
        self.height = height
        self.age = age


if __name__ == "__main__":
    print("=== Garden Plant Registry ===")
    names = ["Rose", "Sunflower", "Cactus"]
    heights = [25, 80, 15]
    ages = [30, 45, 120]
    for i in range(3):
        p = Plant(names[i], heights[i], ages[i])
        print(f"{p.name}: {p.height}cm, {p.age} days old")
