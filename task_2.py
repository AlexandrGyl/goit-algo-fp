import turtle
screen = turtle.Screen() # Create the screen.
screen.setup(320, 320)   # Set Window size.


TTL = turtle.Turtle()
TTL.speed(0) 
TTL.color("brown") 
TTL.pensize(1) 

TTL.penup() 
TTL.setposition(0, -100)
TTL.pendown() 
TTL.hideturtle()
TTL.setheading(90)

###### VARIABLES ######
# Variable 'branchLength' is the starting length of tree brach.
# Variable 'branchReduction' subtracts from 'branchLength' in
# each recursion iteration.
# Variable 'recursionLevel' is the recursion iteration number.

###### DEFINE treeFractal FUNCTION ######
# Draw a fractal with recursion level, tree branch length,
# branch length reduction for each iteration, and
# the angle by which the branch turns each iteration.
def treeFractal(TTL, recursionLevel, branchLength, branchReduction, angle):
  if recursionLevel == 0:
    TTL.fd(0)
  else:
    branchLength = branchLength - branchReduction
    TTL.forward(branchLength)
    TTL.left(angle)
    treeFractal(TTL, recursionLevel-1, branchLength, branchReduction, angle)
    TTL.right(angle * 2)
    treeFractal(TTL, recursionLevel-1, branchLength, branchReduction, angle)
    TTL.left(angle)
    TTL.backward(branchLength)
# 
#  
# Branch length = 50.
# Branch reduction each recursion iteration = 5.
# Turn left of right angle by 45 degrees.
recursion_level = int(input("Введіть рівень рекурсії: "))

treeFractal(TTL, recursion_level, 50, 5, 45)

screen.exitonclick() # Exit screen