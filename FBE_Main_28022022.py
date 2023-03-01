import os
from tkinter import *
from tkinter import messagebox
from tkinter.ttk import *


# ---------------------------- FUNCTIONS ------------------------------- #

def path_finder():
    path_list = os.environ.get('PATH').split(os.pathsep)
    ###Error example
    # python_path = "C:\\Users\\bene\\AppData\\Local\\Programs\\Python\\Python3\\"
    # python_script_path = "C:\\Users\\bene\\AppData\\Local\\Programs\\Python\\Python37\\Scripts"

    ##Clear example
    python_path = "C:\\Users\\bene\\AppData\\Local\\Programs\\Python\\Python37\\"
    python_script_path = "C:\\Users\\bene\\AppData\\Local\\Programs\\Python\\Python37\\Scripts\\"

    messages = []
    if python_path not in path_list:
        python_missing = f"{python_path} does not exist in the PATH environment variable."
        messages.append(python_missing)
    else:
        pass

    if python_script_path not in path_list:
        python_script_missing = f"{python_script_path} does not exist in the PATH environment variable."
        messages.append(python_script_missing)
    else:
        pass

    messages_printing = (', '.join(messages))
    if len(messages) == 0:
        messagebox.showinfo(title="Path Search", message="All paths exist")
    else:
        messagebox.showwarning(title="Warning!",
                               message=f"I found that missing {len(messages)} paths:\n{messages_printing}")


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
# Set the Python path you want to check
# python_path = "C:/Python39"


# Get the list of paths in the PATH environment variable


# Check if the Python path exists in the list of paths
