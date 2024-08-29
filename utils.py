def select_animal_by_species(animals, species_type):
    species_list = [animal.name for animal in animals if isinstance(animal, species_type)]
    
    if not species_list:
        print(f"No {species_type.__name__}s found in the zoo.")
        return None

    print("Select an animal:")
    for index, name in enumerate(species_list, 1):
        print(f"{index}. {name}")

    while True:
        try:
            choice = int(input("Choose an animal by number: ")) - 1
            if 0 <= choice < len(species_list):
                return species_list[choice]
            else:
                print("Invalid choice. Please try again.")
        except ValueError:
            print("Invalid input. Please enter a number.")
