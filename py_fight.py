import turtle
class Py_fight:
  def __init__(self):
    self.turtle = turtle.Turtle()
    self.turtle.hideturtle()
    self.turtle.penup()
    self.turtle.goto(-200 , 150)
    self.turtle.pendown()
  def py_den(self):
    turtle.Screen().bgcolor('black')
    self.turtle.color('gray')
    self.turtle.speed(0)
    for outside in range(4):
      self.turtle.forward(500)
      self.turtle.right(90)
  def python(self):
    self.t = turtle.Turtle()
    turtle.register_shape('green-snake.gif')
    self.t.shape('green-snake.gif')
    self.t.turtlesize(25)
    self.t.penup()
    self.t.goto(50 , -150)
    self.t.left(90)
  def py_fight(self , name , name_gender):
    while True:
      dodge = input('The dungeon creaters don\'t care enough to even put the right snake in the cave. ' + name + ' can tell that this is a Boa Constricter. ' + name + ' knows a lot about Boas. The Boa opens its mouth. ' + name + ' knows that it\'s about to strike. Dive or jump?\n')
      if 'jump' in dodge.lower():
        print(name + ' underestimates the size of the boa and tries to jump but doesn\'t even get close to clearing the leap. It injects venom into' + name + ' just before it swallows' + name + ' whole\nYOU LOSE!!!')
        break
      elif 'dive' in dodge.lower():
        self.t.forward(200)
        print(name + ' successfully dive under the boa. It bashes against the wall and boulders from the ceiling land on its head. ' + name + ' slipped through its grasp this time, but it will get ' + name + ' next time!!!')
        break
      else:
        print('That isn\'t an option. Try again.')
    while True:
      py_continue = input('Do you want to continue?/n')                      # py_fight_2?
      if 'no' in py_continue.lower() or 'not' in py_continue.lower():
        print('Okay, please come another day')
        break
      elif 'yes' in py_continue.lower() or 'sure' in py_continue.lower():
        print(name + ' realize that when the monsterous boa slammed into the wall, not only did boulders fall onto his head, but also fell right in front of the door, making it practically impossable to escape. ' + name + ' looked around to try to find another escape route. When ' + name + ' looked up, ' + name_gender + ' saw a sunroof. ' + name + ' immediately started planning.')
      else:
          print('That wasn\'t an option. Please try again.')