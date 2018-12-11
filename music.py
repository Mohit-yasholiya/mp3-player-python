from Tkinter import *
from pygame import mixer
import Tkinter, Tkconstants, tkFileDialog
var_play = ""
def select():
    global var_play
    window.filename = tkFileDialog.askopenfilename(initialdir = "/",title = "Select file",filetypes = (("mp3 files","*.mp3"),("all files","*.*")))
    print (type(window.filename.decode()))
    var_play=str(window.filename)
    print(var_play)

    
def play_():
    global var_play
    print(var_play)
    mixer.init()                               
    mixer.music.load('123.mp3') 
    mixer.music.play()

    
def stop_():
    mixer.music.stop()
window = Tk()
 
window.title("Welcome to LikeGeeks app")
btn = Button(window, text="Play",bg='#0ff',fg='red',bd=8,command = play_)
btn.grid(column=1, row=0)
Button(window, text="stop",bg='#0ff',fg='red',bd=8,command = stop_).grid(column=2, row=0)
Button(window, text="open",bg='#0ff',fg='red',bd=8,command = select).grid(column=3, row=0)


window.mainloop()
from Tkinter import *
import Tkinter, Tkconstants, tkFileDialog

root=Tk()
root.filename = tkFileDialog.askopenfilename(initialdir="/",title = "Select file",filetypes = (("mp3 files","*.mp3"),("all files","*.*")))
print(root.filename)
