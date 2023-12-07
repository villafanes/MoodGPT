import requests
from tkinter import *
from tkinter import messagebox
from PIL import ImageTk, Image
from genius_api import get_lyrics
from image_api import execute
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt

# Home Page Main Screen
root = Tk()
root.title("Welcome to MoodGPT")

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

# Accepts user song title and artist
text_widget = Label(root, text="MoodGPT", font=("Georgia", 46, "bold"), bg="#6F8FAF")
text_widget.place(x=260, y=275)

song_entry = Entry(root, width=25, bg="#6F8FAF", font="Georgia")
song_entry.insert(0, "Song Title: ")
song_entry.place(x=275, y=340)

artist_entry = Entry(root, width=25, bg="#6F8FAF", font="Georgia")
artist_entry.insert(0, "Artist Name: ")
artist_entry.place(x=275, y=370)

# Exit button, top right of the screen
quit = Button(root, text="Exit", font=("Arial", 16, "bold"), command=root.quit, fg="#FF0000")  # doesn't show on mac
quit.grid(row=0, column=500, sticky="ne")


def newWindow():
    song_title = song_entry.get()
    artist_name = artist_entry.get()

    # if user didn't delete the text in the entry widgets
    if "Song Title: " in song_title or "Artist Name: " in artist_name:
        messagebox.showerror("Error",
                             "Must delete text inside text box[es] before entering song title and artist name.")
    else:
        # put song name and title into genius api
        lyrics = get_lyrics(artist_name, song_title)
        image_url = execute(lyrics)

        # extracts contents of image url
        file = requests.get(image_url).content

        # create a new file to hold the mood board image
        """Check if the file type is jpg or png"""
        f = open('moodboard.png', 'wb')

        # stores the image data inside the data variable to the file
        f.write(file)
        f.close()

        new_window = Toplevel(root)
        new_window.title("Mood Board")

        def display_data(moodboard_path, words, frequencies):
            moodboard = Image.open(moodboard_path)
            moodboard = moodboard.resize((250, 250))
            moodboard_img = ImageTK.PhotoImage(moodboard)

            img_label = Label(new_window, image=moodboard_img)
            img_label.image = moodboard_img
            img_label.grid(row=0, column=0)

            # Create a Matplotlib figure and a subplot for the pie chart
            # Adjust the figure size to match the image size
            plot = Figure(figsize=(5, 5))  # Adjust the size to match the image
            chart = plot.add_subplot(111)

            # Plot the pie chart on the subplot without labels
            colors = ['darkgreen', 'forestgreen', 'seagreen', 'mediumseagreen', 'lightgreen']
            chart.pie(frequencies, colors=colors, autopct='%1.1f%%', shadow=True, startangle=140)
            chart.set_title(f'{song_title} by {artist_name}', fontname='Times New Roman', fontsize=18)
            chart.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

            # Create a legend
            chart.legend(words, loc='upper left', bbox_to_anchor=(0.85, 1))

            # Embed the figure in the Tkinter window
            canvas = FigureCanvasTkAgg(plot, master=new_window)
            canvas.draw()
            canvas.get_tk_widget().pack(side=RIGHT, fill=BOTH, expand=1)

        root.withdraw()
        display_data('moodboard.png', words, frequencies)

        def reopen_root():
            new_window.withdraw()
            root.deiconify()
            new_window.withdraw()

        restart = Button(new_window, text="Start Again", font=("Georgia", 12, "bold"), command=reopen_root)
        restart.place(x=345, y=415)  # temporary location


button = Button(root, text="Enter", font=("Georgia", 12, "bold"), command=newWindow)
button.place(x=345, y=415)

root.mainloop()
