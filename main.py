import tkinter
from PIL import ImageTk, Image
from pydub import AudioSegment
from pydub.playback import play

#Creates main window
root = tkinter.Tk()
root.title("Fedora Tipping Simulator")

#Specifies the height and width of the window
winSize = tkinter.Canvas(height = 60, width = 300)

#Opens the fedora image
imageFed0 = Image.open("fedora.jpeg")

#Creates a label with tkinter and sets it's image to the fedora image
tkFed0 = ImageTk.PhotoImage(imageFed0)
fedoraImg = tkinter.Label(root, image = tkFed0)

#Sets the original score to zero
score = 0
scoreLabel = tkinter.Label(root, text = "Score: " + str(score))

#rotates the image fifteen degrees
def rotateToFifteen():
    global imageFed0
    imageFed1 = imageFed0.rotate(15)
    tkFed1 = ImageTk.PhotoImage(imageFed1)
    fedoraImg.imageTest = imageFed1
    fedoraImg.config(image = tkFed1)
    fedoraImg.image = tkFed1

#Rotates the image back to it's original position
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
	#increments and prints the score by one
    newScore = score + 1
    score = newScore
    scoreLabel.config(text = "Score: " + str(newScore))
	
	#Calls the returnToFifteen function to rotate the image fifteen degrees
    rotateToFifteen()
    root.update()
	
	#Once the returnToFifteen function is finished, the returnToZero function is called
    root.after(1000, rotateToZero)
	
	#Plays the m'lady audio segment
    lady = AudioSegment.from_mp3("m'lady.mp3")
    play(lady)

#Creates the button and sets it's command to the press function
tipFed0 = tkinter.Button(root, text = "Tip Fedora", command = press)

#packs all the tkinter objects
tipFed0.pack()
fedoraImg.pack()
scoreLabel.pack()
winSize.pack()

#runs the window
root.mainloop()
