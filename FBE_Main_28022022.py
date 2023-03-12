from tkinter import *
from tkinter.ttk import *


def change_screen():
    for main_screen in windows.winfo_children():
        main_screen.destroy()


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

style.map('TButton', foreground=[('active', '!disabled', 'blue')],
          background=[('active', 'black')])

def close():
    windows.destroy()


def main_screen():
    global bmc_button, ics_button, db_button, client_button, component_text

    bmc_button = Button(text="BMC", width=9)
    bmc_button.place(x=130, y=315)

    db_button = Button(text="DB", width=9)
    db_button.place(x=270, y=315)

    ics_button = Button(text="Tomer", width=9)
    ics_button.place(x=130, y=370)

    client_button = Button(text="Client", width=9)
    client_button.place(x=270, y=370)

    component_text = Label(text="Select the Component:", style="BW.TLabel", font=("calibri", 18, "bold"))
    component_text.place(x=136, y=265)

    Button(text="Exit", width=4, command=close).place(x=440, y=470)


main_screen()
windows.mainloop()
