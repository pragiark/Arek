def is_symmetrical(num):
    reverse = ""
    for a in num:
        reverse = a + reverse
    print(reverse)
    print (num)
    if num == reverse:
        print(True)
    else:
        print(False)

is_symmetrical("5656")

