
def main():
    score = float(input("Enter Score: "))
    print(evaluate_status(score))


def evaluate_status(score):
    if score < 0 or score > 100:
        return "Invalid Score"
    elif score >= 90:
        return "Excellent"
    elif score >= 50:
        return "Passable"
    else:
        return "Bad"


main()
