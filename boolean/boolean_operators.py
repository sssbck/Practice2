
if __name__ == "__main__":
    age = 18
    has_id = True
    has_ticket = False

    can_enter = age >= 18 and has_id
    print("can_enter (age>=18 and has_id):", can_enter)

    can_watch = has_ticket or age >= 18
    print("can_watch (ticket or adult):", can_watch)

    is_blocked = False
    print("not is_blocked:", not is_blocked)

    allowed = (age >= 18 and has_id) or has_ticket
    print("allowed:", allowed)

    result = True or False and False
    print("True or False and False =", result)  
