#First of all we need to import all the required libraries 
#required to make this project.
#Tkinter is the GUI library for this game
from tkinter import*
#Threading is used to run some background threads,
#Here I've used this to make delay in computer's turn.
from threading import Thread
#I'm importing time library to make 2 seconds delay whe there is computer's turn.
#Just to make like computer is thinking and making decisions, but that's not real
from time import sleep
#Importing os library to check whether your nickname is saves or not
#Random is used by the computer t select some random grids while playing with computer.
import os, random
#Below code is for some geometry management, placing window in the center of the screen
#when first opened, and for setting specific width and height of the window
root = Tk()
root.resizable(0,0)
window_width = 800
window_height = 500
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
root.title("Tic Tac Toe")
try:root.iconbitmap("icon.ico")
except:pass
position_top = int(screen_height / 2 - window_height / 2)
position_right = int(screen_width / 2 - window_width / 2)
root.geometry(f'{window_width}x{window_height}+{position_right}+{position_top}')
bgColor = "#262626"
root.config(background=bgColor)
#Here are some variables used in this game.
############# SOME VARIABLES ###############################################
username = os.path.split(os.path.expanduser('~'))[-1]
scorePath = f"C:\\Users\\{username}"
nickNameEntry = StringVar()
characterX = IntVar(value=1)
characterO = IntVar()
sComputer = IntVar(value=1)
sFriend = IntVar()
myChar = "X"
otherChar = "O"
nowTurn = otherChar
gridCount = 0
noWinner = True
allGrids = [1,2,3,4,5,6,7,8,9]
myCharGrids = []
otherCharGrids = []
playing = False
noOfVictory = 0
noOfLooses = 0
if os.path.isfile(f"{scorePath}\\score"):
    getScore = open(f"{scorePath}\\score","r").read()
    getScore = getScore.split("|")
    if len(getScore) == 2:
        noOfVictory = getScore[0]
        noOfLooses = getScore[1]
############################################################################
#It's boring to write comments on each and every functions, I'm stopping commenting from here.
#The code is very simple and anyone with basic programming skills can easily understand the logic.
############################################################################
def showAlertMessage(msg):
    global toShow
    toShow = msg
    infoThread()
############################################################################
############################################################################
def showInfo():
    alertLabel.config(text=toShow)
    sleep(1)
    alertLabel.config(text="")
def infoThread():
    thread = Thread(target=showInfo)
    thread.start()
############################################################################
############################################################################
def disableAll():
    gridone.config(state=DISABLED)
    gridtwo.config(state=DISABLED)
    gridthree.config(state=DISABLED)
    gridfour.config(state=DISABLED)
    gridfive.config(state=DISABLED)
    gridsix.config(state=DISABLED)
    gridseven.config(state=DISABLED)
    grideight.config(state=DISABLED)
    gridnine.config(state=DISABLED)
############################################################################
############################################################################
def enableAll():
    gridone.config(state=NORMAL)
    gridtwo.config(state=NORMAL)
    gridthree.config(state=NORMAL)
    gridfour.config(state=NORMAL)
    gridfive.config(state=NORMAL)
    gridsix.config(state=NORMAL)
    gridseven.config(state=NORMAL)
    grideight.config(state=NORMAL)
    gridnine.config(state=NORMAL)
############################################################################
############################################################################
def selectXchar():
    global myChar, otherChar, nowTurn
    nowTurn = "O"
    myChar = "X"
    otherChar = "O"
    characterO.set(0)
    youLabel.config(text="You: X")
    if sComputer.get() == 1:frLabel.config(text="Computer: O")
    else:frLabel.config(text="Friend: O")
    oCheckBtn.config(state=NORMAL)
    xCheckBtn.config(state=DISABLED)
def selectOchar():
    global myChar, otherChar, nowTurn
    nowTurn = "X"
    myChar = "O"
    otherChar = "X"
    characterX.set(0)
    youLabel.config(text="You: O")
    if sComputer.get() == 1:frLabel.config(text="Computer: X")
    else:frLabel.config(text="Friend: X")
    xCheckBtn.config(state=NORMAL)
    oCheckBtn.config(state=DISABLED)
############################################################################
############################################################################
def selectComputer():
    sFriend.set(0)
    frendLabel.config(text="Playing with: Computer")
    computer.config(state=DISABLED)
    friend.config(state=NORMAL)
    frLabel.config(text=f"Computer: {otherChar}")
def selectFriend():
    sComputer.set(0)
    frendLabel.config(text="Playing with: Friend")
    computer.config(state=NORMAL)
    friend.config(state=DISABLED)
    frLabel.config(text=f"Friend: {otherChar}")
############################################################################
############################################################################
def saveScore(c):
    global noOfVictory, noOfLooses
    if c == myChar:
        sf = open(f"{scorePath}\\score","w")
        sf.write(f"{int(noOfVictory)+1}|{noOfLooses}")
        sf.close()
        winsGame.config(text=f"Victory: {int(noOfVictory)+1}")
        noOfVictory = int(noOfVictory) + 1
    if c == otherChar:
        sf = open(f"{scorePath}\\score","w")
        sf.write(f"{noOfVictory}|{int(noOfLooses)+1}")
        sf.close()
        loseGame.config(text=f"Looses: {int(noOfLooses)+1}")
        noOfLooses = int(noOfLooses) + 1
############################################################################
############################################################################
def gridOne():
    global nowTurn, gridCount
    if noWinner:
        gridone.config(text=nowTurn)
        if nowTurn == otherChar:
            turnLabel.config(text=f"{myChar}'s Turn")
            nowTurn = myChar
            otherCharGrids.append(1)
        else:
            turnLabel.config(text=f"{otherChar}'s Turn")
            nowTurn = otherChar
            myCharGrids.append(1)
        gridone.config(state=DISABLED)
        gridCount = gridCount + 1
        checkResults()
        allGrids.remove(1)
        if sComputer.get() == 1:
            disableAll()
        if sComputer.get() == 1 and nowTurn == otherChar and noWinner:
            Thread(target=computersTurn).start()

def gridTwo():
    global nowTurn, gridCount
    if noWinner:
        gridtwo.config(text=nowTurn)
        if nowTurn == otherChar:
            turnLabel.config(text=f"{myChar}'s Turn")
            nowTurn = myChar
            otherCharGrids.append(2)
        else:
            turnLabel.config(text=f"{otherChar}'s Turn")
            nowTurn = otherChar
            myCharGrids.append(2)
        gridtwo.config(state=DISABLED)
        gridCount = gridCount + 1
        checkResults()
        allGrids.remove(2)
        if sComputer.get() == 1:
            disableAll()
        if sComputer.get() == 1 and nowTurn == otherChar and noWinner:
            Thread(target=computersTurn).start()

def gridThree():
    global nowTurn, gridCount
    if noWinner:
        gridthree.config(text=nowTurn)
        if nowTurn == otherChar:
            turnLabel.config(text=f"{myChar}'s Turn")
            nowTurn = myChar
            otherCharGrids.append(3)
        else:
            turnLabel.config(text=f"{otherChar}'s Turn")
            nowTurn = otherChar
            myCharGrids.append(3)
        gridthree.config(state=DISABLED)
        gridCount = gridCount + 1
        checkResults()
        allGrids.remove(3)
        if sComputer.get() == 1:
            disableAll()
        if sComputer.get() == 1 and nowTurn == otherChar and noWinner:
            Thread(target=computersTurn).start()

def gridFour():
    global nowTurn, gridCount
    if noWinner:
        gridfour.config(text=nowTurn)
        if nowTurn == otherChar:
            turnLabel.config(text=f"{myChar}'s Turn")
            nowTurn = myChar
            otherCharGrids.append(4)
        else:
            turnLabel.config(text=f"{otherChar}'s Turn")
            nowTurn = otherChar
            myCharGrids.append(4)
        gridfour.config(state=DISABLED)
        gridCount = gridCount + 1
        checkResults()
        allGrids.remove(4)
        if sComputer.get() == 1:
            disableAll()
        if sComputer.get() == 1 and nowTurn == otherChar and noWinner:
            Thread(target=computersTurn).start()

def gridFive():
    global nowTurn, gridCount
    if noWinner:
        gridfive.config(text=nowTurn)
        if nowTurn == otherChar:
            turnLabel.config(text=f"{myChar}'s Turn")
            nowTurn = myChar
            otherCharGrids.append(5)
        else:
            turnLabel.config(text=f"{otherChar}'s Turn")
            nowTurn = otherChar
            myCharGrids.append(5)
        gridfive.config(state=DISABLED)
        gridCount = gridCount + 1
        checkResults()
        allGrids.remove(5)
        if sComputer.get() == 1:
            disableAll()
        if sComputer.get() == 1 and nowTurn == otherChar and noWinner:
            Thread(target=computersTurn).start()

def gridSix():
    global nowTurn, gridCount
    if noWinner:
        gridsix.config(text=nowTurn)
        if nowTurn == otherChar:
            turnLabel.config(text=f"{myChar}'s Turn")
            nowTurn = myChar
            otherCharGrids.append(6)
        else:
            turnLabel.config(text=f"{otherChar}'s Turn")
            nowTurn = otherChar
            myCharGrids.append(6)
        gridsix.config(state=DISABLED)
        gridCount = gridCount + 1
        checkResults()
        allGrids.remove(6)
        if sComputer.get() == 1:
            disableAll()
        if sComputer.get() == 1 and nowTurn == otherChar and noWinner:
            Thread(target=computersTurn).start()

def gridSeven():
    global nowTurn, gridCount
    if noWinner:
        gridseven.config(text=nowTurn)
        if nowTurn == otherChar:
            turnLabel.config(text=f"{myChar}'s Turn")
            nowTurn = myChar
            otherCharGrids.append(7)
        else:
            turnLabel.config(text=f"{otherChar}'s Turn")
            nowTurn = otherChar
            myCharGrids.append(7)
        gridseven.config(state=DISABLED)
        gridCount = gridCount + 1
        checkResults()
        allGrids.remove(7)
        if sComputer.get() == 1:
            disableAll()
        if sComputer.get() == 1 and nowTurn == otherChar and noWinner:
            Thread(target=computersTurn).start()

def gridEight():
    global nowTurn, gridCount
    if noWinner:
        grideight.config(text=nowTurn)
        if nowTurn == otherChar:
            turnLabel.config(text=f"{myChar}'s Turn")
            nowTurn = myChar
            otherCharGrids.append(8)
        else:
            turnLabel.config(text=f"{otherChar}'s Turn")
            nowTurn = otherChar
            myCharGrids.append(8)
        grideight.config(state=DISABLED)
        gridCount = gridCount + 1
        checkResults()
        allGrids.remove(8)
        if sComputer.get() == 1:
            disableAll()
        if sComputer.get() == 1 and nowTurn == otherChar and noWinner:
            Thread(target=computersTurn).start()

def gridNine():
    global nowTurn, gridCount
    if noWinner:
        gridnine.config(text=nowTurn)
        if nowTurn == otherChar:
            turnLabel.config(text=f"{myChar}'s Turn")
            nowTurn = myChar
            otherCharGrids.append(9)
        else:
            turnLabel.config(text=f"{otherChar}'s Turn")
            nowTurn = otherChar
            myCharGrids.append(9)
        gridnine.config(state=DISABLED)
        gridCount = gridCount + 1
        checkResults()
        allGrids.remove(9)
        if sComputer.get() == 1:
            disableAll()
        if sComputer.get() == 1 and nowTurn == otherChar and noWinner:
            Thread(target=computersTurn).start()
############################################################################
############################################################################
def resetGame():
    global nowTurn, noWinner, gridCount, allGrids, myCharGrids, otherCharGrids, playing
    playing = False
    gridCount = 0
    noWinner = True
    allGrids = [1,2,3,4,5,6,7,8,9]
    myCharGrids = []
    otherCharGrids = []
    startBtn.config(text="Start Game", command=startGame)
    if characterO.get() == 1: xCheckBtn.config(state=NORMAL)
    else:oCheckBtn.config(state=NORMAL)
    if sComputer.get() == 1: friend.config(state=NORMAL)
    else:computer.config(state=NORMAL)
    alertLabel.config(text="Press Enter to start game!")
    gridone.config(text="", background="white")
    gridtwo.config(text="", background="white")
    gridthree.config(text="", background="white")
    gridfour.config(text="", background="white")
    gridfive.config(text="", background="white")
    gridsix.config(text="", background="white")
    gridseven.config(text="", background="white")
    grideight.config(text="", background="white")
    gridnine.config(text="", background="white")
    turnLabel.config(text="", foreground="blue")
    nowTurn = otherChar
    disableAll()
############################################################################
############################################################################
def enableSpecificGrid():
    if 1 in allGrids:gridone.config(state=NORMAL)
    if 2 in allGrids:gridtwo.config(state=NORMAL)
    if 3 in allGrids:gridthree.config(state=NORMAL)
    if 4 in allGrids:gridfour.config(state=NORMAL)
    if 5 in allGrids:gridfive.config(state=NORMAL)
    if 6 in allGrids:gridsix.config(state=NORMAL)
    if 7 in allGrids:gridseven.config(state=NORMAL)
    if 8 in allGrids:grideight.config(state=NORMAL)
    if 9 in allGrids:gridnine.config(state=NORMAL)
############################################################################
############################################################################
def getGrid():
    if len(allGrids) == 9:return random.choice(allGrids)
    else:
        ##################################################################
        ##############ATTACKING###########################################
        if 1 in otherCharGrids and 2 in otherCharGrids and 3 in allGrids:return 3
        if 1 in otherCharGrids and 3 in otherCharGrids and 2 in allGrids:return 2
        if 3 in otherCharGrids and 2 in otherCharGrids and 1 in allGrids:return 1
        #4,5,6
        if 4 in otherCharGrids and 5 in otherCharGrids and 6 in allGrids:return 6
        if 4 in otherCharGrids and 6 in otherCharGrids and 5 in allGrids:return 5
        if 6 in otherCharGrids and 5 in otherCharGrids and 4 in allGrids:return 4
        #7,8,9
        if 7 in otherCharGrids and 8 in otherCharGrids and 9 in allGrids:return 9
        if 7 in otherCharGrids and 9 in otherCharGrids and 8 in allGrids:return 8
        if 8 in otherCharGrids and 9 in otherCharGrids and 7 in allGrids:return 7
        #1,4,7
        if 1 in otherCharGrids and 4 in otherCharGrids and 7 in allGrids:return 7
        if 1 in otherCharGrids and 7 in otherCharGrids and 4 in allGrids:return 4
        if 7 in otherCharGrids and 4 in otherCharGrids and 1 in allGrids:return 1
        #2,5,8
        if 2 in otherCharGrids and 5 in otherCharGrids and 8 in allGrids:return 8
        if 2 in otherCharGrids and 8 in otherCharGrids and 5 in allGrids:return 5
        if 5 in otherCharGrids and 8 in otherCharGrids and 2 in allGrids:return 2
        #3,6,9
        if 3 in otherCharGrids and 6 in otherCharGrids and 9 in allGrids:return 9
        if 3 in otherCharGrids and 9 in otherCharGrids and 6 in allGrids:return 6
        if 6 in otherCharGrids and 9 in otherCharGrids and 3 in allGrids:return 3
        #1,5,9
        if 1 in otherCharGrids and 5 in otherCharGrids and 9 in allGrids:return 9
        if 1 in otherCharGrids and 9 in otherCharGrids and 5 in allGrids:return 5
        if 9 in otherCharGrids and 5 in otherCharGrids and 1 in allGrids:return 1
        #3,5,7
        if 3 in otherCharGrids and 5 in otherCharGrids and 7 in allGrids:return 7
        if 3 in otherCharGrids and 7 in otherCharGrids and 5 in allGrids:return 5
        if 5 in otherCharGrids and 7 in otherCharGrids and 3 in allGrids:return 3
        ##################################################################
        ##############DEFENDING###########################################
        #1,2,3
        if 1 in myCharGrids and 2 in myCharGrids and 3 in allGrids:return 3
        if 1 in myCharGrids and 3 in myCharGrids and 2 in allGrids:return 2
        if 3 in myCharGrids and 2 in myCharGrids and 1 in allGrids:return 1
        #4,5,6
        if 4 in myCharGrids and 5 in myCharGrids and 6 in allGrids:return 6
        if 4 in myCharGrids and 6 in myCharGrids and 5 in allGrids:return 5
        if 6 in myCharGrids and 5 in myCharGrids and 4 in allGrids:return 4
        #7,8,9
        if 7 in myCharGrids and 8 in myCharGrids and 9 in allGrids:return 9
        if 7 in myCharGrids and 9 in myCharGrids and 8 in allGrids:return 8
        if 8 in myCharGrids and 9 in myCharGrids and 7 in allGrids:return 7
        #1,4,7
        if 1 in myCharGrids and 4 in myCharGrids and 7 in allGrids:return 7
        if 1 in myCharGrids and 7 in myCharGrids and 4 in allGrids:return 4
        if 7 in myCharGrids and 4 in myCharGrids and 1 in allGrids:return 1
        #2,5,8
        if 2 in myCharGrids and 5 in myCharGrids and 8 in allGrids:return 8
        if 2 in myCharGrids and 8 in myCharGrids and 5 in allGrids:return 5
        if 5 in myCharGrids and 8 in myCharGrids and 2 in allGrids:return 2
        #3,6,9
        if 3 in myCharGrids and 6 in myCharGrids and 9 in allGrids:return 9
        if 3 in myCharGrids and 9 in myCharGrids and 6 in allGrids:return 6
        if 6 in myCharGrids and 9 in myCharGrids and 3 in allGrids:return 3
        #1,5,9
        if 1 in myCharGrids and 5 in myCharGrids and 9 in allGrids:return 9
        if 1 in myCharGrids and 9 in myCharGrids and 5 in allGrids:return 5
        if 9 in myCharGrids and 5 in myCharGrids and 1 in allGrids:return 1
        #3,5,7
        if 3 in myCharGrids and 5 in myCharGrids and 7 in allGrids:return 7
        if 3 in myCharGrids and 7 in myCharGrids and 5 in allGrids:return 5
        if 5 in myCharGrids and 7 in myCharGrids and 3 in allGrids:return 3
        return random.choice(allGrids)
############################################################################
############################################################################
def computersTurn():
    showAlertMessage("Computer is thinking...")
    cchoice = getGrid()
    sleep(1)
    if cchoice == 1:
        gridOne()
        enableSpecificGrid()
    if cchoice == 2:
        gridTwo()
        enableSpecificGrid()
    if cchoice == 3:
        gridThree()
        enableSpecificGrid()
    if cchoice == 4:
        gridFour()
        enableSpecificGrid()
    if cchoice == 5:
        gridFive()
        enableSpecificGrid()
    if cchoice == 6:
        gridSix()
        enableSpecificGrid()
    if cchoice == 7:
        gridSeven()
        enableSpecificGrid()
    if cchoice == 8:
        gridEight()
        enableSpecificGrid()
    if cchoice == 9:
        gridNine()
        enableSpecificGrid()
############################################################################
############################################################################
def whoseTurnFirst():
    players = ["X","X","X","O","O","O","X","O","X","O","X","O","X","O","X","O"]
    return random.choice(players)
############################################################################
############################################################################
def startGame():
    global playing, nowTurn
    playing = True
    startBtn.config(text="Reset Game", command=resetGame)
    if oCheckBtn["state"] == DISABLED:xCheckBtn.config(state=DISABLED)
    else:oCheckBtn.config(state=DISABLED)
    if computer["state"] == DISABLED:friend.config(state=DISABLED)
    else:computer.config(state=DISABLED)
    alertLabel.config(text="")
    if sComputer.get() == 1:
        nowTurn = random.choice(["X","O"])
        turnLabel.config(text=f"{nowTurn}'s Turn")
        if nowTurn == otherChar:
            Thread(target=computersTurn).start()
        enableAll()
    else:
        enableAll()
        turnLabel.config(text=f"{otherChar}'s Turn")
############################################################################
############################################################################
def getColor():
    color1 = "red"
    color2 = "green"
    if myChar == "X":
        tempColor = color1
        color1 = color2
        color2 = tempColor
        return [color1,color2]
    return [color1,color2]
############################################################################
############################################################################
def checkResults():
    global noWinner
    if gridseven["text"]=="X" and gridfour["text"]=="X" and gridone["text"]=="X":
        gridseven.config(background=getColor()[0]);gridfour.config(background=getColor()[0]);gridone.config(background=getColor()[0])
        disableAll()
        turnLabel.config(text="X WON", foreground=getColor()[0])
        noWinner = False
        saveScore("X")
    if grideight["text"]=="X" and gridfive["text"]=="X" and gridtwo["text"]=="X":
        grideight.config(background=getColor()[0]);gridfive.config(background=getColor()[0]);gridtwo.config(background=getColor()[0])
        disableAll()
        turnLabel.config(text="X WON", foreground=getColor()[0])
        noWinner = False
        saveScore("X")
    if gridnine["text"]=="X" and gridsix["text"]=="X" and gridthree["text"]=="X":
        gridnine.config(background=getColor()[0]);gridsix.config(background=getColor()[0]);gridthree.config(background=getColor()[0])
        disableAll()
        turnLabel.config(text="X WON", foreground=getColor()[0])
        noWinner = False
        saveScore("X")
    if gridone["text"]=="X" and gridtwo["text"]=="X" and gridthree["text"]=="X":
        gridone.config(background=getColor()[0]);gridtwo.config(background=getColor()[0]);gridthree.config(background=getColor()[0])
        disableAll()
        turnLabel.config(text="X WON", foreground=getColor()[0])
        noWinner = False
        saveScore("X")
    if gridfour["text"]=="X" and gridfive["text"]=="X" and gridsix["text"]=="X":
        gridfour.config(background=getColor()[0]);gridfive.config(background=getColor()[0]);gridsix.config(background=getColor()[0])
        disableAll()
        turnLabel.config(text="X WON", foreground=getColor()[0])
        noWinner = False
        saveScore("X")
    if gridseven["text"]=="X" and grideight["text"]=="X" and gridnine["text"]=="X":
        gridseven.config(background=getColor()[0]);grideight.config(background=getColor()[0]);gridnine.config(background=getColor()[0])
        disableAll()
        turnLabel.config(text="X WON", foreground=getColor()[0])
        noWinner = False
        saveScore("X")
    if gridone["text"]=="X" and gridfive["text"]=="X" and gridnine["text"]=="X":
        gridone.config(background=getColor()[0]);gridfive.config(background=getColor()[0]);gridnine.config(background=getColor()[0])
        disableAll()
        turnLabel.config(text="X WON", foreground=getColor()[0])
        noWinner = False
        saveScore("X")
    if gridseven["text"]=="X" and gridfive["text"]=="X" and gridthree["text"]=="X":
        gridseven.config(background=getColor()[0]);gridfive.config(background=getColor()[0]);gridthree.config(background=getColor()[0])
        disableAll()
        turnLabel.config(text="X WON", foreground=getColor()[0])
        noWinner = False
        saveScore("X")
    ############################For O###########################################
    if gridseven["text"]=="O" and gridfour["text"]=="O" and gridone["text"]=="O":
        gridseven.config(background=getColor()[1]);gridfour.config(background=getColor()[1]);gridone.config(background=getColor()[1])
        disableAll()
        turnLabel.config(text="O WON", foreground=getColor()[1])
        noWinner = False
        saveScore("O")
    if grideight["text"]=="O" and gridfive["text"]=="O" and gridtwo["text"]=="O":
        grideight.config(background=getColor()[1]);gridfive.config(background=getColor()[1]);gridtwo.config(background=getColor()[1])
        disableAll()
        turnLabel.config(text="O WON", foreground=getColor()[1])
        noWinner = False
        saveScore("O")
    if gridnine["text"]=="O" and gridsix["text"]=="O" and gridthree["text"]=="O":
        gridnine.config(background=getColor()[1]);gridsix.config(background=getColor()[1]);gridthree.config(background=getColor()[1])
        disableAll()
        turnLabel.config(text="O WON", foreground=getColor()[1])
        noWinner = False
        saveScore("O")
    if gridone["text"]=="O" and gridtwo["text"]=="O" and gridthree["text"]=="O":
        gridone.config(background=getColor()[1]);gridtwo.config(background=getColor()[1]);gridthree.config(background=getColor()[1])
        disableAll()
        turnLabel.config(text="O WON", foreground=getColor()[1])
        noWinner = False
        saveScore("O")
    if gridfour["text"]=="O" and gridfive["text"]=="O" and gridsix["text"]=="O":
        gridfour.config(background=getColor()[1]);gridfive.config(background=getColor()[1]);gridsix.config(background=getColor()[1])
        disableAll()
        turnLabel.config(text="O WON", foreground=getColor()[1])
        noWinner = False
        saveScore("O")
    if gridseven["text"]=="O" and grideight["text"]=="O" and gridnine["text"]=="O":
        gridseven.config(background=getColor()[1]);grideight.config(background=getColor()[1]);gridnine.config(background=getColor()[1])
        disableAll()
        turnLabel.config(text="O WON", foreground=getColor()[1])
        noWinner = False
        saveScore("O")
    if gridone["text"]=="O" and gridfive["text"]=="O" and gridnine["text"]=="O":
        gridone.config(background=getColor()[1]);gridfive.config(background=getColor()[1]);gridnine.config(background=getColor()[1])
        disableAll()
        turnLabel.config(text="O WON", foreground=getColor()[1])
        noWinner = False
        saveScore("O")
    if gridseven["text"]=="O" and gridfive["text"]=="O" and gridthree["text"]=="O":
        gridseven.config(background=getColor()[1]);gridfive.config(background=getColor()[1]);gridthree.config(background=getColor()[1])
        disableAll()
        turnLabel.config(text="O WON", foreground=getColor()[1])
        noWinner = False
        saveScore("O")
    if gridCount == 9 and noWinner:
        noWinner = False
        turnLabel.config(text="Tie", foreground="yellow")
############################################################################
############################################################################
controlsframe = LabelFrame(root, background=bgColor, bd=0)
controlsframe.place(x=0,y=0,height=window_height,width=window_width/2-100)
############################################################################
############################################################################
playerName = Label(controlsframe, font=("times",18), text=f"Hi {username}!", bd=0, background=bgColor, foreground="white")
playerName.place(relx=0.50, rely=0.01, anchor=N)
scoreLabel = Label(controlsframe, font=("times",15), text="Score Board", bd=0, background=bgColor, foreground="white")
scoreLabel.place(relx=0.50, rely=0.10, anchor=N)
winsGame = Label(controlsframe, font=("times",15), text=f"Victory: {noOfVictory}", bd=0, background=bgColor, foreground="white")
winsGame.place(relx=0.15, rely=0.15, anchor=NW)
loseGame = Label(controlsframe, font=("times",15), text=f"Looses: {noOfLooses}", bd=0, background=bgColor, foreground="white")
loseGame.place(relx=0.85, rely=0.15, anchor=NE)
############################################################################
############################################################################
syChar = Label(controlsframe, font=("times",15), text="Select your character.", bd=0, background=bgColor, foreground="white")
syChar.place(relx=0.50, rely=0.22, anchor=N)
xCheckBtn = Checkbutton(controlsframe, bd=0, text="X", font=("arial",12),variable=characterX,command=selectXchar, width=5, state=DISABLED)
xCheckBtn.place(relx=0.45, rely=0.27, anchor=NE)
oCheckBtn = Checkbutton(controlsframe, bd=0, text="O", font=("arial",12),variable=characterO,command=selectOchar, width=5)
oCheckBtn.place(relx=0.55, rely=0.27, anchor=NW)
############################################################################
############################################################################
playWith = Label(controlsframe, font=("times",15), text="Select your opponent.", bd=0, background=bgColor, foreground="white")
playWith.place(relx=0.50, rely=0.35, anchor=N)
computer = Checkbutton(controlsframe, state=DISABLED,variable=sComputer,bd=0, text="Computer", font=("arial",12),command=selectComputer, width=10)
computer.place(relx=0.10, rely=0.40, anchor=NW)
friend = Checkbutton(controlsframe, variable=sFriend, bd=0, text="Friend", font=("arial",12),command=selectFriend, width=10)
friend.place(relx=0.90, rely=0.40, anchor=NE)
############################################################################
############################################################################
frendLabel = Label(controlsframe, text="Playing with: Computer", bd=0, background=bgColor, foreground="white",font=("times",15))
frendLabel.place(relx=0.50, rely=0.54, anchor=S)
############################################################################
############################################################################
youLabel = Label(controlsframe, text="You: X", bd=0, background=bgColor, foreground="white",font=("times",15))
youLabel.place(relx=0.20, rely=0.60, anchor=SW)
frLabel = Label(controlsframe, text="Computer: O", bd=0, background=bgColor, foreground="white",font=("times",15))
frLabel.place(relx=0.80, rely=0.60, anchor=SE)
############################################################################
############################################################################
startBtn = Button(controlsframe, text="Start Game", width=15, font=("times", 12), command=startGame)
startBtn.place(relx=0.50, rely=0.70, anchor=S)
############################################################################
############################################################################
turnLabel = Label(controlsframe, text="", bd=0, background=bgColor, foreground="blue",font=("times",45))
turnLabel.place(relx=0.50, rely=0.90, anchor=S)
############################################################################
############################################################################
alertLabel = Label(controlsframe, text="Press Enter to start game!", bd=0, background=bgColor, foreground="yellow",font=(12))
alertLabel.place(relx=0.50, rely=0.98, anchor=S)
############################################################################
############################################################################
gameframe = LabelFrame(root, bd=0, background=bgColor)
gameframe.place(x=window_width/2-100,y=0,height=window_height,width=window_width+100)
gridone = Button(gameframe, font=("arial",50), bd=0, width=3,command=gridOne)
gridone.grid(row=2,column=0,padx=20,pady=20)
gridtwo = Button(gameframe, font=("arial",50), bd=0, width=3,command=gridTwo)
gridtwo.grid(row=2,column=1,padx=20,pady=20)
gridthree = Button(gameframe, font=("arial",50), bd=0, width=3,command=gridThree)
gridthree.grid(row=2,column=2,padx=20,pady=20)
############################################################################
############################################################################
gridfour = Button(gameframe, font=("arial",50), bd=0, width=3,command=gridFour)
gridfour.grid(row=1,column=0,padx=20,pady=20)
gridfive = Button(gameframe, font=("arial",50), bd=0, width=3,command=gridFive)
gridfive.grid(row=1,column=1,padx=20,pady=20)
gridsix = Button(gameframe, font=("arial",50), bd=0, width=3,command=gridSix)
gridsix.grid(row=1,column=2,padx=20,pady=20)
############################################################################
############################################################################
gridseven = Button(gameframe, font=("arial",50), bd=0, width=3,command=gridSeven)
gridseven.grid(row=0,column=0,padx=20,pady=20)
grideight = Button(gameframe, font=("arial",50), bd=0, width=3,command=gridEight)
grideight.grid(row=0,column=1,padx=20,pady=20)
gridnine = Button(gameframe, font=("arial",50), bd=0, width=3,command=gridNine)
gridnine.grid(row=0,column=2,padx=20,pady=20)
############################################################################
############################################################################
def detectKeypress(e):
    key = e.keysym
    if nowTurn == myChar:
        if key == "1":
            if 1 in allGrids:gridOne()
        if key == "2":
            if 2 in allGrids:gridTwo()
        if key == "3":
            if 3 in allGrids:gridThree()
        if key == "4":
            if 4 in allGrids:gridFour()
        if key == "5":
            if 5 in allGrids:gridFive()
        if key == "6":
            if 6 in allGrids:gridSix()
        if key == "7":
            if 7 in allGrids:gridSeven()
        if key == "8":
            if 8 in allGrids:gridEight()
        if key == "9":
            if 9 in allGrids:gridNine()
    if key == "Return":
        if not playing:startGame()
        else:resetGame()
############################################################################
############################################################################
root.bind('<KeyRelease>', detectKeypress)
############################################################################
############################################################################
def nothing():root.destroy()
############################################################################
############################################################################
root.protocol('WM_DELETE_WINDOW', nothing)
# setNickname()
disableAll()
root.mainloop()
#This much:)
#Started this project on June 4, 2022
#Completed on June 6, 2022
#Updated on June 10, 2022
#Made with ❤ by Bidhan Acharya