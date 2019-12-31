# -----------------------------------------------------------
# magic methods exercises in python
# -----------------------------------------------------------   

# Source: https://www.python-course.eu/python3_magic_methods.php
#
# Write a class with the name Ccy, similar to the previously defined Length class.
#
# Ccy should contain values in various currencies, e.g. "EUR", "GBP" or "USD". An instance should contain the amount and the currency unit.
#
# The class, you are going to design as an excercise, might be best described with the following example session:
#

from currencies import Currency
# v1 = Currency(23.43, "EUR")
# v2 = Currency(19.97, "USD")
# print(v1)
# print(v1 + v2)
# 32.89 EUR
# print(v2 + v1)
# 31.07 USD
# print(v1 + 3) # an int or a float is considered to be a EUR value
# 27.43 EUR
# print(3 + v1)
# 27.43 EUR

