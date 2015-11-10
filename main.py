import tkinter
from PIL import ImageTk, Image
from pydub import AudioSegment
from pydub.playback import play

root = tkinter.Tk()
root.title("Fedora Tipping Simulator")

winSize = tkinter.Canvas(height = 60, width = 300)

imageFed0 = Image.open("fedora.jpeg")

tkFed0 = ImageTk.PhotoImage(imageFed0)
fedoraImg = tkinter.Label(root, image = tkFed0)

score = 0
scoreLabel = tkinter.Label(root, text = "Score: " + str(score))

def rotateToFifteen():
    global imageFed0
    imageFed1 = imageFed0.rotate(15)
    tkFed1 = ImageTk.PhotoImage(imageFed1)
    fedoraImg.imageTest = imageFed1
    fedoraImg.config(image = tkFed1)
    fedoraImg.image = tkFed1

def rotateToZero():
    global imageFed0
    global fedoraImg
    imageFed2 = imageFed0.rotate(0)
    tkFed2 = ImageTk.PhotoImage(imageFed2)
    fedoraImg.imageTest = imageFed2
    fedoraImg.config(image = tkFed2)
    fedoraImg.image = tkFed2

def press():
    global score
    global scoreLabel
    newScore = score + 1
    score = newScore
    scoreLabel.config(text = "Score: " + str(newScore))
    rotateToFifteen()
    root.update()
    root.after(1000, rotateToZero)
    lady = AudioSegment.from_mp3("m'lady.mp3")
    play(lady)

tipFed0 = tkinter.Button(root, text = "Tip Fedora", command = press)

tipFed0.pack()
fedoraImg.pack()
scoreLabel.pack()
winSize.pack()

root.mainloop()
