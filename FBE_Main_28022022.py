import os
import funcs
from tkinter import *
from tkinter import messagebox
from tkinter.ttk import *


# ---------------------------- UI SETUP ------------------------------- #

windows = Tk()
windows.title("FBE Finder")
windows.config(padx=0, pady=0, bg="Black")

canvas = Canvas(width=500, height=512, bg="Black", highlightthickness=0)
lock_image = PhotoImage(file="FBE.png")
canvas.create_image(256, 256, image=lock_image)
canvas.grid(column=1, row=0)

style = Style()

style.configure('TButton', font=('calibri', 12, 'bold'), borderwidth='4')

style_label = Style()
style_label.configure("BW.TLabel", foreground="white", background="#0e0604")

# Changes will be reflected
# by the movement of mouse.
style.map('TButton', foreground=[('active', '!disabled', 'blue')],
          background=[('active', 'black')])

# ---------------------------- Buttons ------------------------------- #

bmc_button = Button(text="BMC", width=6, command=path_finder)
bmc_button.place(x=156, y=336)

ics_button = Button(text="ICS", width=6, command=path_finder)
ics_button.place(x=156, y=396)

db_button = Button(text="DB", width=6, command=path_finder)
db_button.place(x=156, y=456)

ad_button = Button(text="AD", width=6, command=path_finder)
ad_button.place(x=284, y=336)

av_button = Button(text="AV", width=6)
av_button.place(x=284, y=396)

client_button = Button(text="Client", width=6, command=path_finder)
client_button.place(x=284, y=456)

# ---------------------------- Label ------------------------------- #

component_text = Label(text="Select the component:",style="BW.TLabel" , font=("calibri", 18, "bold"))
component_text.place(x=136, y=275)

windows.mainloop()

