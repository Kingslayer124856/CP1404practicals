"""
CP1404/CP5632 - Practical
Answer the following questions:
1. When will a ValueError occur?
- The Value Error occurs when the input is not a number
2. When will a ZeroDivisionError occur?
- the ZeroDivisionError will occur when the input for the denominator is 0
3. Could you change the code to avoid the possibility of a ZeroDivisionError?
-
"""

try:
    numerator = int(input("Enter the numerator: "))
    denominator = int(input("Enter the denominator: "))
    if denominator <= 0:
        print("Cannot divide by zero")
        denominator = int(input("Enter the denominator: "))
    fraction = numerator / denominator
    print(fraction)
except ValueError:
    print("Numerator and denominator must be valid numbers!")
#except ZeroDivisionError:
 #   print("Cannot divide by zero!")
print("Finished.")