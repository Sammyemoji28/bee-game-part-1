
import pgzrun
import random

HEIGHT = 500
WIDTH = 600

bee = Actor("bee")
bee.pos = (293,208)

flower = Actor("flower")
flower.pos = (192,420)

score = 0
gameover = False

def draw():
    screen.blit("grass",(0,0))
    bee.draw()
    flower.draw()
    screen.draw.text("Score: {}".format(score),fontsize = 45, topleft = (30,30))

def flowerPos():
    flower.x = random.randint(50,550)
    flower.y = random.randint(50,450)

def update():
    if keyboard.left:
        bee.x = bee.x - 5
    if keyboard.right:
        bee.x = bee.x + 5
    if keyboard.up:
        bee.y = bee.y - 5
    if keyboard.down:
        bee.y = bee.y + 5

pgzrun.go()