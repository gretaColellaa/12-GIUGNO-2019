from dataclasses import dataclass

@dataclass
class Food:
    food_id:int
    food_code:int
    display_name:str
    calories:float


    def __hash__(self):
        return hash(self.food_id)

    def __str__(self):
        return f"{self.food_code} – {self.display_name}, {self.calories} calorie"

