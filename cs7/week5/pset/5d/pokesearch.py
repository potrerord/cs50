

import pokedex


# Valid traits for Pokemon
TRAITS = ["HP", "Attack", "Sp. Attack", "Sp. Defense", "Speed"]


def main():
    # Add your solution to the problem that makes use of the above to
    # print out the results of your pokemon search.
    print("Remove me and add your code!")


def english_name(pokemon):
    """OPTIONAL:
    You can use this as a sorting key function for Pokemon"""
    return pokemon["name"]["english"]


def pokesearch(trait, minimum, maximum):
    """
    Returns a list of Pokemon data structures (dictionaries,
    as shown in the pset problem description) that
    have a value of trait between minimum and maximum
    """

    print("What Pokemon trait would you like to search on?")
    trait = input("Valid traits are HP, Attack, Sp. Attack, Sp. Defense, Speed: ")

    min = int(input(f"What is the minimum value for {trait}? "))
    max = int(input(f"What is the maximum value for {trait}? "))

    print("The Pokemon that match are:")
    

if __name__ == "__main__":
    main()
