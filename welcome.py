from turtle import Turtle,Screen
import time


screen=Screen()
screen.setup(width=1000,height=600)
screen.title("WELCOME USER")
screen.bgcolor("lightcyan1")

sam=Turtle()
sam.hideturtle()
sam.pencolor("brown")
sam.penup()
sam.goto(x=0,y=260)
sam.write(f"-"*15+"WELCOME USER"+"-"*15,font=("Courier",30,"normal"),align="center")

time.sleep(1.5)
sam.clear()