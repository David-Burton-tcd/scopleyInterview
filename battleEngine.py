import dbOperations
import random

# corresponding columns
    # 0 - id
    # 1 - name
    # 2 - gold
    # 3 - attack_value
    # 4 - max_health
    # 5 - luck
    # 6 - created_at

def battle_process(player1, player2):
    player1_data = dbOperations.read_record("player", f"name='{player1}'")
    player2_data = dbOperations.read_record("player", f"name='{player2}'")
    players = [player1_data[0], player2_data[0]]

    player1_current_health = player1_data[0][4]
    player2_current_health = player2_data[0][4]
    players_current_health = [player1_current_health, player2_current_health]

    turn_count = 0
    active_player = 0
    defending_player = 0
    winner = -1
    second_place = -1

    while players_current_health[0] > 0 and players_current_health[1]> 0:
        turn_count+=1
        if turn_count % 2 == 0:
            active_player = 0
            defending_player = 1
        else:
            active_player = 1
            defending_player = 0

        active_player_attack = players[active_player][3] * (players_current_health[active_player]/players[active_player][4])
        random_chance = random.randint(0, 100)
        if random_chance > players[active_player][5]:
            players_current_health[defending_player] = players_current_health[defending_player] - active_player_attack

    if players_current_health[0] > 0 and players_current_health[1] <= 0:
        winner = 0
        second_place = 1
    elif players_current_health[1] > 0 and players_current_health[0] <= 0:
        winner = 1
        second_place = 0
    
    # see notes
    distribute_rewards(winner, second_place)

    return 


def distribute_rewards(winner, second_place):
    update_leader_board(winner)

def update_leader_board(winner):
    pass