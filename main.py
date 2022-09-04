from classes import Player, Map
from py_fight import PyFight
from random import randint
import time

def start_game():
    debug = False
    room_size = 100
    # set up a map with 3x3 rooms
    my_map = Map(room_size, n_rooms_axis=3)

    text = ''
    if debug:
        name = 'The Operator'
        gender = 'The Operator'
        gender2 = 'The Operator\'s'
        player = Player([0, 0], room_size, name, gender)
        choice = input('What are you testing?\n')
    else:
        print('Welcome to Adventure Dungeon!\n')
        time.sleep(1.5)
        name = input('What is your adventurer\'s name?\n')
        gender = input('He or she?\n')
        if gender == 'He':
            gender2 = 'his'
        elif gender == 'She':
            gender2 = 'her'
        else:
            print('Sorry, but we must ask you to do that again.\n')
        player = Player([0, 0], room_size, name, gender)
        text = '\n' + name + ' is in a dimly lit room. There is a door to the north, south, east, and west.'
        print(text)
        choice = input('Which way should ' + name + ' go?\n')

    while choice != 'quit' and player.n_lives > 0:
        prompt = 'What will ' + name + ' do next?\n'
        if debug:
            if 'life orb' in choice:
                player.move('south')
                player.move('west')
                player.state = ('southwest room')
                print('Went southwest to Life Orb')
            elif 'py fight 2' in choice:
                print('Skipped to Py Fight 2')
            elif 'py fight 1' in choice:
                player.state = 'north room'
                player.move('north')
                choice = 'enter'
                print('Skipped to Py Fight 1')
        if player.state == 'start room':
            if 'north' in choice:
                if debug:
                    print('Went north')
                player.move('north')
                player.state = 'north room'
                text = '\n' + name + ' sees a door'
            elif 'south' in choice:
                if debug:
                    print('Went south')
                player.move('south')
                player.state = 'south room'
                text = name + ' sees a chest a few steps away.'
            elif 'east' in choice:
                if debug:
                    print('Went east')
                player.move('east')
                player.state = 'east room'
                text = name + ' is in the west room\n'
            elif 'west' in choice:
                if debug:
                    print('Went west')
                player.move('west')
                player.state = 'west room'
                text = name + ' is in the west room\n'
            else:
                print('\nThat wasn\'t an option. Try again:')
        elif player.state == 'north room':
            if 'south' in choice:
                player.move('south')
                player.state = 'start room'
                text = name + ' is in the room ' + gender.lower() + 'started from.'
            elif 'enter' in choice or 'open' in choice or 'kick' in choice or 'knock' in choice or 'ram' in choice or 'door' in choice:
                print(name + ' creaks open the door to discover a giant python! It looks ready for a fight!')
                my_map.clear_map()
                fight = PyFight(name, gender)
                fight.py_den()
                fight.python()
                fight.py_fight(name, gender, player)
                break
            elif 'west' in choice:
                player.move('west')
                player.state = 'northwest room'
                text = 'You are in the northwest room'
        elif player.state == 'south room':
            if 'north' in choice:
                player.move('north')
                player.state = 'start room'
                text = name + ' is in the room ' + gender.lower() + ' started from.'
            elif 'open' in choice:
                text = name + ' opens the treasure chest to discover a weird shiny object that looked like a big necklace. ' + name + ' puts it on, but quickly realizes that it is too heavy. ' + name + ' just puts it in ' + gender2 + ' backpack'
                player.add_inventory('Strength Necklace')
        elif player.state == 'west room':
            if 'east' in choice:
                player.move('east')
                player.state = 'start room'
                text = name + ' is in the room ' + gender.lower() + ' started from.'
            elif 'north' in choice:
                player.move('north')
                player.state = 'northwest room'
                text = name + 'is in the northwest room.'
            elif 'south' in choice:
                if debug:
                    print('Went south')
                player.move('south')
                player.state = 'southwest room'
                text = name + ' spots a glowing orange orb in the center of the room.'
        elif player.state == 'southwest room':
            if 'north' in choice:
                player.move('north')
                player.state = 'west room'
                text = name + 'is in the west room'
            elif 'grab' in choice:
                if randint(1, 2) == 2:
                    player.n_lives += 1
                    print('You got lucky and gained a life.')
                else:
                    player.n_lives -= 1
                    print('You got unlucky and lost a life.')
                print(f'Player life is: {player.n_lives}')
            elif 'east' in choice:
                player.move('east')
                player.state = 'south room'
                text = name + ' sees a chest a few steps away.'
        elif player.state == 'northwest room':
            if 'south' in choice:
                player.move('south')
                player.state = 'west room'
                text = name + 'is in the west room'
        else:
            print('\nThat wasn\'t an option. Try again:')
        print(text)
        choice = input(prompt).lower()
start_game()