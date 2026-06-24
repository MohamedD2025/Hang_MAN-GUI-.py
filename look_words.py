from turtle import Turtle,Screen

from words import words
import time

screen=Screen()
screen.title("LOOK AT WORDS")
screen.setup(width=1000,height=800)
screen.bgcolor("lightcyan1")


sam=Turtle()
sam.hideturtle()
sam.penup()
sam.goto(0,240)
sam.pendown()
sam.pencolor("brown")
sam.write(f"{len(words)} WORDS:\n",font=("Courier",40,"bold"),align="center")

step_down=21
sam.pencolor("black")
for word in words[:30]:
    sam.penup()
    sam.goto(-200,sam.ycor()-step_down)
    sam.pendown()
    sam.write(f"{word} ",font=("Arial",20,"normal"),align="center")


sam.penup()
sam.goto(sam.xcor()+100,240)
for word in words[30:60]:
    sam.penup()
    sam.goto(sam.xcor(),sam.ycor()-step_down)
    sam.pendown()
    sam.write(f"{word} ",font=("Arial",20,"normal"),align="center")



sam.penup()
sam.goto(sam.xcor()+100,240)
for word in words[60:90]:
    sam.penup()
    sam.goto(sam.xcor(),sam.ycor()-step_down)
    sam.pendown()
    sam.write(f"{word} ",font=("Arial",20,"normal"),align="center")



sam.penup()
sam.goto(sam.xcor()+100,240)
for word in words[90:]:
    sam.penup()
    sam.goto(sam.xcor(),sam.ycor()-step_down)
    sam.pendown()
    sam.write(f"{word} ",font=("Arial",20,"normal"),align="center")


time.sleep(7)
sam.clear()





















