import time
from turtle import Screen,Turtle
from words import words
import welcome
import help
import look_words
import skull
from stages import hangman_stages
import random

window=Screen()
window.setup(width=1000,height=600)
window.title("HANG MAN GAME")
window.bgcolor("lightcyan1")
window.tracer(0)

sam=Turtle()
sam.hideturtle()


random_word=random.choice(words)
show_spaces=["_"]*len(random_word)
sam.penup()
sam.goto(0,0)
sam.pendown()
sam.write(f"{hangman_stages[0]}",font=("Courier",30,"normal"),align="center")
sam.penup()
sam.goto(0,-180)
sam.pendown()
sam.write(f" ".join(show_spaces),align="center",font=("Courier",30,"bold"))
lives=6
guessed_letters=[]


def reset_ever_thing():
        sam.clear()
        sam.penup()
        sam.goto(0,0)
        sam.pendown()
        window.clear()
        window.bgcolor("lightcyan1")
        sam.penup()
        sam.goto(0,0)
        sam.pendown()
        sam.pencolor("black")
        sam.write(f"{hangman_stages[6-lives]}",font=("Courier",30,"normal"),align="center")
        sam.penup()
        sam.goto(0,-180)
        sam.pendown()
        sam.write(f" ".join(show_spaces),align="center",font=("Courier",30,"bold"))


while "_" in show_spaces and lives>0:
    window.update()
    sam.penup()
    sam.goto(400,260)
    sam.pendown()
    sam.pencolor("green")
    sam.write(f"LIVES: {lives}",font=("Courier",25,"bold"),align="center")
    if guessed_letters:
        sam.penup()
        sam.goto(-310,200)
        sam.pencolor("brown")
        sam.pendown()
    
        sam.write(f"You Guessed: "+", ".join(guessed_letters),font=("Courier",16,"normal"),align="center")
        time.sleep(0.8)
    guessed=window.textinput(title="GUESS A LETTER",prompt="Please, Guess a Letter\n").lower()


    if guessed in guessed_letters:
        
        reset_ever_thing()
        continue
    guessed_letters.append(guessed)
    

    if guessed not in random_word:
        lives-=1
        
        reset_ever_thing()


    else:
        for letter in range(len(random_word)):
            if random_word[letter]==guessed:
                show_spaces[letter]=guessed
                reset_ever_thing()
                
        sam.penup()
        sam.pencolor("black")
        sam.goto(0,-180)
        sam.pendown()
        
    sam.write(f" ".join(show_spaces),align="center",font=("Courier",30,"bold"))


time.sleep(1)
window.clear()
sam.penup()
sam.goto(0,0)
sam.pendown()


if lives==0:
    window.bgcolor("red")
    sam.pencolor("black")
    sam.write(f"YOU LOSE ☠️☠️☠️☠️☠️\n",align="center",font=("Courier",40,"bold"))

else:

    window.bgcolor("lightgreen")
    sam.pencolor("white")
    sam.write(f"YOU WIN 💎💎💎💎💎💎\n ",align="center",font=("Courier",40,"bold"))




sam.penup()
sam.goto(0,0)
sam.pendown()
sam.pencolor("black")
sam.write(f"The Word: {random_word}",font=("Courier",40,"normal"),align="center")


window.exitonclick()