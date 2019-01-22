ages = {"Princess Di": 57, "James Dean": 87, "Elvis": 83, "Curt Cobain": 51, "Freddie Mercury": 71}

max_age = max(zip(ages.values(), ages.keys()))
print(max_age)

max_age = max(zip(ages.keys(), ages.values()))
print("Put Keys First : ", max_age)
