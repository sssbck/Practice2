
if __name__ == "__main__":
    a = 10
    b = 20

    bigger = a if a > b else b
    print("Bigger:", bigger)

    n = 13
    print("even" if n % 2 == 0 else "odd")

    score = 59
    status = "pass" if score >= 60 else "fail"
    print("Status:", status)

    is_ready = True
    if is_ready: print("Ready!")  
