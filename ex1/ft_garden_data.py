class Plant:
    def __init__(self, name: str, height: int, age: int):
        self.name = name
        self.height = height
        self.age = age


def ft_garden_data():
    print("=== Garden Plant Registry ===")
    names = ["Rose", "Sunflower", "Cactus"]
    heights = [25, 80, 15]
    ages = [30, 45, 120]
    for i in range(3):
        p = Plant(names[i], heights[i], ages[i])
        print(f"{p.name}: {p.height}cm, {p.age} days old")


if __name__ == "__main__":
    ft_garden_data()
