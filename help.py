from turtle import Screen,Turtle
import time

screen=Screen()
screen.setup(width=1000,height=600)
screen.title("HELP BY RULES OF THE GAME")
screen.bgcolor("lightcyan1")


sam=Turtle()
sam.hideturtle()



def ready():
        sam.penup()
        sam.goto(0,-200)
        sam.pendown()
        sam.pencolor("red")
        sam.write("You Are Ready !!! 😎😎😎 ",align="center",font=("Arial",30,"normal"))
        time.sleep(1)
        sam.clear()




see_rules=screen.textinput("SEE RULES",prompt="DO YOU WANT OT SEE THE RULES:\n[Y/n]").lower()



while True:
    if see_rules in ["y","yes"]:

        sam.penup()
        sam.goto(-180,-50)
        sam.pencolor("blue")
        sam.pendown()
        sam.write(f""" 
                  

                  
                                        1. you will guess a letter depended on the space that appears to you
                  
                                        2. if your guess is wrong , a part of the peaniata appears
                  
                                        3. when the all peaniata appears you lose 🤔
                  
                                        4. else if your guess is right , you win 😎  
                                                         
                                        """,align="center",font=('Arial',25,'normal'))

        time.sleep(5)

        if screen.textinput("READY","ARE YOU READY?\n [Y/n]").lower()  in ["y","yes"]:
            ready()

            break

    else:
        ready()
        break












