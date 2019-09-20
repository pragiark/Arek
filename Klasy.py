
class Calculator():

    def __init__(self):
        print("init")

    def __del__(self):
        print("Del")

    def __str__(self):
        return "Hello"

    def dodaj(self, a, b):
        wynik = a + b
        print(wynik)
    def odejmij(self, a, b):
        wynik = a - b
        print(wynik)


calc = Calculator()
calc.dodaj(7,7)

print(len(calc))
