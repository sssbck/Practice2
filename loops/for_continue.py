"""
for_continue.py
Тема: For Loop Continue

continue - пропускает текущую итерацию
"""

if __name__ == "__main__":
    nums = [5, -1, 7, -3, 10]
    positives = []
    for n in nums:
        if n < 0:
            continue
        positives.append(n)
    print("Positives:", positives)

    words = ["a", "python", "plc", "scada", "ok"]
    long_words = []
    for w in words:
        if len(w) < 3:
            continue
        long_words.append(w)
    print("Long words:", long_words)

    for i in range(1, 11):
        if i % 3 == 0:
            continue
        print("Not multiple of 3:", i)
