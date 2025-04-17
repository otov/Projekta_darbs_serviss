import tkinter as tk
from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
import csv

logs = Tk()
logs.geometry("1130x850")
logs.title("Auto servisa kalkulators")


foto_frame = tk.Frame(logs)
foto_frame.grid(row=1, column=1, padx=5, pady=5)
foto_image = Image.open("vw logo.png")
resized_foto = foto_image.resize((200, 200))
foto = ImageTk.PhotoImage(resized_foto)
foto_label = ttk.Label(foto_frame, image=foto)
foto_label.grid(row=1, column=1,columnspan=2, padx=10, pady=40)

ttk.Label(logs, text="Auto servisa remonta kalkulators", font=("Helvetica", 27, "bold")).grid(row=1, column=2, columnspan=3, pady=40, padx=5)

ttk.Label(logs, text="Auto marka:", font=("Helvetica", 14)).grid(row=2, column=1, pady=5, padx=10, sticky="e")
marka = ttk.Combobox(logs, state="readonly", values=["Volkswagen"])
marka.current(0)
marka.grid(row=2, column=2, pady=5, padx=10, sticky="w")

ttk.Label(logs, text="Auto modelis:", font=("Helvetica", 14)).grid(row=2, column=3, pady=5, padx=10,sticky="e", columnspan=1)
modelis = ttk.Combobox(logs, state="readonly", values=["Golf 5"])
modelis.current(0)
modelis.grid(row=2, column=4, pady=5, padx=10, sticky="w", columnspan=1)

ttk.Label(logs, text="Izvēlieties nepieciešamos pakalpojumus:", font=("Helvetica", 12, "bold")).grid(row=3, column=1, columnspan=4, sticky="w", padx=10, pady=10)

#def aprekins():



#def pievieno():






e1 = BooleanVar()
pak1 = Checkbutton(logs, text="Eļļas maiņa (+ filtrs)", variable=e1)
pak1.grid(row=4, column=1, padx=10,sticky="w")

e2 = BooleanVar()
pak2 = Checkbutton(logs,text="Filtru maiņa (degvielas, gaisa, salona)", variable=e2)
pak2.grid(row=5, column=1, padx=10,sticky="w")

e3 = BooleanVar()
pak3 = Checkbutton(logs,text="Dzesēšanas šķidruma maiņa", variable=e3)
pak3.grid(row=6, column=1, padx=10,sticky="w")

e4 = BooleanVar()
pak4 = Checkbutton(logs,text="Kondicioniera uzpilde", variable=e4)
pak4.grid(row=7, column=1, padx=10,sticky="w")

e5 = BooleanVar()
pak5 = Checkbutton(logs,text="Bremžu disku un kluču maiņa", variable=e5)
pak5.grid(row=8, column=1, padx=10,sticky="w")

e6 = BooleanVar()
pak6 = Checkbutton(logs,text="Auto diagnostika", variable=e6)
pak6.grid(row=9, column=1, padx=10,sticky="w")

e7 = BooleanVar()
pak7 = Checkbutton(logs,text="Kvēpu filtra tīrīšana", variable=e7)
pak7.grid(row=10, column=1, padx=10,sticky="w")

e8 = BooleanVar()
pak8 = Checkbutton(logs,text="Kvēlsveču maiņa", variable=e8)
pak8.grid(row=4, column=2, padx=10,sticky="w")

e9 = BooleanVar()
pak9 = Checkbutton(logs,text="Savirzes regulēšana", variable=e9)
pak9.grid(row=5, column=2, padx=10,sticky="w")

e10 = BooleanVar()
pak10 = Checkbutton(logs,text="Amortizātoru maiņa", variable=e10)
pak10.grid(row=6, column=2, padx=10,sticky="w")

e11 = BooleanVar()
pak11 = Checkbutton(logs,text="Atsperu maiņa", variable=e11)
pak11.grid(row=7, column=2, padx=10,sticky="w")

e12 = BooleanVar()
pak12 = Checkbutton(logs,text="Stūres pastiprinātāja remonts", variable=e12)
pak12.grid(row=8, column=2, padx=10,sticky="w")

e13 = BooleanVar()
pak13 = Checkbutton(logs,text="Eļļas noplūdes novēršana (blīvju maiņa)", variable=e13)
pak13.grid(row=9, column=2, padx=10,sticky="w")

e14 = BooleanVar()
pak14 = Checkbutton(logs,text="Bremžu šķidruma maiņa", variable=e14)
pak14.grid(row=10, column=2, padx=10,sticky="w")

e15 = BooleanVar()
pak15 = Checkbutton(logs,text="Degvielas sūkņa maiņa", variable=e15)
pak15.grid(row=4, column=3, padx=10,sticky="w")

e16 = BooleanVar()
pak16 = Checkbutton(logs,text="Ātrumkārbas eļļas maiņa", variable=e16)
pak16.grid(row=5, column=3, padx=10,sticky="w")

e17 = BooleanVar()
pak17 = Checkbutton(logs,text="Lukturu maiņa un regulēšana", variable=e17)
pak17.grid(row=6, column=3, padx=10,sticky="w")

e18 = BooleanVar()
pak18 = Checkbutton(logs,text="Ūdens sūkņa maiņa", variable=e18)
pak18.grid(row=7, column=3, padx=10,sticky="w")

e19 = BooleanVar()
pak19 = Checkbutton(logs,text="Ģenerātora maiņa", variable=e19)
pak19.grid(row=8, column=3, padx=10,sticky="w")

e20 = BooleanVar()
pak20 = Checkbutton(logs,text="Turbīnas maiņa", variable=e20)
pak20.grid(row=9, column=3, padx=10,sticky="w")

e21 = BooleanVar()
pak21 = Checkbutton(logs,text="Zobsiksnas maiņa", variable=e21)
pak21.grid(row=10, column=3, padx=10,sticky="w")

e22 = BooleanVar()
pak22 = Checkbutton(logs,text="Akumulātora maiņa", variable=e22)
pak22.grid(row=4, column=4, padx=10,sticky="w")

e23 = BooleanVar()
pak23 = Checkbutton(logs,text="Mehāniskās ātrumkārbas remonts un maiņa", variable=e23)
pak23.grid(row=5, column=4, padx=10,sticky="w")

e24 = BooleanVar()
pak24 = Checkbutton(logs,text="Automātiskās ātrumkārbas remonts un maiņa", variable=e24)
pak24.grid(row=6, column=4, padx=10,sticky="w")

e25 = BooleanVar()
pak25 = Checkbutton(logs,text="Stūres mehānisma remonts", variable=e25)
pak25.grid(row=7, column=4, padx=10,sticky="w")

e26 = BooleanVar()
pak26 = Checkbutton(logs,text="Sprauslu remonts un maiņa", variable=e26)
pak26.grid(row=8, column=4, padx=10,sticky="w")

e27 = BooleanVar()
pak27 = Checkbutton(logs,text="Tiltu bukšu maiņa", variable=e27)
pak27.grid(row=9, column=4, padx=10,sticky="w")

e28 = BooleanVar()
pak28 = Checkbutton(logs,text="Radiatora maiņa", variable=e28)
pak28.grid(row=10, column=4, padx=10,sticky="w")



pak_info = {
    pak1: [20, 15, 1.0],
    pak2: [],
    pak3: [],
    pak4: [],
    pak5: [],
    pak6: [],
    pak7: [],
    pak8: [],
    pak9: [],
    pak10: [],
    pak11: [],
    pak12: [],
    pak13: [],
    pak14: [],
    pak15: [],
    pak16: [],
    pak17: [],
    pak18: [],
    pak19: [],
    pak20: [],
    pak21: [],
    pak22: [],
    pak23: [],
    pak24: [],
    pak25: [],
    pak26: [],
    pak27: [],
    pak28: [],
}

ttk.Label(logs, text="Ja nepieciešams cits pakalpojums lūdzu sazinaties ar servisu!", font=("Helvetica",15,"bold")).grid(row=11, column=2, columnspan=2,pady=10, padx=1)

kopejascenas=tk.Listbox(logs, width=40, height=5, bg="black", fg="white", font=("Helvetica", 16, "bold"))
kopejascenas.grid(row=12, columnspan=5, pady=10, padx=1)

Button(logs, text="Saglabāt", font=("Helvetica", 12, "bold")).grid(row=13, column=1, columnspan=2, pady=10, sticky="e")
ttk.Label(logs, text="Saziņa ar servisu: +37112345678  vwserviss@epasts.com", font=("Helvetica",15,"bold")).grid(row=14, column=2, columnspan=2,pady=1, padx=1)

logs.mainloop()