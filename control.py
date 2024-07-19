import dbOperations
import battleEngine

def player_creation_validity(player_creation_request):
    # TODO GET request - is name in DB?
    if len(player_creation_request["name"]) < 21: #and name not in db
        return True
    else:
        return False
    
def create_player(player_creation_request):
    user_name = player_creation_request["name"]
    result = dbOperations.create_record("player", ["name"], [user_name])
    if result:
        return "Player created", 201
    else:
        return "Name taken or exceeds 20 characters. Try again!", 400

def battle_validity(battle_request):
    # check that both players are in the db
    names = dbOperations.read_record("player")
    player1 = battle_request["player1"]
    player2 = battle_request["player2"]

    if player1 in names and player2 in names:
        return True
    else:
        return False

def battle_process(battle_request):
    player1 = battle_request["player1"]
    player2 = battle_request["player2"]
    battleEngine.battle_process(player1, player2)

    return