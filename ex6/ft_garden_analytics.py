class Plant:
    def __init__(self, name: str, height: int) -> None:
        self.name = name
        self.height = height

    def grow(self, amount: int) -> None:
        self.height += amount

    def get_info(self) -> str:
        return f"{self.name}: {self.height}cm"


class FloweringPlant(Plant):
    def __init__(self, name: str, height: int, color: str) -> None:
        super().__init__(name, height)
        self.color = color

    def get_info(self) -> str:
        return f"{self.name}: {self.height}cm, {self.color} flowers"


class PrizeFlower(FloweringPlant):
    def __init__(self, name: str, height: int, color: str,
                 prize_points: int) -> None:
        super().__init__(name, height, color)
        self.prize_points = prize_points

    def get_info(self) -> str:
        return (
            f"{self.name}: {self.height}cm, {self.color} flowers, "
            f"Prize points: {self.prize_points}"
        )


class GardenManager:
    total_gardens = 0

    class GardenStats:
        def __init__(self) -> None:
            self.plants_added = 0
            self.total_growth = 0
            self.regular_count = 0
            self.flowering_count = 0
            self.prize_count = 0

    def __init__(self, owner_name: str) -> None:
        self.owner_name = owner_name
        self.plants = []
        self.stats = self.GardenStats()
        GardenManager.total_gardens += 1

    def add_plant(self, plant: Plant, silent=False) -> None:
        self.plants.append(plant)
        self.stats.plants_added += 1
        self.stats.regular_count += 1
        if not silent:
            print(f"Added {plant.name} to {self.owner_name}'s garden")

    def help_plants_grow(self) -> None:
        for p in self.plants:
            p.grow(2)
            self.stats.total_growth += 2

    def get_garden_score(self) -> int:
        score = 0
        for p in self.plants:
            score += p.height
        return score

    def create_garden_network(cls, owners_list: list) -> list:
        return [cls(owner) for owner in owners_list]

    create_garden_network = classmethod(create_garden_network)


def ft_garden_analytics() -> None:
    print("=== Garden Management System Demo ===\n")

    network = GardenManager.create_garden_network(["Alice", "Bob"])
    alice = network[0]
    bob = network[1]

    alice.add_plant(Plant("Oak Tree", 100))
    alice.add_plant(FloweringPlant("Rose", 25, "red"))
    alice.add_plant(PrizeFlower("Sunflower", 50, "yellow", 10))

    bob.add_plant(Plant("Bonsai", 92), silent=True)

    alice.help_plants_grow()

    print(f"\nGarden scores - Alice: {alice.get_garden_score()}"
          f", Bob: {bob.get_garden_score()}")


if __name__ == "__main__":
    ft_garden_analytics()
