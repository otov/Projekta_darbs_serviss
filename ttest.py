import tkinter as tk
from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
import csv

logs = Tk()
logs.geometry("1300x800")
logs.title("Auto servisa kalkulators")

foto_frame = tk.Frame(logs)
foto_frame.grid(row=1, column=1, padx=5, pady=5)
foto_image = Image.open("vw logo.png")
resized_foto = foto_image.resize((100, 100))
foto = ImageTk.PhotoImage(resized_foto)
foto_label = ttk.Label(foto_frame, image=foto)
foto_label.grid(row=1, column=1, padx=10, pady=40)

ttk.Label(logs, text="Auto servisa remonta kalkulators", font=("Helvetica", 26, "bold")).grid(row=1, column=3, pady=40, padx=5)

ttk.Label(logs, text="Auto marka:", font=("Helvetica", 14)).grid(row=2, column=1, pady=5, padx=5, sticky="e")
marka = ttk.Combobox(logs, state="readonly", values=["Volkswagen"])
marka.current(0)
marka.grid(row=2, column=2, pady=5, padx=5)

ttk.Label(logs, text="Auto modelis:", font=("Helvetica", 14)).grid(row=2, column=3, pady=5, padx=5, sticky="e")
modelis = ttk.Combobox(logs, state="readonly", values=["Golf 5"])
modelis.current(0)
modelis.grid(row=2, column=4, pady=5, padx=5)

ttk.Label(logs, text="Izvēlieties nepieciešamos pakalpojumus:", font=("Helvetica", 12, "bold")).grid(row=3, column=1, columnspan=4, sticky="w", padx=30, pady=10)


e1 = BooleanVar()
pak1 = Checkbutton(logs, text="Eļļas maiņa (+ filtrs)", variable=e1)
pak1.grid(row=4, column=1, sticky="w", padx=10)


pak_info = {
    pak1: [20, 15, 1.0],
}



Button(logs, text="Saglabāt", font=("Helvetica", 12, "bold")).grid(row=12, column=1, columnspan=4, pady=10)

logs.mainloop()