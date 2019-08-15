"""
CP1404/CP5632 - Practical
Broken program to determine score status
"""

score = float(input("Enter Score: "))
if score < 0:
    print("Invalid Score")
elif score < 50:
    print("Bad")
else:
    if score > 100:
        print("Invalid Score")
    elif score > 90:
        print("Excellent")
    elif score > 50:
        print("Passable")
