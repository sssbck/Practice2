

if __name__ == "__main__":
    i = 1
    while i <= 5:
        print("i =", i)
        i += 1

    numbers = [1, 2, 3, 4]
    idx = 0
    total = 0
    while idx < len(numbers):
        total += numbers[idx]
        idx += 1
    print("Sum =", total)

    attempts = 0
    max_attempts = 3
    is_logged_in = False

    while attempts < max_attempts and not is_logged_in:
        attempts += 1
        if attempts == 2:
            is_logged_in = True

    print("Attempts:", attempts, "Logged in:", is_logged_in)
