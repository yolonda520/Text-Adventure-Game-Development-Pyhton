"""
DocString:
This is a KO game from the movie'The Hunger Games'.
Each player and opponent attributes are randomly generated and each side attacks the other until one side has less than zero health.
In addition, such a battle will continue for three rounds, take two wins out of three as the final survier.
"""

import time
import random


def game_start():
    print("""
    welcome to "HUNGER GAME"!
    You have been selected to hunt and kill stand for our area in the hunger games this year.
    In this hunger games, you have to try your best to kill other players, and the last one who survives will get a huge bonus.
    Or, you may die if you failed.

    This is the hunger games regional tryouts, only the winner from here can join to the finnal fighting! """)

    game_player = input("What\'s your name, my brave challenger?\n >")

    print(f"""
    Welcome to hunger game,{game_player}!
    You will challenge the opponent in a random draw and may lose your life in any of round if you failed.
    Of course, if you can successfully beat the opponent up to two out of three rounds if you still survives, you will go to the final fight with last year's champion: Miss Katniss Everdeen!
    """)

    print(f"I'd like to get to know you better {game_player}!")
    weapon = input("What weapon would you like to use for fighting today? \n>")
    body_part = input("Which part of your body do you like best? \n> ")

    print(f"""
    Ladies and gentlemen, this is {game_player},
    Our contestant tonight is going to use {weapon}, which is best for fighting!
    Don't leave us, We'll be right back.\n""")

    game_choice(game_player, weapon, body_part)

def game_end(message):o
    print(message)
    while True:
        player_answer = input(">").casefold()
        if player_answer == "no":
            print("Sorry to hear that... Bye!")
            break
        elif player_answer == "yes":
            print("Great!")
            return game_start()
        print("Could you repeat please? I didnt understand you...")
        continue

def game_choice(game_player, weapon, body_part):
    player_answer = input("Are you ready to fight for honor in this round?\n>").casefold()
    if player_answer == 'yes' or player_answer == 'maybe':
        print("I knew you were the bravest warrior in our area!"+f"\n{game_player}, I'm so proud of you! Come on, let's go fight for honor!")
        return game_rounds(game_player, weapon, body_part)
    elif player_answer == 'no':
        print(f"{game_player}, you are such a coward! I kick you out of my country! From now on, you are a homeless pussy!")
        return game_end("Do you want to try again?")
    print("I am not clearly understand you. Please review the question and straight forward to answer 'yes' or 'no'\n")
    game_choice(game_player, weapon, body_part)

def game_info(game_player, player_life, player_attack, enemy_life, enemy_attack, i):
    player_info = input(f"Do you wanna know some comparative information of you and your opponent in round {i}?\n>").casefold()
    if player_info == "yes":
        return game_info_accept(game_player, player_life, player_attack, enemy_life, enemy_attack, i)
    elif player_info == "no":
        return game_info_reject(game_player)
    else:
        print("Something went wrong, please try again. I would appreciate if you can straightforward to answer 'yes' or 'no'.")
        return game_info(game_player, player_life, player_attack, enemy_life, enemy_attack, i)


def game_info_accept(game_player, player_life, player_attack, enemy_life, enemy_attack, i):
    print(f'【{game_player}】'+f'\nHealth points：{player_life}\nAttack power：{player_attack}')
    print(f"You have orignal health points {player_life},and your first attack power is {player_attack}")
    print(f'----------Good luck, {game_player}!--------------')
    print(f'【opponent in round {i}】'+f'\nHealth points：{enemy_life}\nAttack power：{enemy_attack}')
    print(f"Your first opponent has orignal health points {enemy_life}, and his first attack power is {enemy_attack}")
    print("----------I hope you can win from my deeply down, that's why I told you the opponent-------------")
    time.sleep(2)

def game_info_reject(game_player):
    print(f"""
    {game_player}! I am sorry !That was not the answer I expected! I tried to help you. But you already lost the chance to know the information in advance.
    Now if you want to know please press enter to actually attack.
    """)

def game_action(player_life, player_attack, enemy_life, enemy_attack, action):
    modificator = 1.4
    if action is True:
        player_life = player_life - enemy_attack*modificator
        enemy_life = enemy_life - player_attack*modificator
    else:
        player_life = player_life - enemy_attack/modificator
        enemy_life = enemy_life - player_attack/modificator
    return (player_life, enemy_life)

def game_round(game_player, player_life, player_attack, enemy_life, enemy_attack, weapon, i, body_part):
    while player_life > 0 and enemy_life > 0:
        print(f"Player Life: {player_life}, Enemy Life: {enemy_life}")
        first_attack = input("Are you going to attack for first move? \n1.Yes, I will attack first. \n2.No, I prefer to choose defense\n>").casefold()
        if first_attack == '1' or first_attack=='yes':
            player_life, enemy_life = game_action(player_life, player_attack, enemy_life, enemy_attack, True)
            print(f"""
                {game_player} ride a fiery horse and hurt the opponent's waist by {weapon}.
                After several rounds of fighting, you have {player_life} health points remaining.
                Opponent defense so hard, opponent is remaining health points {enemy_life} in round.
            """)
            continue
        elif first_attack == '2' or first_attack=='no':
            player_life, enemy_life = game_action(player_life, player_attack, enemy_life, enemy_attack, False)
            print(f"""
                Opponent in the round {i} shot you and hurt your {body_part}. You were seriously injured, remaining health points {player_life}.
                You hurt the opponent by the {weapon}, the opponent was hurt by you, remaining health points {enemy_life}.
            """)
            continue
        else:
            print("Something went wrong, please try again.")
            continue
    return (player_life, enemy_life)

def game_results(player_victory, enemy_victory):
    if player_victory > enemy_victory :
        print(f'【Congratuations!】')
        return game_end("You won! Do you want to try again?")
    elif enemy_victory > player_victory:
        print('\n【You lost your life!】')
        return game_end("Unfortunately you lose... Do you want to try again?")
    print(' Whatever, gameover!')
    return game_end("Do you want to try again?")

def game_rounds(game_player, weapon, body_part):
    print("Winner would be greater score than loser")
    player_victory = 0
    enemy_victory = 0

    for i in range(1,4):
        print(f"  \n——————ROUND {i}——————")
        print("""
        The default is that you and other challengers have health value radomly between 100 and 150.
        Attacks are random between 30 and 50.
        When health value is less than or equal to 0, you have already lost your life. Game is over!
        """)
        player_life = random.randint(100,150)
        player_attack = random.randint(30,50)
        enemy_life = random.randint(100,150)
        enemy_attack = random.randint(30,50)

        game_info(game_player, player_life, player_attack, enemy_life, enemy_attack, i)
        input('<Press enter to start fighting>\n')
        player_life, enemy_life = game_round(game_player, player_life, player_attack, enemy_life, enemy_attack, weapon, i, body_part)

        if player_life >= 0 and enemy_life <= 0:
            player_victory += 1
            print(f'Congratuations! The opponent died, you win the {i} round！')
            continue
        elif player_life <= 0 and enemy_life >= 0:
            enemy_victory += 1
            print('Sorry you are killed！')
        else:
            print('Oppos! You were killed by each other ！')

    game_results(player_victory, enemy_victory)

game_start()
