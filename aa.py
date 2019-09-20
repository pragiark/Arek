sandwich_orders = ["pastrani", "boczek", "ser", "pastrani", "salami", "tuńczyk", "pastrani"]
finished_sandwiches = []

print("Brak pastrani")
while "pastrani" in sandwich_orders:
    sandwich_orders.remove("pastrani")

print(sandwich_orders)

while sandwich_orders:
    for sandwitch in sandwich_orders:
        order = sandwich_orders.pop()
        finished_sandwiches.append(order)


