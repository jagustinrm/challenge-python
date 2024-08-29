from animal import Animal
from datetime import datetime
class Zoo:
    def __init__(self, name, city, hours):
        self.name = name
        self.city = city
        self.hours = hours
        self.animals = []

    def add_animal(self, animal: Animal):
        self.animals.append(animal)
        print(f"{animal.name} the {animal.species} has been added to the zoo.")

    def remove_animal(self, name: str):
        for animal in self.animals:
            if animal.name == name:
                self.animals.remove(animal)
                print(f"{name} has been removed from the zoo.")
                return
        print(f"No animal named {name} was found in the zoo.")

    def print_animals(self):
        if not self.animals:
            print("There are no animals in the zoo.")
        else:
            for animal in self.animals:
                animal.describe()

    def animal_count(self):
        print(f"There are {len(self.animals)} animals in the zoo.")

    def admission_price(self):

        day_of_week = datetime.now().strftime('%A')
        if day_of_week in ['Monday', 'Tuesday']:
            price = 19.99
        elif day_of_week == 'Wednesday':
            price = 9.99
        elif day_of_week in ['Thursday', 'Friday']:
            price = 19.99
        else:  
            price = 25.99
        print(f"Today's admission price is: ${price:.2f}")

