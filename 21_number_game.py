import random
import time

#####
def nearestMultiple(n):
    return 4 - (n%4) if ((n%4) != 0) else random.choice([1,2,3])
#####

#####
def startGame(usr_turn):
    result = 0
    while True:
        if result == 20 or result == 21:
            print('\nCongratulation! You' if not usr_turn else '\nComputer', 'Win')
            return 0 # exit with code 0

        if usr_turn:
            usr_turn = False

            print('\nYour Turn\n')
            print('Enter a number between (1, 3)')
            res = ''
            while True: 
                res = input('> ')
                if (not res.isdecimal()) or (int(res) > 3) or (int(res) <= 0):
                    continue
                else: break
            result += int(res)

        else:
            usr_turn = True

            print('\nComputer Turn\n')
            print('Thinking...')
            time.sleep(2)
            
            # computer always wins except usr starts second, then computer will choose a random number
            # between (1, 2, 3) and usr will win the game
            if result == 0: comp_choice = random.choice([1,2,3])
            else: comp_choice = nearestMultiple(result)
            
            print('Computer choosed number', comp_choice)
            result += comp_choice

        print('Result:', result)
#####

#####
def init():
    usr_turn = True

    usr_game_starter = ''
    while True:
        usr_game_starter = input('Do you want to start the game? (Yes/No): ').lower()
        
        if not (usr_game_starter == 'yes' or usr_game_starter == 'no'):
            print('*'*11 + '\nWRONG INPUT\n' + '*'*11)
        else: break
    
    if usr_game_starter == 'yes':
        usr_turn == True

    else: # usr_game_starter equals 'no'
        usr_turn = False

    startGame(usr_turn)

#####

init()