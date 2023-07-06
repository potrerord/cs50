"""
Prints the Kelvin equivalent of any temperature in degrees Fahrenheit as
provided by user input.

Fun fact: "Kelvins" are an absolute unit of temperature, so the term
"degrees" is not appropriate when referring to them.
"""


def main():
    """Request temperature from user and print results in simple
    English.
    """

    # Request and convert temperature, provide prompt for get_temp
    # function.
    fahrenheit = get_temp("Input a temperature in degrees Fahrenheit to be "
                         "converted to Kelvins: ")
    kelvin = convert_temp_ftok(fahrenheit)

    # Formattng an "s" for a plural amount of units. If either
    # temperature's float value is 1.0, it will be referred to as
    # singular.
    f_plural = "s"
    k_plural = "s"
    if int(fahrenheit) == 1.0:
        f_plural = ""
    if int(kelvin) == 1.0:
        k_plural = ""

    # Print results.
    print(f"{fahrenheit} degree{f_plural} Fahrenheit equals "
          f"{kelvin:.2f} Kelvin{k_plural}.")
    print()


def get_temp(prompt: str) -> float:
    """Prompt user and continually reprompt if input is nonnumeric.
    Return float user input.

    Keyword argument:
    prompt -- The string prompt that will accept user input.
    """

    while True:
        user_input = input("\n" + prompt)
        if user_input.isdigit():
            return float(user_input)
        print("error: temperature must be numeric")


def convert_temp_ftok(f_temp) -> float:
    """Convert temperature from degrees Fahrenheit to Kelvins.
    Returns temperature in Kelvins as a float.
    """

    k_temp = (5 / 9) * (f_temp - 32) + 273.16
    return k_temp


main()
