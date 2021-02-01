# def describe_pets(animal_type, pet_name):
#     """Display information about pets"""
#     print(f"\nI have a {animal_type}.")
#     print(f"my {animal_type}'s name is {pet_name.title()}.")


# # describe_pets('dog', 'joey')
# describe_pets(animal_type ='dog', pet_name = 'joey')


def describe_pets(pet_name,animal_type ='cat'):
    # default parameter should be placed at last because when you call a argument program willl look for the first parameter 
    """Display information about pets"""
    print(f"\nI have a {animal_type}.")
    print(f"my {animal_type}'s name is {pet_name.title()}.")

describe_pets('joey')
#since i created default parameter for animal type, giving pet name only runs the program with default value
describe_pets(pet_name = 'chandler',animal_type='leopad')
#since i explicitly mention animal type program will ignore default parameter value
