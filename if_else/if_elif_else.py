
if __name__ == "__main__":
    score = 76

    if score >= 90:
        grade = "A"
    elif score >= 75:
        grade = "B"
    elif score >= 60:
        grade = "C"
    else:
        grade = "D"
    print("Score:", score, "Grade:", grade)

    x = 0
    if x > 0:
        print("positive")
    elif x < 0:
        print("negative")
    else:
        print("zero")

    age = 18
    if age < 13:
        print("child")
    elif age < 18:
        print("teen")
    else:
        print("adult")

    temp = 10
    if temp > 25:
        print("hot")
    elif 10 <= temp <= 25:
        print("warm")
    else:
        print("cold")
