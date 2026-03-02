class Plant:
    def __init__(self, name, height):
        self.name = name
        self.height = height

class FloweringPlant(Plant):
    def __init__(self, name, height, color):
        super().__init__(name, height)
        self.color = color

class PrizeFlower(FloweringPlant):
    def __init__(self, name, height, color, prize_points):
        super().__init__(name, height, color)
        self.prize_points = prize_points
        
class GardenManager:
    def __init__(self):
        self.gardens = []
    
    class GardenStats:
        def __init__(self, plants_list):
            self.plants_list = plants_list
            
        def calculates_types(self):
            pass
        def calculate_total_growth(self):
            pass
        
    def add_plant(self, garden_name, plant):
        print(f"Added {self.plant} to {garden_name}'s garden")
    classmethod()
    def simulate_growth(self, garden_name, amount):
        pass
    
    def generate_report(self, garden_name):
        pass
    
    @classmethod
    def create_garden_network(cls):
        pass
    
    @staticmethod
    def is_valid_height(height):
        pass
        
