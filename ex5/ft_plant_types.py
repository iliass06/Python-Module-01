class Plant:
    def __init__(self, name, height, age):
        self.name = name
        self.height = height
        self.age = age
        
class Flower(Plant):
    def __init__(self, name, height, age, color):
        super().__init__(name, height, age)
        self.color = color
    
    def bloom(self):
       print(f"{self.name} is blooming beautifully!") 

class Tree(Plant):
    def __init__(self, name, height, age, trunk_diameter):
        super().__init__(name, height, age)
        self.trunk_diameter = trunk_diameter
    
    def produce_shade(self, shade_surface):
        print(f"{self.name} provides {shade_surface} square meters of shade")
        
        
class Vegetable(Plant):
    def __init__(self, name, height, age, harvest_season, nutritional_value):
        super().__init__(name, height, age)
        self.harvest_season = harvest_season
        self.nutritional_value = nutritional_value
        
    def nutri_value(self):
        print(f"{self.name} is rich in vitamin {self.nutritional_value}")
        
if __name__ == "__main__":
    f1 = Flower("Rose", 25, 30, "red")
    f2 = Flower("warda", 45, 50, "yellow")
    t1 = Tree("Oak", 500, 1825, 50)
    t2 = Tree("sanawbar", 1000, 2000, 100)
    v1 = Vegetable("Tomato", 80, 90, "summer harvest", "C")
    v2 = Vegetable("carrot", 100, 200, "winter harvest", "A")
    print("=== Garden Plant Types ===")
    print()
    print(f"{f1.name} (Flower): {f1.height}cm, {f1.age} days, {f1.color} color")
    f1.bloom()
    print()
    print(f"{t1.name} (Tree): {t1.height}cm, {t1.age} days, {t1.trunk_diameter}cm diameter")
    t1.produce_shade(78)
    print()
    print(f"{v1.name} (Vegetable): {v1.height}cm, {v1.age} days, {v1.harvest_season}")
    v1.nutri_value()