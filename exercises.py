# Exercise 1: Calculate Area of a Triangle
#
# Write a function named `calculate_area_triangle` that takes the base and height of a triangle and returns the area.
# The area formula is (base * height) / 2.
#
# Examples:
# calculate_area_triangle(10, 5) should return 25.0.
# calculate_area_triangle(7, 3) should return 10.5.
#
# Define your function and call it below.

def calculate_area_triangle(base, height):
    area = (base * height) / 2

    return area

print('Exercise 1:', calculate_area_triangle(10, 5))



# Exercise 2: Apply a Discount
#
# Write a function named `apply_discount` that takes a product's price and a discount percentage (from 0 to 100).
# Return the new price after applying the discount.
#
# Examples:
# apply_discount(100, 25) should return 75.
# apply_discount(80, 10) should return 72.
#
# Define your function and call it to display the discounted price.


def apply_discount(price, discount_percentage):
    discount = price * (discount_percentage / 100)
    final_price = price - discount
    return final_price

#print(apply_discount(100, 25))  # 75.0
#print(apply_discount(80, 10))   # 72.0

print('Exercise 2:', apply_discount(100, 25))




# Exercise 3: Convert Temperature
#
# Write a function called `convert_temperature` that takes a
# temperature and a unit ('C' for Celsius, 'F' for Fahrenheit)
# and converts the temperature to the other unit.
# The formula for converting Celsius to Fahrenheit is (Celsius * 9/5) + 32.
# The formula for converting Fahrenheit to Celsius is (Fahrenheit - 32) * 5/9.
#
# Examples:
# convert_temperature(0, 'C') should return 32.0.
# convert_temperature(32, 'F') should return 0.0.
#
# Define the function and then call it below.


def convert_temperature(temperature, unit):
    if unit == 'C':
        return (temperature * 9 / 5) + 32
    elif unit == 'F':
        return (temperature - 32) * 5 / 9

#print(convert_temperature(25, 'C'))  # 77.0
#print(convert_temperature(77, 'F'))  # 25.0

print('Exercise 3: Convert 0°C to Fahrenheit:', convert_temperature(0, 'C'))
print('Exercise 3: Convert 32°F to Celsius:', convert_temperature(32, 'F'))
