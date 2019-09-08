paulina = {"first_name": "Paulina", "last_name": "Pragier", "age": "32", "city": "Gdynia"}
celina = {"first_name": "Celina", "last_name": "Pragier", "age": "5", "city": "Gdynia"}
michalina = {"first_name": "Michalina", "last_name": "Pragier", "age": "2", "city": "Gdynia"}

people = [paulina, celina, michalina]

for peop in people:
    print("Użytkownik " + peop["first_name"] + " " + peop["last_name"] + " lat " + peop["age"] + " mieszka w mieście "
          + peop["city"])

