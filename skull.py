from turtle import Screen,Turtle
import time
screen=Screen()
screen.setup(width=1000,height=600)
screen.title("WELCOME TO DEATH")
screen.bgcolor("darkred")


sam=Turtle()
sam.hideturtle()

sam.pencolor("black")
sam.penup()
sam.goto(250,-250)
sam.write(f"☠️",font=("Courier",300,"normal"),align="center")
time.sleep(1.5)
sam.clear()




