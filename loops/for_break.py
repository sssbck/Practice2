
if __name__ == "__main__":
    for i in range(1, 11):
        if i == 5:
            break
        print(i)

    items = ["plc", "scada", "python", "dcs"]
    target = "python"
    found = False

    for item in items:
        if item == target:
            found = True
            break

    print("Found target?", found)

    matrix = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9],
    ]
    target = 8
    pos = None

    for r in range(len(matrix)):
        for c in range(len(matrix[r])):
            if matrix[r][c] == target:
                pos = (r, c)
                break
        if pos is not None:
            break

    print("Target position:", pos)
