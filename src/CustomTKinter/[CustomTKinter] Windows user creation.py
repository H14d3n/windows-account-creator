from tkinter import *
import customtkinter
import subprocess
import os

#Theme of Application
customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("blue")
customtkinter.deactivate_automatic_dpi_awareness()

# Function to create account
def create_account():
    # Get Username and save into new var
    end_username = username.get()
    end_password = password.get()
    is_checked =  admin_check_var.get()

    # Take variables and execute command
    user_command = f"net user {end_username} {end_password} /add"

    print("Executing command:", user_command)

    try:
        subprocess.run(user_command, shell=True, check=True)
        print("User created successfully!")
    except subprocess.CalledProcessError as e:
        print("Error creating user:", e)
        return

    # If checkbox is checked, add user to administrator group
    if is_checked:

        admin_group_name = determine_admin_group()
        
        if admin_group_name:
            admin_command = f"net localgroup {admin_group_name} {end_username} /add"
            print("Executing command:", admin_command)

            try:
                subprocess.run(admin_command, shell=True, check=True)
                print(f"User '{end_username}' added to {admin_group_name} group successfully.")
            except subprocess.CalledProcessError as e:
                print(f"Error adding user to {admin_group_name} group: {e}")
                return
        else:
            print("No suitable admin group found.")
        
# This functions checks / iterates through every object in array, then returns existing groupname
def determine_admin_group():
    admin_groups = ["Administrateurs", "Administratoren", "Administrators"]
    for group in admin_groups:
        result = subprocess.run (f"net localgroup {group}", shell=True, capture_output=True, text=True) 
        if "alias does not exist" not in result.stderr:
            return group
    return None       
    

root = customtkinter.CTk()

# Create Window for GUI and add Icon 
root.title('Offline Account Creator')
root.geometry('350x350')
root.resizable(False, False)

# Title Account Creator centered
title = customtkinter.CTkLabel(root, text="Account Creator", font=('Bold Calibri', 25))
title.place(relx=0.25, rely=0.1)

# Entry for Username
username = customtkinter.CTkEntry(root, corner_radius=10, width=140, height=40, fg_color="#ffffff", text_color="#000000", placeholder_text="Username")
username.place(relx=0.3, rely=0.3)

# Entry for Password
password = customtkinter.CTkEntry(root, corner_radius=10, width=140, height=40, fg_color="#ffffff", text_color="#000000", placeholder_text="Password")
password.configure(show="*")
password.place(relx=0.3, rely=0.45)

# Checkbox if admin is needed
admin_check_var = BooleanVar()
admin_check = customtkinter.CTkCheckBox(root, corner_radius=10, fg_color="#ffffff", checkmark_color="#000000", text="Administrator", variable=admin_check_var)
admin_check.place(relx=0.35, rely=0.625)

# Function so that the button press works -> linked in command
def submit_pressed():
    create_account()

# Submit button, linked with submit_pressed function
submit = customtkinter.CTkButton(root, corner_radius=10, text="Submit", fg_color="#ffffff", hover_color="#A9A9A9", text_color="#000000", command=submit_pressed)
submit.place(relx=0.5, rely=0.8, anchor=customtkinter.CENTER)


root.mainloop()