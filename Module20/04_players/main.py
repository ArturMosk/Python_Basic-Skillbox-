players = {
    ("Ivan", "Volkin"): (10, 5, 13),
    ("Bob", "Robbin"): (7, 5, 14),
    ("Rob", "Bobbin"): (12, 8, 2)
}

players_new = []
for i_key, i_value in players.items():
    players_new.append(i_key + i_value)

print(players_new)
