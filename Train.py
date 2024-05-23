import random

players = {
    "Ber": "forward",
    "Roma": "defender",
    "Kulachini": "goalkeeper",
    "Osokin": "defender",
    "Dog": "goalkeeper",
    "Denis": "defender",
    "Sasha": "defender",
    "Ivan": "forward",
    "Sergey": "defender",
    "ManCity": "forward",
    "Dmitry": "goalkeeper",
    "Evgeny": "forward",

    }
goalies = []
defs = []
strikers = []
players_ready = []
number_of_players = int(input("How many players are available? "))
for i in range(1, number_of_players + 1):
    player = input("Type a player: ")
    players_ready.append(player)
    if players[player] == "goalkeeper":
        goalies.append(player)
    elif players[player] == "defender":
        defs.append(player)
    else:
        strikers.append(player)

team_one = []
team_two = []



if len(goalies) >=2 and len(strikers) >= 2:
    first_gk = random.choice(goalies)
    team_one.append(first_gk)
    goalies.remove(first_gk)
    players_ready.remove(first_gk)
    second_gk = random.choice(goalies)
    team_two.append(second_gk)
    goalies.remove(second_gk)
    players_ready.remove(second_gk)
    first_str = random.choice(strikers)
    team_one.append(first_str)
    strikers.remove(first_str)
    players_ready.remove(first_str)
    second_str = random.choice(strikers)
    team_two.append(second_str)
    strikers.remove(second_str)
    players_ready.remove(second_str)
    for c in range(1, int(len(players_ready)/2) + 1):
        first = random.choice(players_ready)
        team_one.append(first)
        players_ready.remove(first)
        second = random.choice(players_ready)
        team_two.append(second)
        players_ready.remove(second)
elif len(goalies) >=2:
    first_gk = random.choice(goalies)
    team_one.append(first_gk)
    goalies.remove(first_gk)
    players_ready.remove(first_gk)
    second_gk = random.choice(goalies)
    team_two.append(second_gk)
    goalies.remove(second_gk)
    players_ready.remove(second_gk)
    for c in range(1, int(len(players_ready)/2) + 1):
        first = random.choice(players_ready)
        team_one.append(first)
        players_ready.remove(first)
        second = random.choice(players_ready)
        team_two.append(second)
        players_ready.remove(second)
elif len(strikers) >= 2:
    first_str = random.choice(strikers)
    team_one.append(first_str)
    strikers.remove(first_str)
    players_ready.remove(first_str)
    second_str = random.choice(strikers)
    team_two.append(second_str)
    strikers.remove(second_str)
    players_ready.remove(second_str)
    for c in range(1, int(len(players_ready)/2) + 1):
        first = random.choice(players_ready)
        team_one.append(first)
        players_ready.remove(first)
        second = random.choice(players_ready)
        team_two.append(second)
        players_ready.remove(second)
elif len(goalies) == 1 and len(strikers) == 1:
    first = random.choice(goalies)
    team_one.append(first)
    goalies.remove(first)
    players_ready.remove(first)
    second = random.choice(strikers)
    team_two.append(second)
    strikers.remove(second)
    players_ready.remove(second)
    for c in range(1, int(len(players_ready)/2) + 1):
        first = random.choice(players_ready)
        team_one.append(first)
        players_ready.remove(first)
        second = random.choice(players_ready)
        team_two.append(second)
        players_ready.remove(second)
else:
    for c in range (1, int(len(players_ready)/2) + 1):
        first = random.choice(players_ready)
        team_one.append(first)
        players_ready.remove(first)
        second = random.choice(players_ready)
        team_two.append(second)
        players_ready.remove(second)

print(team_one)
print(team_two)









