def main():
    score = float(input("Enter score: "))
    result = determine_status(score)
    print(result)


def determine_status(score):
    if score < 0 or score > 100:
        return "Invalid score"
    elif score >= 90:
        return "Excellent"
    elif score >= 50:
        return "Passable"
    else:
        return "Bad"


main()