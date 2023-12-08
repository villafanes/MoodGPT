        # put song name and title into genius api
        lyrics = genius_api.get_lyrics(artist_name, song_title)
        image_url = image_api.execute(lyrics)

        print(lyrics)
        duplicate_words = image_api.generate_title(lyrics)
        print('Duplicate words: ', duplicate_words)
        words, frequencies = image_api.top_5_words_and_counts(duplicate_words)
        print('Words:', words)
        print('Frequencies:', frequencies)

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

        def display_data(moodboard_path, top_words, top_word_counts):
            moodboard = Image.open(moodboard_path)
            moodboard = moodboard.resize((500, 500))
            moodboard_img = ImageTk.PhotoImage(moodboard)

            img_label = Label(new_window, image=moodboard_img)
            img_label.image = moodboard_img
            img_label.grid(row=0, column=0)

            # Create a Matplotlib figure and a subplot for the pie chart
            # Adjust the figure size to match the image size
            plot = Figure(figsize=(5, 5), facecolor='honeydew')
            chart = plot.add_subplot(111)

            # Plot the pie chart on the subplot without labels
            colors = ['darkgreen', 'forestgreen', 'seagreen', 'mediumseagreen', 'lightgreen']
            chart.pie(frequencies, colors=colors, autopct='%1.1f%%', shadow=True, startangle=140)
            chart.set_title(f'{song_title} by {artist_name}', fontname='Georgia', fontsize=18)
            chart.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

            # Create a legend
            chart.legend(words, loc='upper left', bbox_to_anchor=(0.85, 1))

            # Embed the figure in the Tkinter window
            canvas = FigureCanvasTkAgg(plot, master=new_window)
            canvas.draw()
            canvas.get_tk_widget().grid(row=0, column=1)

        root.withdraw()
        display_data('moodboard.png', words, frequencies)

        def reopen_root():
            new_window.withdraw()
            root.deiconify()
            new_window.withdraw()

        restart = Button(new_window, text="Start Again", font=("Georgia", 12, "bold"), command=reopen_root)
        restart.place(x=850, y=450)  # temporary location
