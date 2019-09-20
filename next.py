
try:
    plik = open("test.txt", "w")
    plik.read("o")
    plik.close()

except FileNotFoundError as e:
    print("NIe istnieje utwórz plik")
    print(e)


except Exception as e:
    print("nienany bład")
    print(e)

    pr