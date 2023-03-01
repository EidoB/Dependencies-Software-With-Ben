from tkinter import *
from tkinter.ttk import *



def change_screen():
    for main_screen in windows.winfo_children():
        main_screen.destroy()


# ---------------------------- UI MAIN PROGRAM ------------------------------- #


windows = Tk()
windows.title("FBE-DC")
windows.config(padx=0, pady=0, bg="Black")

canvas = Canvas(width=500, height=512, bg="Black", highlightthickness=0)
lock_image = PhotoImage(file="FBE.png")
canvas.create_image(256, 256, image=lock_image)
canvas.grid(column=1, row=0)

style = Style()

style.configure('TButton', font=('calibri', 14, 'bold'), borderwidth='4')

style_label = Style()
style_label.configure("BW.TLabel", foreground="white", background="#0e0604")

style.map('TButton', foreground=[('active', '!disabled', 'blue')],
          background=[('active', 'black')])

# ---------------------------- Buttons ------------------------------- #


bmc_button = Button(text="BMC", width=6)
bmc_button.place(x=156, y=336)

ics_button = Button(text="ICS", width=6)
ics_button.place(x=156, y=396)

db_button = Button(text="DB", width=6)
db_button.place(x=276, y=336)

client_button = Button(text="Client", width=6)
client_button.place(x=276, y=396)

# ---------------------------- Label ------------------------------- #

component_text = Label(text="Select the component:", style="BW.TLabel", font=("calibri", 18, "bold"))
component_text.place(x=136, y=275)


windows.mainloop()
