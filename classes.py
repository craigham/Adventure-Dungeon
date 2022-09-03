import turtle
screen = turtle.Screen()
screen.setup(1.0 , 1.0)
class Map:                         # This class uses Turtle to draw a map of rooms
  def __init__(self, room_size):
    self.turtle = turtle.Turtle()
    self.turtle.speed(0)
    self.rooms = [[0, 0]]
    self.turtle.hideturtle()
    self.room_size = room_size
  def add_room(self , room_loc):
    self.rooms.append(room_loc)
  def clear_map(self):
    self.turtle.clear()
  def draw_room(self, room_loc):
    self.turtle.penup()
    x = -self.room_size/2 + self.room_size * room_loc[0]
    y = self.room_size/2 + self.room_size * room_loc[1]
    self.turtle.goto(x , y)
    self.turtle.pendown()
    for i in range(4):
      self.turtle.forward(self.room_size)
      self.turtle.right(90)
    self.turtle.penup()
  def draw_map(self):
    for room in self.rooms:
      self.draw_room(room)
class Player:
  def __init__(self , start_room , map_scale):
    self.loc = start_room             # location
    self.map_scale = map_scale
    self.life = 1
    self.inventory = []               # to keep track of items
    self.state ='start room'         # game state
    self.t = turtle.Turtle()
    self.t.color('red')
    self.t.penup()
    self.t.shape('circle')            # change what turtle looks like
    self.t.goto(start_room[0] * map_scale , start_room[1] * map_scale)
    self.t.left(90)                   
  def move(self , direction):
    if direction == 'west':
      self.t.left(90)
      self.t.forward(self.map_scale)
      self.t.right(90)
      self.loc[0] -= 1
    elif direction == 'east':
      self.t.right(90)
      self.t.forward(self.map_scale)
      self.t.left(90)
      self.loc[0] += 1
    elif direction == 'south':
      self.t.left(180)
      self.t.forward(self.map_scale)
      self.t.right(180)
      self.loc[1] -= 1
    elif direction == 'north':
      self.t.forward(self.map_scale)
      self.loc[1] += 1
  def add_inventory(self , item):
    self.inventory.append(item)