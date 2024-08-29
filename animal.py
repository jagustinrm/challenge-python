class Animal:
    def __init__(self, species, name, gender, legs=4):
        self.species = species
        self.name = name
        self.gender = gender
        self.legs = legs

    def describe(self):
        print(f"{self.name} is a {self.gender} {self.species} with {self.legs} legs.")

class Giraffe(Animal):
    def __init__(self, name, gender, height):
        super().__init__("Giraffe", name, gender)
        self.height = height

    def compare_height(self):
        average_height = 5.5 if self.gender == "Male" else 4.6
        comparison = "taller" if self.height > average_height else "shorter"
        return f"{self.name} is {comparison} than the average {self.gender.lower()} giraffe."

class Crocodile(Animal):
    def __init__(self, name, gender, teeth, ffood):
        super().__init__("Crocodile", name, gender)
        self.teeth = teeth
        self.ffood = ffood

    def favorite_food(self):
        return f"{self.name}'s favorite food is {self.ffood}."

class GiantTortoise(Animal):
    def __init__(self, name, gender, age):
        super().__init__("Giant Tortoise", name, gender)
        self.age = age

    def age_category(self):
        if self.age < 50:
            category = "young"
        elif 50 <= self.age <= 100:
            category = "middle-aged"
        else:
            category = "old"
        return f"{self.name} is {category}."
