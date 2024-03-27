import tkinter as tk
from tkinter import ttk

def on_button_click():
    input_text = input_entry.get()
    print("Eingegebener Text:", input_text)

root = tk.Tk()
root.title("Rundes Eingabefeld")

# Hintergrundfarbe setzen
root.configure(bg="#87CEEB")

# Funktion für das Rundmachen eines Widgets
def round_rectangle(x1, y1, x2, y2, radius=25, **kwargs):
    points = [x1+radius, y1,
              x1+radius, y1,
              x2-radius, y1,
              x2-radius, y1,
              x2, y1,
              x2, y1+radius,
              x2, y1+radius,
              x2, y2-radius,
              x2, y2-radius,
              x2, y2,
              x2-radius, y2,
              x2-radius, y2,
              x1+radius, y2,
              x1+radius, y2,
              x1, y2,
              x1, y2-radius,
              x1, y2-radius,
              x1, y1+radius,
              x1, y1+radius,
              x1, y1]
    return canvas.create_polygon(points, **kwargs, smooth=True)

# Erstellen eines Canvas
canvas = tk.Canvas(root, bg="#87CEEB", highlightthickness=0)
canvas.pack(fill="both", expand=True)

# Koordinaten für das runde Eingabefeld
x1, y1, x2, y2 = 50, 50, 250, 100

# Rundes Eingabefeld erstellen
round_rectangle(x1, y1, x2, y2, radius=20, fill="white")
input_entry = tk.Entry(root, bg="white", bd=0)
input_entry.place(x=60, y=60, width=180, height=30)

# Button erstellen
button = ttk.Button(root, text="Klick mich!", command=on_button_click)
button.place(x=120, y=150, width=100, height=30)

root.mainloop()
