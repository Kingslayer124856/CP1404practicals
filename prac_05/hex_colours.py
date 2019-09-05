"""
CP1404 Practical
Intermediate Exercise with
hexadecimal colours codes
"""

COLOUR_CODES = {"coral": "#ff7f50", "chocolate": "#d2691e",
                "gray": "#bebebe", "sea green": "#c1ffc1",
                "cyan": "#00ffff", "ivory": "#fffff0",
                "lavender": "#e6e6fa", "purple": "#9370db",
                "turquoise": "#48d1cc", "red": "#ff0000"}

colour_name = input("Enter a colour name: ").lower()
while colour_name != "":
    print("The code for \"{}\" is {}".format(colour_name,
                                             COLOUR_CODES.get(colour_name)))
colour_name = input("Enter a colour name: ").lower()
