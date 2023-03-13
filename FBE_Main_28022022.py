from tkinter import *
from tkinter.ttk import *

from funcs import *

# ---------------------------- UI MAIN PROGRAM ------------------------------- #


windows = Tk()
windows.title("FBE Dependency Checker")
windows.config(padx=0, pady=0, bg="Black")
windows.resizable(False, False)
windows.iconbitmap("firebolt1.ico")

canvas = Canvas(width=500, height=512, bg="Black", highlightthickness=0)
lock_image = PhotoImage(file="FBE.png")
canvas.create_image(256, 256, image=lock_image)
canvas.grid(column=1, row=0)

style = Style()

style.configure('TButton', font=('calibri', 14, 'bold'))

style_label = Style()
style_label.configure("BW.TLabel", foreground="white", background="#0e0604")

style.map('TButton', foreground=[('active', '!disabled', 'blue')],background=[('active', 'black')])


def close():
    windows.destroy()


def about():
    messagebox.showinfo(title="About", message="Integration dependencies application Version 1.0 by Ben Eytan & Eido Bennun ")


def main_screen():
    bmc_button = Button(text="BMC", width=9, command=bmc_checker)
    bmc_button.place(x=130, y=315)

    db_button = Button(text="DB", width=9, command=db_checker)
    db_button.place(x=270, y=315)

    ics_button = Button(text="ICS", width=9, command=ics_checker)
    ics_button.place(x=130, y=370)

    client_button = Button(text="Client", width=9, command=client_checker)
    client_button.place(x=270, y=370)

    component_text = Label(text="Select the Component:", style="BW.TLabel", font=("calibri", 18, "bold"))
    component_text.place(x=136, y=265)

    Button(text="Exit", width=5, command=close).place(x=430, y=470)
    Button(text="About", width=5, command=about).place(x=360, y=470)


main_screen()
windows.mainloop()
