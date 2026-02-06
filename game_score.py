#game_score.py
player_name = input("enter player name")
games_played = int(input("enter number of games played"))
total_score = int(input("enter total score"))

average_score = total_score/games_played

print("player :",player_name)
print("games_played :",games_played)
print("total_score :",total_score)
print("average score :",average_score)