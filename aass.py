prompt = "Ile masz lat?"
active = True
while active:
    massage = input(prompt)
    if massage == "koniec":
        active = False
    if massage != "koniec":
        print("Masz teraz " + massage + " lat")
