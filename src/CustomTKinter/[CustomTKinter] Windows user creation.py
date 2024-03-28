from tkinter import *
import customtkinter
import subprocess
import os

#Theme of Application
customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("blue")
customtkinter.deactivate_automatic_dpi_awareness()

root = customtkinter.CTk()

root.title('Offline Account Creator')
root.geometry('350x350')

title = customtkinter.CTkLabel(root, text="Account Creator", font=('Calibri', 25))
title.place(relx=0.275, rely=0.1)

username = customtkinter.CTkEntry(root, corner_radius=10, width=140, height=40, fg_color="#ffffff", text_color="#000000", placeholder_text="Username")
username.place(relx=0.3, rely=0.3)

password = customtkinter.CTkEntry(root, corner_radius=10, width=140, height=40, fg_color="#ffffff", text_color="#000000", placeholder_text="Password")
password.place(relx=0.3, rely=0.45)

admin_check = customtkinter.CTkCheckBox(root, corner_radius=10, fg_color="#ffffff", checkmark_color="#000000", text="Administrator")
admin_check.place(relx=0.35, rely=0.625)

submit = customtkinter.CTkButton(root, corner_radius=10, text="Submit", fg_color="#ffffff", hover_color="#A9A9A9", text_color="#000000")
submit.place(relx=0.5, rely=0.8, anchor=customtkinter.CENTER)


root.mainloop()

def create_user():
    # Lesen Sie den Benutzernamen und das Passwort
    user = username.get()
    passwd = password.get()
    
    # Überprüfen, ob der Administrator ausgewählt ist
    admin = " /add" if admin_check.get() else ""

    command = f"net user {user} {passwd}{admin}"
    result = subprocess.run(command, capture_output=True, text=True, shell=True)
    
    if result.returncode == 0:
        print("Benutzer erfolgreich erstellt.")
    else:
        print("Fehler beim Erstellen des Benutzers:", result.stderr)

