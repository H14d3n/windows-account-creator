# tKinter-Experiment
Brief simplification of the user creation process in Windows, implemented in python.

### Version with CustomTKinter
![image](https://github.com/H14d3n/tKinter-experiment/assets/146072924/fbaa6dbb-0237-43e9-ad36-71cf0633fcc2)

### `Version with TKinter`
![image](https://github.com/H14d3n/tKinter-experiment/assets/146072924/0b755d6c-e133-4910-8824-5f46fc3b7fc4)

I think you can see the clear winner here. Though I must admit, I didn't spend that much time with the TKinter version. ;D

## Offline Account Creator

This Python script utilizes Tkinter, a standard GUI toolkit for Python, along with custom styling provided by the `customtkinter` module. It allows users to create offline accounts on a Windows system.

### Setup

- The script imports necessary modules such as Tkinter (`from tkinter import *`), a custom Tkinter module (`import customtkinter`), subprocess (`import subprocess`), and os (`import os`).

### Theme and Styling

- The appearance mode of the application is set to "dark" using `customtkinter.set_appearance_mode("dark")`.
- The default color theme is set to "blue" with `customtkinter.set_default_color_theme("blue")`.
- Automatic DPI awareness is deactivated using `customtkinter.deactivate_automatic_dpi_awareness()`.

### Account Creation Function

- The `create_account()` function is defined to handle the creation of user accounts.
- It retrieves the username and password entered by the user and checks if the "Administrator" checkbox is selected.
- Based on the checkbox selection, it constructs a command to create the user account using `net user` command or add the user to the administrators group using `net localgroup administrators` command.
- The constructed command is executed using `subprocess.run()`.

### GUI Setup

- A Tkinter root window is created using `customtkinter.CTk()`.
- The window title is set to "Offline Account Creator" with `root.title('Offline Account Creator')`.
- Window dimensions are set to 350x350 pixels using `root.geometry('350x350')`.
- An icon is set for the window using `root.iconbitmap()`.

### Widgets

- A title label "Account Creator" is created using `customtkinter.CTkLabel`.
- Entry fields for username and password are created using `customtkinter.CTkEntry`.
- A checkbox for selecting the administrator role is created using `customtkinter.CTkCheckBox`.
- A submit button labeled "Submit" is created using `customtkinter.CTkButton`.

### Event Handling

- The `submit_pressed()` function is defined to handle button press events. It calls the `create_account()` function.

### Execution

- The Tkinter event loop is started using `root.mainloop()` to run the GUI application.

