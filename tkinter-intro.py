from tkinter import *

############## Create the GUI ##############

def login():
    # Get the username and password and check if they are correct

    if username.get() == "username" and password.get() == "password":
        # Display success message
        print("Success!")
        success_message.set("You are now logged in!")
    else:
        print("Wrong!")
        username.set("")
        password.set("")


# Create root window
root = Tk()
root.title("My first GUI")

w = 420 # width for the Tk root
h = 120 # height for the Tk root

ws = root.winfo_screenwidth() # width of the screen
hs = root.winfo_screenheight() # height of the screen
# calculate x and y coordinates for the Tk root window
x = (ws/2) - (w/2)
y = (hs/2) - (h/2)

# set the dimensions of the screen
# and where it is placed
root.geometry('%dx%d+%d+%d' % (w, h, x, y))


#root.resizable(width=FALSE, height=FALSE)
#root.geometry('200x150')

user_label = Label(root, text="username")
user_label.grid(row=0, column=0)

password_label = Label(root, text="password")
password_label.grid(row=1, column=0)

username = StringVar()
password = StringVar()

user_entry = Entry(root, textvariable=username)
user_entry.grid(row=0, column=1)

password_entry = Entry(root, textvariable=password)
password_entry.grid(row=1, column=1)

# Add a login button
login_button = Button(root, text="login", fg="white", command=login)
login_button.grid(row=2, column=1)

# label to display a message after user logs in
success_message = StringVar()
success_message.set("Enter your login details")
success_label = Label(root, textvariable=success_message)
success_label.grid(row=3, column=3)

# run the program
root.mainloop()
