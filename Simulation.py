import numpy as np

#winrate: float = 0.55
Diamonds = 10000

class Draft:
    pass

class Quickdraft(Draft):
    cost = 750
    reward = {0:50, 1: 100, 2:200, 3:300, 4:450, 5:650, 6:850, 7:950}

class Premierdraft(Draft):
    cost = 1500
    reward = {0:50, 1: 100, 2:250, 3:1000, 4:1400, 5:1600, 6:1800, 7:2200}

class Traditional(Draft):
    cost = 1500
    reward = {0:100, 1: 250, 2:1000, 3:2500}

def start_game(winrate)->bool:
    win = np.random.choice([True, False], p=[winrate, 1-winrate])
    return win

def draft_simulation(Draft, winrate)->bool:
    # Simulates an Arena Drafts and updates the Diamond count, based on the winrate
    try:
        Draft.cost
        Draft.reward
    except:
        print("Draft class has no cost")

    # check if Draft is of tyoe traditional
    if isinstance(Draft, Traditional):
        sucess = simulate_traditional(Draft, winrate)
    else:
        sucess = simulate_quick_and_premier(Draft, winrate)

    return sucess



def simulate_traditional(Draft, winrate)->bool:
    global Diamonds
    if Diamonds < Draft.cost:
        return False
    Diamonds = Diamonds - Draft.cost
    wins = 0
    outcome = {"wins":0, "looses":0}

    for games in range(3):
        for subgames in range(3):
            if start_game(winrate):
                outcome["wins"] += 1
            else:
                outcome["looses"] += 1

            if outcome["wins"] == 2:
                wins += 1
                break
            if outcome["looses"] == 2:
                break

    Diamonds += Draft.reward[wins]
    return True
            
def simulate_quick_and_premier(Draft, winrate)->bool:
    global Diamonds
    if Diamonds < Draft.cost:
        return False
    Diamonds = Diamonds - Draft.cost

    wins = 0
    looses = 0
    for game in range(10):
        if start_game(winrate):
            wins += 1
        else:
            looses += 1
        if wins == 7 or looses == 3:
            rewards = Draft.reward[wins]
            Diamonds += rewards
            wins, looses = 0, 0 
            break
    return True