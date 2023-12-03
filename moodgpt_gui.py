from tkinter import *
from PIL import ImageTk, Image


root = Tk()
# title at the top of the root widget window
root.title("Welcome to MoodGPT")

# Home page background
pop_image = Image.open("pop_music.png")
resized_pop = pop_image.resize((250, 250))
pop_music = ImageTk.PhotoImage(resized_pop)
pop_label = Label(image=pop_music)
pop_label.grid(row=0, column=0)

rap_image = Image.open("rap_music.png")
resized_rap = rap_image.resize((250, 250))
rap_music = ImageTk.PhotoImage(resized_rap)
rap_label = Label(image=rap_music)
rap_label.grid(row=0, column=250)

rnb_image = Image.open("rnb_music.png")
resized_rnb = rnb_image.resize((250, 250))
rnb_music = ImageTk.PhotoImage(resized_rnb)
rnb_label = Label(image=rnb_music)
rnb_label.grid(row=0, column=500)

rock_image = Image.open("rock_music.png")
resized_rock = rock_image.resize((250, 250))
rock_music = ImageTk.PhotoImage(resized_rock)
rock_label = Label(image=rock_music)
rock_label.grid(row=250, column=0)

moodgpt_image = Image.open("moodgpt_bg.png")
resized_moodgpt = moodgpt_image.resize((250, 250))
moodgpt_bg = ImageTk.PhotoImage(resized_moodgpt)
moodgpt_label = Label(image=moodgpt_bg)
moodgpt_label.grid(row=250, column=250, rowspan=2)

heavymetal_image = Image.open("heavymetal_music.png")
resized_heavymetal = heavymetal_image.resize((250, 250))
heavymetal_music = ImageTk.PhotoImage(resized_heavymetal)
heavymetal_label = Label(image=heavymetal_music)
heavymetal_label.grid(row=250, column=500)

classical_image = Image.open("classical_music.png")
resized_classical = classical_image.resize((250, 250))
classical_music = ImageTk.PhotoImage(resized_classical)
classical_label = Label(image=classical_music)
classical_label.grid(row=500, column=0)

edm_image = Image.open("edm_music.png")
resized_edm = edm_image.resize((250, 250))
edm_music = ImageTk.PhotoImage(resized_edm)
edm_label = Label(image=edm_music)
edm_label.grid(row=500, column=250)

latin_image = Image.open("latin_music.png")
resized_latin = latin_image.resize((250, 250))
latin_music = ImageTk.PhotoImage(resized_latin)
latin_label = Label(image=latin_music)
latin_label.grid(row=500, column=500)

# Accepts user song title
text_widget = Label(root, text="MoodGPT", font=("Georgia", 46, "bold"), bg="#6F8FAF")
text_widget.place(x=260, y=275)
song_entry = Entry(root, width=25, bg="#6F8FAF")
song_entry.place(x=262, y=340)
song_title = song_entry.get()


# Exit button, top right of the screen
quit = Button(root, text="Exit", font=("Arial", 16, "bold"), command=root.quit, fg="#FF0000") # doesn't show on mac
quit.grid(row=0, column=500, sticky="ne")

def newWindow():
    new_window = Toplevel(root)
    new_window.title("Mood Board")

    tester = Image.open("Ligma.png")
    resized_tester = tester.resize((750, 750))
    test_img = ImageTk.PhotoImage(resized_tester)

    test_label = Label(new_window, image=test_img)
    test_label.image = test_img
    test_label.grid(row=0, column=0)

    root.withdraw()


button = Button(root, text="Enter", font=("Georgia", 12, "bold"), padx=5, pady=2.5, command=newWindow, bg="#B5A2C8")
button.place(x=345, y=380)

root.mainloop()