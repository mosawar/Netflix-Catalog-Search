import csv, tkinter, tkinter.messagebox, tkinter.ttk, json, requests, os, pandas as pd
from twilio.rest import Client

# Lists to hold the selected movie, director, or cast member for sending as SMS
input_title_send = []
input_director_send = []
input_cast_send = []

# Twilio account details for sending SMS
account_sid = '' # Enter Twilio Account SID here
auth_token = '' # Enter Twilio Auth Token here
twilio_number = '' # Twilio phone number to send texts from
my_phone_number = '' # User's verified phone number to receive SMS

# Function to send movie title to phone using Twilio
def title_sender():
    client = Client(account_sid, auth_token)
    message = client.messages.create(
        body = input_title_send,
        from_ = twilio_number,
        to = my_phone_number
    )

# Function to send director name to phone using Twilio
def director_name_sender():
    client = Client(account_sid, auth_token)
    message = client.messages.create(
        body = input_director_send,
        from_ = twilio_number,
        to = my_phone_number
    )

# Function to send cast name to phone using Twilio
def cast_name_sender():
    client = Client(account_sid, auth_token)
    message = client.messages.create(
        body = input_cast_send,
        from_ = twilio_number,
        to = my_phone_number
    )

# Function to close the Tkinter window
def killer():
    """Closes the tkinter window"""
    root.destroy()

# Main Tkinter window setup
root = tkinter.Tk()
root.title("Weekly Movie or TV Show Suggestions")
root.configure(bg="dark grey")

# Dropdown menu for category selection: title, director, or cast
category_box = tkinter.ttk.Combobox(root, values=["Title", "Director", "Cast"])
category_box.grid(row=0, column=1, padx=5, pady=5, sticky='w')

# Labels for the UI
category_label = tkinter.Label(root, text="Search by: title, director, \n and cast")
category_label.configure(bg="yellow")
category_label.grid(row=1, column=1)

info_label = tkinter.Label(root, text="Options: ")
info_label.configure(bg="dark grey")
info_label.grid(row=0, column=0)

# Function to handle search based on selected category
def search():
    str_cat_box = str(category_box.get()).lower().strip()
    if str_cat_box == 'title':
        # New window for title search
        root1 = tkinter.Toplevel()
        root1.title("Searching")
        root1.configure(bg="dark grey")

        # UI setup for title input
        title_label = tkinter.Label(root1, text="Full Title:")
        title_label.configure(bg="dark grey")
        title_label.grid(row=0, column=0)

        tile_warning = tkinter.Label(root1, text="Warning! First letter of each \n word has to be capital")
        tile_warning.configure(bg="yellow")
        tile_warning.grid(row=1, column=0)

        title_box = tkinter.Entry(root1, width=23)
        title_box.grid(row=0, column=1, padx=5, pady=7, sticky='w')

        # Function to check if title exists in the Netflix catalog
        def title():
            input_title = str(title_box.get().lower().title())
            os.chdir(r"C:\Users")
            netflix_csv = pd.read_csv("netflix_titles.csv")
            column = netflix_csv.title

            try: 
                for row in column:
                    if row == input_title:
                        input_title_send.append(input_title)
                        tkinter.messagebox.showinfo("Success!", "The title you searched for was found on Netflix's catalog")
            except:
                tkinter.messagebox.showinfo("No Luck!", "Could not find anything with that title")

        # Buttons to generate list and send title to phone
        genre_button = tkinter.Button(root1, text="           Generate list           ", command=title)
        genre_button.configure(bg="cyan") 
        genre_button.grid(row=1, column=1, sticky='w', padx=5, pady=5)

        sender_button = tkinter.Button(root1, text="Send the name to phone", command=title_sender)
        sender_button.configure(bg="pale green") 
        sender_button.grid(row=2, column=1, sticky='w', padx=5, pady=5)

        root1.mainloop()
        
    elif str_cat_box == "director":
        # New window for director search
        root1 = tkinter.Tk()
        root1.title("Searching")
        root1.configure(bg="dark grey")

        # UI setup for director input
        director_label = tkinter.Label(root1, text="Enter name of cast members:")
        director_label.configure(bg="dark grey")
        director_label.grid(row=0, column=0)

        tile_warning = tkinter.Label(root1, text="Warning! First letter of each \n word has to be capital")
        tile_warning.configure(bg="yellow")
        tile_warning.grid(row=1, column=0)

        director_box = tkinter.Entry(root1, width=23)
        director_box.grid(row=0, column=1, padx=5, pady=7, sticky='w')

        # Function to check if director exists in the Netflix catalog
        def director():
            input_director = str(director_box.get().lower().title())
            os.chdir(r"C:\Users")
            netflix_csv = pd.read_csv("netflix_titles.csv")
            column = netflix_csv.director

            try: 
                for row in column:
                    if row == input_director:
                        input_director_send.append(input_director)
                        tkinter.messagebox.showinfo("Success!", "The director you searched for was found on Netflix's catalog")
            except:
                tkinter.messagebox.showinfo("No Luck!", "Could not find anyone with that name")

        # Buttons to generate list and send director to phone
        genre_button = tkinter.Button(root1, text="           Generate list           ", command=director)
        genre_button.configure(bg="cyan") 
        genre_button.grid(row=1, column=1, sticky='w', padx=5, pady=5)

        sender_button = tkinter.Button(root1, text="Send the name to phone", command=director_name_sender)
        sender_button.configure(bg="pale green") 
        sender_button.grid(row=2, column=1, sticky='w', padx=5, pady=5)

        root1.mainloop()

    elif str_cat_box == "cast":
        # New window for cast search
        root1 = tkinter.Tk()
        root1.title("Searching")
        root1.configure(bg="dark grey")

        # UI setup for cast input
        cast_label = tkinter.Label(root1, text="Fullname of Cast Member:")
        cast_label.configure(bg="dark grey")
        cast_label.grid(row=0, column=0)

        tile_warning = tkinter.Label(root1, text="Warning! First letter of each \n word/name has to be capital")
        tile_warning.configure(bg="yellow")
        tile_warning.grid(row=1, column=0)

        cast_box = tkinter.Entry(root1, width=23)
        cast_box.grid(row=0, column=1, padx=5, pady=7, sticky='w')

        # Function to check if cast member exists in the Netflix catalog
        def cast():
            input_cast = str(cast_box.get().lower().title())
            
            # Change directory to where the Netflix catalog is located (ex. C:\Users\....)
            os.chdir(r"C:\Users")
            netflix_csv = pd.read_csv("netflix_titles.csv")
            column = netflix_csv.cast

            try: 
                for row in column:
                    if row == input_cast:
                        input_cast_send.append(input_cast)
                        tkinter.messagebox.showinfo("Success!", "The cast member you searched for was found on Netflix's catalog")
            except:
                tkinter.messagebox.showinfo("No Luck!", "Could not find any cast members with that name  \n make sure spelling is correct") 

        # Buttons to generate list and send cast name to phone
        genre_button = tkinter.Button(root1, text="           Generate list           ", command=cast)
        genre_button.configure(bg="cyan") 
        genre_button.grid(row=1, column=1, sticky='w', padx=5, pady=5)

        sender_button = tkinter.Button(root1, text="Send the name to phone", command=cast_name_sender)
        sender_button.configure(bg="pale green") 
        sender_button.grid(row=2, column=1, sticky='w', padx=5, pady=5)

        root1.mainloop()

    else: 
        tkinter.messagebox.showwarning("Failed", "Please enter topic from list!")

# Main page buttons to trigger search or close program
finder_button = tkinter.Button(root, text="Search", command=search)
finder_button.configure(bg="cyan") 
finder_button.grid(row=0, column=4, sticky='w', padx=5, pady=5)

close_button = tkinter.Button(root, text=" Close ", command=killer) 
close_button.configure(bg="red") 
close_button.grid(row=1, column=4, sticky='w', padx=5, pady=5)

root.mainloop()