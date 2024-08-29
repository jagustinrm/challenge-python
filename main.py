from menu import show_menu, continue_or_exit, create_zoo
from animal import Giraffe, Crocodile, GiantTortoise
from utils import select_animal_by_species

def main():
    my_zoo = create_zoo()

    while True:
        show_menu()
        choice = input("Choose an option: ").strip()

        if choice == '1':
            species = input("Enter animal species (Giraffe, Crocodile, Giant Tortoise): ").strip().capitalize()
            name = input("Enter animal name: ").strip()
            gender = input("Enter animal gender (Male/Female): ").strip().capitalize()
            
            if species == "Giraffe":
                height = float(input("Enter giraffe's height in meters: "))
                animal = Giraffe(name, gender, height)

            elif species == "Crocodile":
                teeth = int(input("Enter number of teeth: "))
                ffood = input("Enter its favorite food: ")
                animal = Crocodile(name, gender, teeth, ffood)

            elif species == "Giant Tortoise":
                age = int(input("Enter age of the tortoise: "))
                animal = GiantTortoise(name, gender, age)

            else:
                print("Invalid species entered.")
                continue

            my_zoo.add_animal(animal)

        elif choice == '2':
            animal_name = input("Enter the name of the animal to remove: ").strip()
            my_zoo.remove_animal(animal_name)

        elif choice == '3':
            my_zoo.print_animals()

        elif choice == '4':
            my_zoo.animal_count()

        elif choice == '5':
            my_zoo.admission_price()

        elif choice == '6':  # Giraffe Height
            selected_name = select_animal_by_species(my_zoo.animals, Giraffe)
            if selected_name:
                for animal in my_zoo.animals:
                    if animal.name == selected_name:
                        print(animal.compare_height())
                        break

        elif choice == '7':  # Crocodile's Favorite Food
            selected_name = select_animal_by_species(my_zoo.animals, Crocodile)
            if selected_name:
                for animal in my_zoo.animals:
                    if animal.name == selected_name:
                        print(animal.favorite_food())
                        break

        elif choice == '8':  # Giant Tortoise Age Category
            selected_name = select_animal_by_species(my_zoo.animals, GiantTortoise)
            if selected_name:
                for animal in my_zoo.animals:
                    if animal.name == selected_name:
                        print(animal.age_category())
                        break

        elif choice == '9':
            print("Thanks for using the Zoo Management System. Goodbye!")
            break

        else:
            print("Invalid choice. Please select a valid option.")
            continue
        # Si quiere o no volver al menú
        if not continue_or_exit():
            break

if __name__ == "__main__":
    main()
