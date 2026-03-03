class Plant:
    def __init__(self, name: str, height: int, age: int) -> None:
        self.name = name
        self.height = height
        self.age = age

    def get_common_info(self) -> str:
        return f"{self.height}cm, {self.age} days"


class Flower(Plant):
    def __init__(self, name: str, height: int, age: int, color: str) -> None:
        super().__init__(name, height, age)
        self.color = color

    def bloom(self) -> None:
        print(f"{self.name} is blooming beautifully!")

    def display_info(self) -> None:
        print(f"{self.name} (Flower): {self.get_common_info()}"
              f", {self.color} color")


class Tree(Plant):
    def __init__(self, name: str, height: int, age: int,
                 trunk_diameter: int) -> None:
        super().__init__(name, height, age)
        self.trunk_diameter = trunk_diameter

    def produce_shade(self, shade_surface: int) -> None:
        print(f"{self.name} provides {shade_surface} square meters of shade")

    def display_info(self) -> None:
        print(f"{self.name} (Tree): {self.get_common_info()}"
              f", {self.trunk_diameter}cm diameter")


class Vegetable(Plant):
    def __init__(self, name: str, height: int, age: int, harvest_season: str,
                 nutritional_value: str) -> None:
        super().__init__(name, height, age)
        self.harvest_season = harvest_season
        self.nutritional_value = nutritional_value

    def nutri_value(self) -> None:
        print(f"{self.name} is rich in vitamin {self.nutritional_value}")

    def display_info(self) -> None:
        print(f"{self.name} (Vegetable): {self.get_common_info()}"
              f", {self.harvest_season}")


if __name__ == "__main__":
    flower_1 = Flower("Rose", 25, 30, "red")
    flower_2 = Flower("Tulip", 45, 50, "yellow")
    tree_1 = Tree("Oak", 500, 1825, 50)
    tree_2 = Tree("Pine", 1000, 2000, 100)
    vegetable_1 = Vegetable("Tomato", 80, 90, "summer harvest", "C")
    vegetable_2 = Vegetable("Carrot", 100, 200, "winter harvest", "A")
    print("=== Garden Plant Types ===")
    print()
    flower_1.display_info()
    flower_1.bloom()
    flower_2.display_info()
    flower_2.bloom()
    print()
    tree_1.display_info()
    tree_1.produce_shade(78)
    tree_2.display_info()
    tree_2.produce_shade(88)
    print()
    vegetable_1.display_info()
    vegetable_1.nutri_value()
    vegetable_2.display_info()
    vegetable_2.nutri_value()
