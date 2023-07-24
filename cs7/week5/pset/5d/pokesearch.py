

import sys

import pokedex


# Valid traits for Pokemon
TRAITS = ["HP", "Attack", "Sp. Attack", "Sp. Defense", "Speed"]


def main():
    # Add your solution to the problem that makes use of the above to
    # print out the results of your pokemon search.

    print()
    print("What Pokemon trait would you like to search on?")
    user_trait = input("Valid traits are HP, Attack, Sp. Attack, Sp. Defense, Speed: ")
    if user_trait not in TRAITS:
        sys.exit(f"\nInvalid trait.\n")

    user_min = int(input(f"What is the minimum value for {user_trait}? "))
    user_max = int(input(f"What is the maximum value for {user_trait}? "))

    user_matches, width = pokesearch(user_trait, user_min, user_max)
    sorted_user_matches = sorted(list(user_matches.keys()))

    print("The Pokemon that match are:")
    for pokemon in sorted_user_matches:
        print(f"{pokemon:<{width + 1}}{user_matches[pokemon]}")


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
    name_length = 0
    for pokemon in pokedex.data:
        if minimum <= pokemon["base"][trait] <= maximum:
            matches[english_name(pokemon)] = pokemon["base"][trait]
            if len(english_name(pokemon)) > name_length:
                name_length = len(english_name(pokemon))

    return matches, name_length


if __name__ == "__main__":
    main()
