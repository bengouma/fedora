import tkinter
from PIL import ImageTk, Image
from pydub import AudioSegment
from pydub.playback import play

window = tkinter.Tk()
window.title("Fedora Tipping Simulator")

winSize = tkinter.Canvas(height = 60, width = 300)

imageFed0 = Image.open("fedora.jpeg")

tkFed0 = ImageTk.PhotoImage(imageFed0)
fedoraImg = tkinter.Label(window, image = tkFed0)

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
    rotateToFifteen()
    window.update()
    window.after(2000, rotateToZero)
    lady = AudioSegment.from_mp3("m'lady.mp3")
    play(lady)

tipFed0 = tkinter.Button(window, text = "Tip Fedora", command = press)

tipFed0.pack()
fedoraImg.pack()
winSize.pack()

window.mainloop()
