cities = {
    "Gdynia": {"Country": "Polska", "Pulation": 200, "Fact": "Dostęp do morza"},
    "Katowice": {"Country":"Polska", "Pulation": 2500, "Fact": "Ma spodek"},
    "Kraków": {"Country":"Polska", "Pulation": 3000, "Fact": "Smog wawelski"},
}

for city, cityprop in cities.items():
    print(city)
    print("To miasto leży w kraju o nazwie: " + cityprop["Country"] + ", ilość ludności to: " + str(cityprop["Pulation"])
          + ", interesujący fakt dotyczący tego miasta: " + cityprop["Fact"])
