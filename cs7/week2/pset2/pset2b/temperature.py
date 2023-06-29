# Prints the Kelvin equivalent of any temperature in degrees Fahrenheit

fahrenheit = float(input("Input a temperature in degrees Fahrenheit to be converted: "))
kelvin = (5 / 9) * (fahrenheit - 32) + 273.16

# Note: "Kelvins" are an absolute unit of temperature, so the term "degrees" is not appropriate
print(f"{fahrenheit} degrees Fahrenheit equals {kelvin} Kelvins.")