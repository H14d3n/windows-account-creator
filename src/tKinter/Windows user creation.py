import tkinter
import os
from tkinter import messagebox

def create_account():
    username = username_entry.get()
    password = password_entry.get()

    # Create user account
    command_create_user = f"net user {username} {password} /add"
    os.system(command_create_user)

    if admin_var.get():
        command_add_admin = f"net localgroup administrators {username} /add"
        os.system(command_add_admin)

    messagebox.showinfo("Account created!", f"User '{username}' has been created.")


window = tkinter.Tk()
window.title("Windows offline-user creation")

frame = tkinter.Frame(window)
frame.pack()

# Benutzer Informationen speichern
user_info_frame = tkinter.LabelFrame(frame, text="Information")
user_info_frame.grid(row=0, column=0)

username_label = tkinter.Label(user_info_frame, text="Username")
username_label.grid(row=0, column=0)
password_label = tkinter.Label(user_info_frame, text="Password")
password_label.grid(row=1, column=0)

username_entry = tkinter.Entry(user_info_frame)
username_entry.grid(row=0, column=1)
password_entry = tkinter.Entry(user_info_frame, show="*")
password_entry.grid(row=1, column=1)

admin_var = tkinter.IntVar()
admin_checkbox = tkinter.Checkbutton(user_info_frame, text="Administrator", variable=admin_var)
admin_checkbox.grid(row=2, column=1)

create_button = tkinter.Button(user_info_frame, text="Create", command=create_account)
create_button.grid(row=3, column=1)

window.mainloop()
