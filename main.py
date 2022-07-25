# importing required module
import sys
from tkinter import *
from tkinter import messagebox
from gtts import gTTS
from tkinter.ttk import Combobox
import os

# create tkinter window
root = Tk()
root.geometry("1200x700")
root.config(background="#121212")
root.title("Text to Speech")
root.config(cursor="spider")

text = Text(root, background="#7f7f7f", foreground="white", height=35, borderwidth=2, font=("Verdana", 12), insertbackground="#39ace7", cursor="heart")
text.place(x=15, y=30)

Label(root, text="Accent", font="arial 15", background="#121212", foreground="white").place(x=980, y=100)

tx = StringVar()
tx.set("United States")
tldch = Combobox(root,
                 values=["Australia", "United Kingdom", "United States", "Canada", "India", "Ireland", "South Africa"],
                 width=19, textvariable=tx)
tldch.place(x=950, y=140)

sx = StringVar()
sx.set("False")

Label(root, text="Slow", font="arial 15", background="#121212", foreground="white").place(x=990, y=210)
slch = Combobox(root, values=["True", "False"], width=19, textvariable=sx)
slch.place(x=950, y=250)


def play():
    # Language in which you want to convert
    language = "en-us"

    tldget = tldch.get()
    slget = slch.get()

    slow = ""

    tld = ""

    if tldget == "Australia":
        tld = "com.au"
    elif tldget == "United Kingdom":
        tld = "co.uk"
    elif tldget == "United States":
        tld = "com"
    elif tldget == "Canada":
        tld = "ca"
    elif tldget == "India":
        tld = "co.in"

    elif tldget == "Ireland":
        tld = "ie"

    elif tldget == "South Africa":
        tld = "co.za"

    if slget == "False":
        slow = False
    else:
        slow = True

    text.get(1.0, END)

    myobj = gTTS(text=text.get(1.0, END),
                 lang=language,
                 tld=tld,
                 slow=slow)

    filename = "tts.wav"

    # give the name as you want to
    # save the audio

    try:
        myobj.save(filename)
        messagebox.showinfo(title="Success", message="Saved! Click OK or close this window to play the audio.")
        os.system(filename)
    except:
        messagebox.showerror(title="Error!", message="Can't save your file right now. Try again later!")


def exitapp():
    messagebox.showinfo(title="Exit", message="exiting the App! Click OK or close this window to exit.")
    sys.exit()


speakbtn = Button(root, text="Speak", background="#39ace7", width=20, font="arial 15", height=1, command=play).place(
    x=900, y=520)
Button(root, text="Exit", background="#39ace7", width=20, font="arial 15", height=1, command=exitapp).place(
    x=900, y=590)

root.mainloop()
