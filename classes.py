import turtle

screen = turtle.Screen()
screen.setup(1.0, 1.0)


class Map:  # This class uses Turtle to draw a map of rooms

    def __init__(self, room_size, n_rooms_axis):
        self.max_rooms_dimension = n_rooms_axis
        self.turtle = turtle.Turtle()
        self.turtle.speed(0)
        self.turtle.hideturtle()

        self.room_size = room_size
        self.rooms = []
        for i in range(n_rooms_axis):
            for j in range(n_rooms_axis):
                self.rooms.append([i - 1, j - 1])
                self._draw_room([i - 1, j - 1])
        self.player_location = [0, 0]
        self.turtle.showturtle()
        # lets draw the player now
        self.turtle.color('red')
        self.turtle.penup()
        self.turtle.shape('circle')  # change what turtle looks like
        self.turtle.goto(self.player_location[0] * room_size,
                         self.player_location[1] * room_size)
        self.turtle.left(90)
        # self.turtle.pendown()

    def clear_map(self):
        self.turtle.clear()

    def move_player(self, direction):
        print(f'Attempting to move player: {direction}')
        print(f'player location is: {self.player_location}')
        if direction.lower().startswith('n'):
            if self.player_location[1] > -1:
                self.turtle.forward(self.room_size)
                self.player_location[1] -= 1
            else:
                print(f"'{direction}'' is not a valid direction.")
        elif direction.lower().startswith('s'):
            if self.player_location[1] < self.max_rooms_dimension - 2:
                self.turtle.left(180)
                self.turtle.forward(self.room_size)
                self.turtle.right(180)
                self.player_location[1] += 1
            else:
                print(f"'{direction}'' is not a valid direction.")
        elif direction.lower().startswith('e'):
            if self.player_location[0] < self.max_rooms_dimension - 2:
                self.turtle.right(90)
                self.turtle.forward(self.room_size)
                self.turtle.left(90)
                self.player_location[0] += 1
            else:
                print(f"'{direction}'' is not a valid direction.")
        elif direction.lower().startswith('w'):
            if self.player_location[0] > -1:
                self.turtle.left(90)
                self.turtle.forward(self.room_size)
                self.turtle.right(90)
                self.player_location[0] -= 1
            else:
                print(f"'{direction}'' is not a valid direction.")

    def _draw_room(self, room_loc):
        self.turtle.penup()
        x = -self.room_size / 2 + self.room_size * room_loc[0]
        y = self.room_size / 2 + self.room_size * room_loc[1]
        self.turtle.goto(x, y)
        self.turtle.pendown()
        for i in range(4):
            self.turtle.forward(self.room_size)
            self.turtle.right(90)
        self.turtle.penup()


class Player:

    def __init__(self, start_room, map_scale, name, gender):
        self.loc = start_room  # location
        self.map_scale = map_scale
        self.n_lives = 1
        self.name = name  # player name
        self.gender = gender  # player gender
        # self.t = turtle.Turtle()
        self.inventory = []  # to keep track of items
        self.state = 'start room'  # game state
        # self.t.color('red')  # change the colour of the turtle
        # self.t.penup()
        # self.t.shape('circle')  # change what turtle looks like
        # self.t.goto(start_room[0] * map_scale, start_room[1] * map_scale)
        # self.t.left(90)

    # def move(self, direction):
    #     if direction == 'west':
    #         self.t.left(90)
    #         self.t.forward(self.map_scale)
    #         self.t.right(90)
    #         self.loc[0] -= 1
    #     elif direction == 'east':
    #         self.t.right(90)
    #         self.t.forward(self.map_scale)
    #         self.t.left(90)
    #         self.loc[0] += 1
    #     elif direction == 'south':
    #         self.t.left(180)
    #         self.t.forward(self.map_scale)
    #         self.t.right(180)
    #         self.loc[1] -= 1
    #     elif direction == 'north':
    #         self.t.forward(self.map_scale)
    #         self.loc[1] += 1

    def add_inventory(self, item):
        self.inventory.append(item)
