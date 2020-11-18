def check_password(n):
    str(n)
    s = 0
    if len(n) >= 10:
        for i in n:
            if i.isdigit():
                if i.isupper():
                    if i.isalnum():
                        s = s + 1

    if s >= 10:
        print("Perfect password")
    else:
        print("Easy peasy")

check_password("Qwertypas12!")