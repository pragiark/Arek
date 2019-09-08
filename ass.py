favorite_places = {
    "Paulina": ["Gdynia", "Gdańsk", "Sopot"],
    "Celina": ["Gdynia2", "Gdańsk2", "Sopot2"],
    "Michalina": ["Gdynia3", "Gdańsk3", "Sopot3"],}

fav = []
for key,value in favorite_places.items():
    fav.append(key)
    for value in favorite_places.items():
        fav.append(value)

print(fav)