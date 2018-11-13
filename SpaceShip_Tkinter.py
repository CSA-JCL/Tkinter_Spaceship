# Jack Lawrence
# 11th Advanced Programming`
# 11/12/2018


# Version 1.0

from tkinter import *
from tkinter import ttk

window = Tk()
window.title("Spaceship")
window.geometry('350x175')

window2 = Toplevel()
window2.title('Spaceship_Game_Start')
window2.geometry("500x200")

window3 = Toplevel()
window3.title('INFO')
window3.geometry("350x200")

window4 = Toplevel()
window4.title('INFO')
window4.geometry("350x200")

window5 = Toplevel()
window5.title('INFO')
window5.geometry("350x200")


scoretxt = StringVar()
scoretxt.set(0)
labeltxt = StringVar()
var1 = StringVar()
var2 = StringVar()
var3 = StringVar()
global PLANET
esc = 11.186
# All of this sets up important variables
global CODE
global POINTS
POINTS = int(0)


def restart():  # Resets important values when the player chooses to restart
    global PLANET
    global POINTS
    scoretxt.set(0)
    labeltxt.set("Earth")
    window3.withdraw()
    window4.withdraw()
    window2.deiconify()

def escapespeed(SPEED, GOTO):  # Defines the esc variable
    global PLANET
    global esc
    global CODE
    global POINTS
    if PLANET == "Earth":
        esc = 11.186
    elif PLANET == "Mercury":
        esc = 4.25
    elif PLANET == "Venus":
        esc = 10.36
    elif PLANET == "Mars":
        esc = 5.03
    elif PLANET == "Jupiter":
        esc = 60.20
    elif PLANET == "Saturn":
        esc = 36.09
    elif PLANET == "Uranus":
        esc = 21.38
    elif PLANET == "Neptune":
        esc = 23.56
    elif PLANET == "Pluto":
        esc = 1.23

def check(SPEED,GOTO):  # Checks for correct escape speed and continues if they succeed or asks if they want to restart if they fail
    global PLANET
    global esc
    global CODE
    global POINTS
    if SPEED > (esc * 1.1):  # Crashes if they went to fast
        PLANET = GOTO
        var1.set("You went too fast and crashed on " + PLANET + " You failed.")
        window3.deiconify()
        window2.withdraw()
    elif SPEED >= esc and SPEED <= (esc * 1.1):
        PLANET = GOTO
        var3.set("You made it! You landed on " + PLANET + "!")
        labeltxt.set(PLANET)
        window5.deiconify()

        POINTS = POINTS + 10  # Gives the user +10 points
        scoretxt.set(str(POINTS))
    elif SPEED < esc:  # Crashes back on the current planet if they went to slow

        var2.set("You went too slow and crashed back on " + PLANET + " You failed.")
        window4.deiconify()
        window2.withdraw()



def ok():
    txt = options.get()
    labeltxt.set(txt)
    options2.set(txt)
    window2.deiconify()
    window.withdraw()
    return


def close():
    sys.exit()

def back():
    window5.withdraw()

def LIFTOFF():
    global PLANET
    PLANET = str(labeltxt.get())
    SPEED = float(note.get("1.0", 'end-1c'))
    GOTO = options2.get()
    escapespeed(SPEED, GOTO)  # Defines the esc value not noticable by the player
    check(SPEED, GOTO)
    print("")



options = StringVar()
options2 = StringVar()




options.set("Earth")

optiones = ("Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune", "Pluto")
choices = ttk.Combobox(window, textvariable=options, state='readonly', values=optiones)
choices.bind("<<ComboboxSelected>>")
choices.grid(row=0, column=0, sticky=(N, W),pady=10)

note = Text(window2, height=1, width=12)
note.grid(column=3, row=1)

options2.set(choices.get())
optiones2 = ("Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune", "Pluto")
choices2 = ttk.Combobox(window2, textvariable=options2, state='readonly', values=optiones2)
choices2.bind("<<ComboboxSelected>>")
choices2.grid(row=0, column=0, sticky=(N, W))

speed_label = ttk.Label(window2, text="Escape Speed (KM/S)")
speed_label.grid(row=0,column = 3, padx = 10)
current=ttk.Label(window2, text ="Current Planet:")
current.grid(row=3, column=2)
current_planet=ttk.Label(window2, text =choices2.get(),textvariable=labeltxt)
current_planet.grid(row=3, column=3)
score_label = ttk.Label(window2, text="Score:")
score_label.grid(row=5, column=2)
current_score=ttk.Label(window2, text='0',textvariable=scoretxt)
current_score.grid(row=5, column=3)


toofast = Label(window3,text='', textvariable=var1).grid(row=0,column=0,padx=40)
restartlabeltwo= Label(window3, text ="Do you Wish to Restart From Earth?").grid(row=1, column=0)
No1 = Button(window3, text="No",command=close).grid(row=5,column=0,pady=10)
Yes1 = Button(window3, text ="Yes", command=restart).grid(row=6,column=0)

tooslow = Label(window4,text='', textvariable= var2).grid(row=0,column=0,padx=40)
restartlabelone= Label(window4, text ="Do you Wish to Restart From Earth?").grid(row=1, column=0)
No2 = Button(window4, text="No",command=close).grid(row=5,column=0,pady=10)
Yes2 = Button(window4, text ="Yes", command=restart).grid(row=6,column=0)
madeit = Label(window5,text='', textvariable=var3).grid(row=0,column=0,padx=40)
Back = Button(window5, text="Close",command=back).grid(row=5,column=0,pady=10)


introtxt1 = "Hello, The goal of this game is to leave the planet"
introtxt2 = "via your spaceship and go to other planets, getting"
introtxt3 = "points along the way!"

ok = Button(window, text="Start!", command=ok).grid(row=0,column=0,padx=20,pady=10,sticky="E")
intro1 = Label(window, text=introtxt1).grid(row=4, column=0, padx=0,sticky="W")
intro2 = Label(window, text=introtxt2).grid(row=5, column=0, padx=0,sticky="W")
intro3 = Label(window, text=introtxt3).grid(row=6, column=0, padx=0,sticky="W")



Launch = Button(window2, text='Launch', command=LIFTOFF).grid(row=0, column=2, padx=10)

window2.withdraw()
window3.withdraw()
window4.withdraw()
window5.withdraw()
window.mainloop()


