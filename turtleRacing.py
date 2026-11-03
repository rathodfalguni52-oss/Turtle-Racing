import turtle
import time
import random

WIDTH,HEIGHT=500,500
COLORS=['red','green','blue','orange','yellow','black','purple','pink','brown','cyan']

def get_number_of_racers():
    racers=0
    while True:
        racers=input('Enter the number of racers (2 - 10):  ')
        if racers.isdigit():
            racers=int(racers) 
        else:
            print('Input is not numeric... Try Again!')
            continue

        if 2<= racers <=10:
            return racers
        else:
            print("Number not in range 2 - 10. Try Again !")

def create_turtles(colors):
    turtles=[]
    spacingx=WIDTH//(len(colors)+1)
    for i, color in enumerate(colors):
        racer=turtle.Turtle()
        racer.color(color)
        racer.shape('turtle')
        racer.left(90)
        racer.penup()
        racer.setpos(-WIDTH//2+(i+1)*spacingx,-HEIGHT//2+20)
        racer.pendown()
        turtles.append(racer)
    return turtles

def race(colors):
    turtles= create_turtles(colors)
    while True:
        for racer in turtles:
            distance=random.randrange(1,20)
            racer.forward(distance)

            x,y=racer.pos()
            if y>= HEIGHT//2-10:
                return colors[turtles.index(racer)]

def init_turtle():
    screen=turtle.Screen()
    screen.setup(WIDTH,HEIGHT)
    screen.title('Turtle Racing')

racers=get_number_of_racers()
init_turtle()

random.shuffle(COLORS)
# Example:  [1,2,3,4][:2] will give [1,2] 
colors=COLORS[:racers]
winner=race(colors)
print("The winner is the turtle with color:",winner)

# racer=turtle.Turtle()
# racer.speed(1)
# racer.penup()
# racer.shape('turtle')
# racer.color('pink')
# racer.forward(100)
# racer.left(90)
# racer.forward(100)
# racer.pendown()
# racer.right(90)
# racer.backward(100)

time.sleep(2)