

import pokedex


# Valid traits for Pokemon
TRAITS = ["HP", "Attack", "Sp. Attack", "Sp. Defense", "Speed"]


def main():
    # Add your solution to the problem that makes use of the above to
    # print out the results of your pokemon search.

    print("What Pokemon trait would you like to search on?")
    user_trait = input("Valid traits are HP, Attack, Sp. Attack, Sp. Defense, Speed: ")

    user_min = int(input(f"What is the minimum value for {user_trait}? "))
    user_max = int(input(f"What is the maximum value for {user_trait}? "))

    user_matches = pokesearch(user_trait, user_min, user_max)
    sorted_user_matches = sort(list(user_matches.keys()))

    print("The Pokemon that match are:")
    for pokemon in sorted_user_matches:
        print(f"{pokemon:<20}{user_matches[pokemon]}")


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

    matches = {}
    for pokemon in pokedex.data:
        if minimum <= pokedex.data[pokemon]["base"][trait] <= maximum:
            matches[pokemon] = pokedex.data[pokemon]["base"][trait]

    return matches


if __name__ == "__main__":
    main()
