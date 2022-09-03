from classes import Player, Map
from py_fight import Py_fight
from random import randint
import time
def start_game():
  debug = True
  map_size = 100
  my_map = Map(map_size)
  my_map.add_room([1, 0])
  my_map.add_room([1, 1])
  my_map.add_room([0, 1])
  my_map.add_room([1, -1])
  my_map.add_room([-1, 1])
  my_map.add_room([-1, -1])
  my_map.add_room([0, -1])
  my_map.add_room([-1, 0])
  my_map.draw_map()
  player = Player([0, 0], map_size)
  text = ''
  if debug:
    name = 'The Operator'
    name_gender = 'The Operator'
    name_gender2 = 'The Operator\'s'
    choice = input('What are you testing?\n')
  else:
    print('Welcome to Adveture Dungeon!\n')
    time.sleep(1.5)
    name = input('What is your adventurer\'s name?\n')
    name_gender = input('He or she?\n')
    if name_gender == 'He':
      name_gender2 = 'his'
    elif name_gender == 'She':
      name_gender2 = 'her'
    else:
      print('Sorry, but we must ask you to do that again.\n')
    text = '\n' + name + ' is in a dimly lit room. There is a door to the north, south, east, and west.'
    print(text)
    choice = input('Which way should ' + name + ' go?\n')
  while choice.lower() != 'quit' and player.life > 0:
    prompt = 'What will ' + name + ' do next?\n'
    if debug:
      if 'test life orb' in choice.lower():
        player.move('south')
        player.move('west')
        player.state = ('southwest room')
        print('Went southwest to Life Orb')
      elif 'test py fight 2' in choice.lower():
        print('Skipped to Py Fight 2')
    if player.state == 'start room':
      if 'north' in choice.lower():
        if debug:
          print('Went north')
        player.move('north')
        player.state = 'north room'
        text = '\n' + name + ' sees a door'
      elif 'south' in choice.lower():
        if debug:
          print('Went south')
        player.move('south')
        player.state = 'south room'
        text = name + ' sees a chest a few steps away.'
      elif 'east' in choice.lower():
        if debug:
          print('Went east')
        player.move('east')
        player.state = 'east room'
      elif 'west' in choice.lower():
        if debug:
          print('Went west')
        player.move('west')
        player.state = 'west room'
        text = name + ' is in the west room\n'
      else:
        print('\nThat wasn\'t an option. Try again:')
    elif player.state == 'north room':
      if 'south' in choice.lower():
        player.move('south')
        player.state = 'start room'
        text = name + ' is in the room ' + name_gender + ' started from.'
      elif 'enter' in choice.lower() or 'open' in choice.lower() or 'kick' in choice.lower() or 'knock' in choice.lower() or 'ram' in choice.lower() or 'door' in choice.lower():
        print('' + name + ' creaks open the door to discover a giant python! It looks ready for a fight!')
        my_map.clear_map()
        fight = Py_fight(name_gender)
        fight.py_den()
        fight.python()
        fight.py_fight(name)
        break
      elif 'west' in choice.lower():
        player.move('west')
        player.state = 'northwest room'
        text = 'You are in the northwest room'
    elif player.state == 'south room':
      if 'north' in choice.lower():
        player.move('north')
        player.state = 'start room'
        text = name + ' is in the room ' + name_gender + ' started from.'
      elif 'open' in choice.lower():
        text = name + ' opens the treasure chest to discover a weird shiny object that looked like a big necklace. ' + name + ' puts it on, but quickly realizes that it is too heavy. ' + name + ' just puts it in ' + name_gender2 + ' backpack'
        player.add_inventory('Strength Necklace')
    elif player.state == 'west room':
        if 'east' in choice.lower():
          player.move('east')
          player.state = 'start room'
          text = name + ' is in the room ' + name_gender + ' started from.'
        elif 'north' in choice.lower():
          player.move('north')
          player.state = 'northwest room'
          text = name + 'is in the northwest room.'
        elif 'south' in choice.lower():
          if debug:
            print('Went south')
          player.move('south')
          player.state = 'southwest room'
          text = name + ' spots a glowing orange orb in the center of the room.'
    elif player.state == 'southwest room':
        if 'north' in choice.lower():
          player.move('north')
          player.state = 'west room'
          text = name + 'is in the west room'
        elif 'grab' in choice.lower():
          if randint(1 , 2) == 2:
            player.life += 1
            print('You got lucky and gained a life.')
          else:
            player.life -= 1
            print('You got unlucky and lost a life.')
            
          print(f'Player life is: {player.life}')            
    elif player.state == 'northwest room':
      if 'south' in choice.lower():
        player.move('south')
        player.state = 'west room'
        text = name + 'is in the west room'
    else:
      print('\nThat wasn\'t an option. Try again:')
    print(text)
    choice = input(prompt)
start_game()