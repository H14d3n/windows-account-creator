import os
import ctypes
import subprocess
import customtkinter
from tkinter import BooleanVar

# Theme of Application
customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("blue")
customtkinter.deactivate_automatic_dpi_awareness()

special_characters = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '-', '_', '=', '+', '{', '}', '[', ']', '|', '\\', ':', ';', '"', "'", '<', '>', ',', '.', '?', '/', '~', '`']
alphabet_characters = list("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ")

# Function to create account
def create_account():
    # Get Username and Password
    end_username = username.get()
    end_password = password.get()
    is_checked = admin_check_var.get()

    if len(end_username) > 0 and len(end_password) >= 5:

        if any(char in end_password for char in special_characters):
            if "12345" in end_password:
                error_message("More Complex Password")
            elif not any(char in end_password for char in alphabet_characters):
                error_message("Password must contain letters")   
            elif not run_as_admin():    
                error_message("Run program as administrator")
            else:    
                # Create user account
                user_command = f"net user {end_username} {end_password} /add"
                print("Executing command:", user_command)
                try:
                    subprocess.run(user_command, shell=True, check=True)
                    success_message("User created successfully!")
                except subprocess.CalledProcessError as e:
                    error_message(f"Error creating user: {e}")
                    return

                # Add user to administrator group if checkbox is checked
                if is_checked:
                    admin_group_name = determine_admin_group()
                    if admin_group_name:
                        admin_command = f"net localgroup \"{admin_group_name}\" {end_username} /add"
                        print("Executing command:", admin_command)
                        try:
                            subprocess.run(admin_command, shell=True, check=True)
                            success_message(f"User '{end_username}' added to {admin_group_name} group successfully.")
                        except subprocess.CalledProcessError as e:
                            error_message(f"Error adding user to {admin_group_name} group: {e}")
                    else:
                        error_message("No suitable admin group found.")
        else:
            error_message("Password should contain special characters")            
    else: 
        error_message("Username or password too short")        
        
# Function to determine the correct admin group
def determine_admin_group():
    admin_groups = ["Administrateurs", "Administratoren", "Administrators"]
    for group in admin_groups:
        result = subprocess.run(f"net localgroup \"{group}\"", shell=True, capture_output=True, text=True)
        if result.returncode == 0:
            return group
    return None

def success_message(message):
    message_label = customtkinter.CTkLabel(root, text=message, font=('Bold Calibri', 10), text_color="green")
    message_label.place(relx=0.1, rely=0.875, relwidth=0.8)    

def error_message(message):
    message_label = customtkinter.CTkLabel(root, text=message, font=('Bold Calibri', 10), text_color="red")
    message_label.place(relx=0.1, rely=0.875, relwidth=0.8)
    
# Function to check if the program is running as administrator
def run_as_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False

# Initialize main application window
root = customtkinter.CTk()
root.title('Offline Account Creator')
root.geometry('350x350')
root.resizable(False, False)
root.iconbitmap(".\src\CustomTKinter\image-removebg-preview.ico")

# Title label
title = customtkinter.CTkLabel(root, text="Account Creator", font=('Bold Calibri', 25))
title.place(relx=0.25, rely=0.1)

# Entry for Username
username = customtkinter.CTkEntry(root, corner_radius=10, width=140, height=40, fg_color="#ffffff", text_color="#000000", placeholder_text="Username")
username.place(relx=0.3, rely=0.3)

# Entry for Password
password = customtkinter.CTkEntry(root, corner_radius=10, width=140, height=40, fg_color="#ffffff", text_color="#000000", placeholder_text="Password", show="*")
password.place(relx=0.3, rely=0.45)

# Checkbox for admin privilege
admin_check_var = BooleanVar()
admin_check = customtkinter.CTkCheckBox(root, corner_radius=10, fg_color="#ffffff", checkmark_color="#000000", text="Administrator", variable=admin_check_var)
admin_check.place(relx=0.35, rely=0.625)

# Function to handle submit button press
def submit_pressed():
    create_account()

# Submit button
submit = customtkinter.CTkButton(root, corner_radius=10, text="Submit", fg_color="#ffffff", hover_color="#A9A9A9", text_color="#000000", command=submit_pressed)
submit.place(relx=0.5, rely=0.8, anchor=customtkinter.CENTER)

root.mainloop()
