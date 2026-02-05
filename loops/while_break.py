
if __name__ == "__main__":
    i = 1
    while i <= 10:
        if i == 6:
            break
        print("i =", i)
        i += 1

    nums = [3, 7, 10, 15, 20]
    target = 10
    index = 0

    while index < len(nums):
        if nums[index] == target:
            print("Found target:", target)
            break
        index += 1

    count = 0
    while True:
        count += 1
        if count == 3:
            print("Stop loop at count =", count)
            break
