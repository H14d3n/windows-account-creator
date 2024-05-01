from tkinter import messagebox, IntVar, LabelFrame, Tk, Frame, Label, Entry, Checkbutton, Button
import os

# Function to collect user information from frames and check if administrator box is checked.
def create_account(username_entry, password_entry, admin_var):
    username = username_entry.get()
    password = password_entry.get()

    command_create_user = f"net user {username} {password} /add"
    os.system(command_create_user)

    if admin_var.get():
        command_add_admin = f"net localgroup administrators {username} /add"
        os.system(command_add_admin)

    messagebox.showinfo("Account created!", f"User '{username}' has been created.")

# Main GUI
def main():
    window = Tk()
    window.title("Windows offline-user creation")

    frame = Frame(window)
    frame.pack()

    user_info_frame = LabelFrame(frame, text="Information")
    user_info_frame.grid(row=0, column=0, padx=10, pady=10)

    username_label = Label(user_info_frame, text="Username")
    username_label.grid(row=0, column=0, padx=5, pady=5)
    password_label = Label(user_info_frame, text="Password")
    password_label.grid(row=1, column=0, padx=5, pady=5)

    username_entry = Entry(user_info_frame)
    username_entry.grid(row=0, column=1, padx=5, pady=5)
    password_entry = Entry(user_info_frame, show="*")
    password_entry.grid(row=1, column=1, padx=5, pady=5)

    admin_var = IntVar()
    admin_checkbox = Checkbutton(user_info_frame, text="Administrator", variable=admin_var)
    admin_checkbox.grid(row=2, column=1, padx=5, pady=5)

    create_button = Button(user_info_frame, text="Create", command=lambda: create_account(username_entry, password_entry, admin_var))
    create_button.grid(row=3, column=1, padx=5, pady=5)

    window.mainloop()

if __name__ == "__main__":
    main()
