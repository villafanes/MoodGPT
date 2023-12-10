import requests
from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk
import genius_api
import image_api
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

# Home Page Main Screen
root = Tk()
root.title("Welcome to MoodGPT")

# Home Page Background Image Grid
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

# Exit button, top right of the screen to avoid quit program smoothly
quit = Button(root, text="Exit", font=("Georgia", 16, "bold"), command=root.quit, fg="#FF0000")  # doesn't show on mac
quit.grid(row=0, column=500, sticky="ne")


def open_window():
    song_title = song_entry.get()
    artist_name = artist_entry.get()

    # Prompts error window in case user did not delete default text in entry widgets 
    if "Song Title: " in song_title or "Artist Name: " in artist_name:
        messagebox.showerror("Error", "Must delete text inside text box[es] before entering song title and artist name.")
    else:
        # Enters artist name and title entered by the user
        # Stores the closest match of artist name and title found by Genius 
        lyrics, artist_used, song_used = genius_api.get_lyrics(artist_name, song_title)
        
        # If the song isn't found in the Genius API
        if lyrics is None:
            messagebox.showerror("Error", "Song cannot be found. Please check your spelling and try again.")

        # Passes lyrics into AI image generator
        image_url = image_api.execute(lyrics)
        
        # If the lyrics contain any words or phrases not allowed by the AI image generator
        if image_url is None:
            messagebox.showerror("Error", "The system detected potentially unsafe content. Please try running the program again or adjust the prompt.")
            return

        # Collect repeated words and store arrays of the top 5 words and their frequencies
        duplicate_words = image_api.generate_title(lyrics)
        words, frequencies = image_api.top_5_words_and_counts(duplicate_words)
        
        # Creates a file to hold the mood board image
        f = open('moodboard.png', 'wb')

        # stores the image data inside the data variable to the file
        file = requests.get(image_url).content
        f.write(file)
        f.close()

        # Creates new window for mood board and pie chart presentation
        new_window = Toplevel(root)
        new_window.title("Mood Board")

        def display_data(moodboard_path, top_words, top_word_counts):
            # Displays generated mood board image on the new window
            moodboard = Image.open(moodboard_path)
            moodboard = moodboard.resize((500, 500))
            moodboard_img = ImageTk.PhotoImage(moodboard)
            img_label = Label(new_window, image=moodboard_img)
            img_label.image = moodboard_img
            img_label.grid(row=0, column=0)

            # Creates a Matplotlib figure and a subplot for the pie chart
            plot = Figure(figsize=(6, 5), facecolor='honeydew')
            chart = plot.add_subplot(111)

            # Plots the pie chart on the subplot without labels
            colors = ['darkgreen', 'forestgreen', 'seagreen', 'mediumseagreen', 'lightgreen']
            chart.pie(frequencies, colors=colors, autopct='%1.1f%%', shadow=True, startangle=140)
            chart.set_title(f'{song_used} by {artist_used}', fontname='Georgia', fontsize=18)
            chart.axis('equal')  

            # Creates a legend
            chart.legend(words, loc='upper left', bbox_to_anchor=(0.85, 1))

            # Embeds the pie chart in the Tkinter window
            canvas = FigureCanvasTkAgg(plot, master=new_window)
            canvas.draw()
            canvas.get_tk_widget().grid(row=0, column=1)

        # Hides the home screen window
        root.withdraw()
        display_data('moodboard.png', words, frequencies)

        def reopen_root():
            # Hides mood board window and reopens home window so the user can enter a new song
            new_window.withdraw()
            root.deiconify()
            new_window.withdraw()

        # Triggers the home window to open when clicked
        restart = Button(new_window, text="Start Again", font=("Georgia", 12, "bold"), command=reopen_root)
        restart.place(x=750, y=450)  


# Triggers the mood board window to open when clicked
enter = Button(root, text="Enter", font=("Georgia", 12, "bold"), command=open_window)
enter.place(x=345, y=415)

root.mainloop()
