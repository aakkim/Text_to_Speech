from tkinter import *
from gtts import gTTS
from playsound import playsound


core = Tk()
core.geometry('350x350')
core.configure(bg='white')
core.title('Text to Speech Converter')

Label(core, text="Text to Speech Converter", font="georgia 18 bold", fg="black", bg="white").pack()
Label(text="Enjoy!", font="georgia 14 bold", fg="black", bg="white").pack(side="bottom")

Msg = StringVar()
Label(core, text="Enter Text:", font="georgia 16 bold", fg="black", bg="white").place(x=20,y=60)


text_field = Entry(core, textvariable=Msg, width="33")
text_field.place(x=20,y=100)

# converting text to speech functions
def textToSpeech():
    message = text_field.get()
    speech = gTTS(text = message)
    speech.save('TTS.mp3')
    playsound('TTS.mp3')


def exit():
    core.destroy()


def reset():
    Msg.set('')


# define buttons
Button(core, text="PLAY", font="georgia 14", command=textToSpeech, width="5", padx=0, pady=0, fg="black", bg="white").place(x=53,y=140)
Button(core, text="EXIT", font="georgia 14", command=exit, width="5", padx=0, pady=0, fg="black", bg="white").place(x=137,y=140)
Button(core, text="RESET", font="georgia 14", command=reset, width="5", padx=0, pady=0, fg="black", bg="white").place(x=220,y=140)


core.mainloop()


