

if __name__ == "__main__":
    i = 0
    while i < 10:
        i += 1
        if i % 2 == 0:
            continue
        print("Odd number:", i)

    words = ["hello", "", " ", "python", "\n", "scada"]
    index = 0
    cleaned = []

    while index < len(words):
        word = words[index]
        index += 1

        if word.strip() == "":
            continue

        cleaned.append(word.strip())

    print("Cleaned words:", cleaned)

    attempt = 0
    while attempt < 5:
        attempt += 1
        if attempt == 3:
            continue
        print("Attempt:", attempt)
