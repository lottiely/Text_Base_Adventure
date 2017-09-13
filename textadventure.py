import tkinter

#Global Variables
#CharacterList
characters=["Diamond", "Spade", "Club", "Heart"]
deathCount = 0

#Button creation functions
#Delete buttons
def deletebtns(btns, func):
    for i in btns:
        i.pack_forget()

#Yes or no functions
def yes_no():
    btns=[
    tkinter.Button(window, text="Yes", font=("Courier", 12), fg="#a1dbcd", bg="#383a39", width=12),
    tkinter.Button(window, text="No", font=("Courier", 12), fg="#a1dbcd", bg="#383a39", width=12)]
    return btns

#Choice buttons
def choices(num):
    btns = []
    for i in range (0, num):
        btns.append(tkinter.Button(window, text="", font=("Courier", 10), fg="#a1dbcd", bg="#383a39",
                                   wraplength=window.winfo_width()))
    return btns


#Story Functions
#Opening
def chooseChar(text):
    text['text'] = ("Choose your character: ")
    btns =[]
    for i in characters:
        btns.append(
            tkinter.Button(window, text=i, font=("Courier", 16), fg="#a1dbcd", bg="#383a39", width=12,command =lambda i=i: prologue(characters.index(i), text, btns)))
        btns[characters.index(i)].pack(pady=2)

#Prologue
def prologue(characterindex, text, btns):
    position = ""
    description = ""
    text.config(font=10, wraplength= window.winfo_width())
    for i in btns:
        i.pack_forget()
    btns.clear()
    btns = yes_no()

    if characterindex == 0:
        description = "unpredictable and clever. \n"
        position = "where people are distrustful of you. \n"
        # Prepare yes or no buttons
        btns[0].config(command=lambda: deletebtns(btns, diamondPrologue(text)))
        btns[1].config(command=lambda: deletebtns(btns, chooseChar(text)))

    elif characterindex == 1:
        description = "reliable and skilled.\n"
        position = "where you people look to you for protection. \n"
        #Prepare yes or no buttons
        btns[0].config(command=lambda: deletebtns(btns, spadePrologue(text)))
        btns[1].config(command=lambda: deletebtns(btns, chooseChar(text)))

    elif characterindex == 2:
        description = "wild and powerful \n"
        position = "where people fear you. \n"
        # Prepare yes or no buttons
        btns[0].config(command=lambda: deletebtns(btns, clubPrologue(text)))
        btns[1].config(command=lambda: deletebtns(btns, chooseChar(text)))

    elif characterindex == 3:
        description = "intelligent and resourceful. \n"
        position = "where people look to you for help and wisdom. \n"
        # Prepare yes or no buttons
        btns[0].config(command=lambda: deletebtns(btns, heartPrologue(text)))
        btns[1].config(command=lambda: deletebtns(btns, chooseChar(text)))

    else:
        text['text'] = "Error"

    for i in btns:
        i.pack(pady=2)

    #Main text
    text['text'] = ("You have chosen " + characters[characterindex] + "\n"
                    "This character is known for being " + description +
                    "You will start in a position " + position +
                    "Are you sure you want this character?")

def diamondPrologue(text):
    characterName = characters[0]
    text['text'] = ("You are stuck in a prison cell. You can pick locks, but timing is important to escape. "
                    "You know that they are preparing your execution soon. When is the best time to escape?")
    btns = choices(4)
    btns[0]['text'] = "Right now, while no one is here."
    btns[0].config(command=lambda: deletebtns(btns, gameOver(text, "You pick the lock and attempt your escape "
                                                                   "only to run into the guard coming to retrieve "
                                                                   "you for your execution. Unprepared for battle, "
                                                                   "you are caught by the guard and executed.")))

    btns[1]['text'] = "Wait for the guard, and kill him when he tries to leave."

    btns[2]['text'] = "Wait for the guard, and escape after the guard has left."
    btns[3]['text'] = "Why worry about it? Escape when there are more options."

    for i in btns:
        i.pack(pady=2)

def spadePrologue(text):
    characterName = characters[1]
    text['text'] = ("You have chosen Spade. \n"
                    "You will start in a position where you have the power to uphold justice and fairness. \n"
                    "Are you sure you want this character?")
def clubPrologue(text):
    characterName = characters[2]
    text['text'] = ("You have chosen Club. \n"
                    "You will start in a position at the beginning of an adventure, ready to make a name for yourself.")
def heartPrologue(text):
    characterName = characters[3]
    text['text'] = ("You have chosen Heart. \n"
                    "You will start in a position where you ")

#Game Over
def gameOver(text, gameovertext):
    text['text'] = gameovertext
    global deathCount
    deathCount += 1
    thelabel = "Death Count : \n" + str(deathCount)
    counter = tkinter.Label(window, text= thelabel, fg="#282828", bg="#8E8E8E", font=("Courier", 30))
    counter.pack(pady=2)
    btn = choices(1)
    btn[0].config(text="Return to Title Screen", command=lambda: endgame(text, counter, deletebtns(btn, titleScreen())))
    btn[0].pack(pady=2)

def endgame(text, counter, deletebtns):
    text.pack_forget()
    counter.pack_forget()

#create the window
window = tkinter.Tk()

#modify root window
window.configure(background="#800000")
window.title("Text Based Adventure")
window.geometry("500x300")

#Title screen functions
def startbtn(title, start):
    title.pack_forget()
    start.pack_forget()
    gamescreen()

#title screen content
def titleScreen():
    title = tkinter.Label(window, text="Text Based Adventure", fg="#282828", bg="#8E8E8E", font=("Courier", 30))
    title.pack(pady=30)

    start = tkinter.Button(window, text = "Start", font=("Courier", 20), fg ="#a1dbcd", bg="#383a39", height=2, width=12,
                           command=lambda: startbtn(title, start))
    start.pack(pady=10)

#game screen
def gamescreen():
    text = tkinter.Label(window, text="", fg="#282828", bg="#8E8E8E", font=("Courier", 24))
    text.pack(pady=10)
    chooseChar(text)

#reset
def deathreset():
    window.destroy()

titleScreen()
window.mainloop()