import tkinter as tk
from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
import csv

logs = Tk()
logs.geometry("990x800")
logs.title("Auto servisa kalkulators")


foto_frame = tk.Frame(logs)
foto_frame.grid(row=1, column=1, padx=5, pady=5)
foto_image = Image.open("vw logo.png")
resized_foto = foto_image.resize((200, 200))
foto = ImageTk.PhotoImage(resized_foto)
foto_label = ttk.Label(foto_frame, image=foto)
foto_label.grid(row=1, column=1,columnspan=2, padx=10, pady=40)

ttk.Label(logs, text="Auto servisa remonta kalkulators", font=("Helvetica", 27, "bold")).grid(row=1, column=2, columnspan=3, pady=40, padx=5)

ttk.Label(logs, text="Auto marka:", font=("Helvetica", 14)).grid(row=2, column=1, pady=5, padx=5, sticky="e")
marka = ttk.Combobox(logs, state="readonly", values=["Volkswagen"])
marka.current(0)
marka.grid(row=2, column=2, pady=5, padx=5)

ttk.Label(logs, text="Auto modelis:", font=("Helvetica", 14)).grid(row=2, column=3, pady=5, padx=5,sticky="e")
modelis = ttk.Combobox(logs, state="readonly", values=["Golf 5"])
modelis.current(0)
modelis.grid(row=2, column=4, pady=5, padx=5)

ttk.Label(logs, text="Izvēlieties nepieciešamos pakalpojumus:", font=("Helvetica", 12, "bold")).grid(row=3, column=1, columnspan=4, sticky="w", padx=30, pady=10)










e1 = BooleanVar()
pak1 = Checkbutton(logs, text="Eļļas maiņa (+ filtrs)", variable=e1)
pak1.grid(row=4, column=1, padx=10)

e2 = BooleanVar()
pak2 = Checkbutton(logs,text="Filtru maiņa (degvielas, gaisa, salona)", variable=e2)
pak2.grid(row=5, column=1, padx=10)

e3 = BooleanVar()
pak3 = Checkbutton(logs,text="Dzesēšanas šķidruma maiņa", variable=e3)
pak3.grid(row=6, column=1, padx=10)

e4 = BooleanVar()
pak4 = Checkbutton(logs,text="Kondicioniera uzpilde", variable=e4)
pak4.grid(row=7, column=1, padx=10)

e5 = BooleanVar()
pak5 = Checkbutton(logs,text="Bremžu disku un kluču mainā", variable=e5)
pak5.grid(row=8, column=1, padx=10)

e6 = BooleanVar()
pak6 = Checkbutton(logs,text="Auto diagnostika", variable=e6)
pak6.grid(row=9, column=1, padx=10)

e7 = BooleanVar()
pak7 = Checkbutton(logs,text="Kvēpu filtra tīrīša", variable=e7)
pak7.grid(row=10, column=1, padx=10)

e8 = BooleanVar()
pak8 = Checkbutton(logs,text="Kvēlsveču maiņa", variable=e8)
pak8.grid(row=4, column=2, padx=10)

e9 = BooleanVar()
pak9 = Checkbutton(logs,text="Savirzes regulēšana", variable=e9)
pak9.grid(row=5, column=2, padx=10)

e10 = BooleanVar()
pak10 = Checkbutton(logs,text="Amortizātoru nomaiņa", variable=e10)
pak10.grid(row=6, column=2, padx=10)

e11 = BooleanVar()
pak11 = Checkbutton(logs,text="Atsperu nomaiņa", variable=e11)
pak11.grid(row=7, column=2, padx=10)

e12 = BooleanVar()
pak12 = Checkbutton(logs,text="Stūres pastiprinātāja remonts", variable=e12)
pak12.grid(row=8, column=2, padx=10)

e13 = BooleanVar()
pak13 = Checkbutton(logs,text="Eļļas noplūdes novēršana (blīvju maiņa)", variable=e13)
pak13.grid(row=9, column=2, padx=10)

e14 = BooleanVar()
pak14 = Checkbutton(logs,text="Bremžu šķidruma maiņa", variable=e14)
pak14.grid(row=10, column=2, padx=10)

e15 = BooleanVar()
pak15 = Checkbutton(logs,text="Degvielas sūkņa maiņa", variable=e15)
pak15.grid(row=4, column=3, padx=10)

e16 = BooleanVar()
pak16 = Checkbutton(logs,text="Atrumkārbas eļļas maiņa", variable=e16)
pak16.grid(row=5, column=3, padx=10)

e17 = BooleanVar()
pak17 = Checkbutton(logs,text="Lukturu maiņa ur regulēšana", variable=e17)
pak17.grid(row=6, column=3, padx=10)

e18 = BooleanVar()
pak18 = Checkbutton(logs,text="Udens sūkņa maiņa", variable=e18)
pak18.grid(row=7, column=3, padx=10)

e19 = BooleanVar()
pak19 = Checkbutton(logs,text="Ģenerātora maiņa", variable=e19)
pak19.grid(row=8, column=3, padx=10)

e20 = BooleanVar()
pak20 = Checkbutton(logs,text="Turbīnas maiņa", variable=e20)
pak20.grid(row=9, column=3, padx=10)

e21 = BooleanVar()
pak21 = Checkbutton(logs,text="Zobsiksnas maiņa", variable=e21)
pak21.grid(row=10, column=3, padx=10)


pak_info = {
    pak1: [20, 15, 1.0],
}


kopejascenas=tk.Listbox(logs, width=40, height=5, bg="black", fg="white", font=("Helvetica", 16, "bold"))
kopejascenas.grid(row=11, column=1, columnspan=4, pady=1, padx=1)




Button(logs, text="Saglabāt", font=("Helvetica", 12, "bold")).grid(row=12, column=1, columnspan=4, pady=10)
ttk.Label(logs, text="Saziņa ar servisu: +37112345678  vwserviss@epasts.com", font=("Helvetica",15,"bold")).grid(row=13, column=2, columnspan=2,pady=1, padx=1)





logs.mainloop()