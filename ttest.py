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
    pak1: [30, 15, 0.5],
    pak2: [30, 15, 0.7],
    pak3: [15, 20, 1],
    pak4: [40, 20, 1],
    pak5: [80, 40, 1.5],
    pak6: [0, 10, 0.3],
    pak7: [0, 350, 3],
    pak8: [65, 30, 1],
    pak9: [0, 20, 0.5],
    pak10: [120, 30, 2],
    pak11: [80, 30, 2],
    pak12: [40, 40, 2],
    pak13: [20, 30, 2],
    pak14: [10, 20, 0.5],
    pak15: [35, 20, 1.5],
    pak16: [20, 15, 1],
    pak17: [15, 15, 0.5],
    pak18: [40, 20, 1.5],
    pak19: [150, 30, 2],
    pak20: [350, 40, 2],
    pak21: [100, 40, 2],
    pak22: [100, 5, 0.1],
    pak23: [500, 150, 6],
    pak24: [650, 200, 8],
    pak25: [60, 60, 3],
    pak26: [100, 60, 2],
    pak27: [30, 100, 5],
    pak28: [60, 30, 1.5],
}

ttk.Label(logs, text="Ja nepieciešams cits pakalpojums lūdzu sazinaties ar servisu!", font=("Helvetica",15,"bold")).grid(row=11, column=2, columnspan=2,pady=10, padx=1)

kopejascenas = tk.Listbox(logs, width=50, height=5, bg="black", fg="white", font=("Helvetica", 16, "bold"))
kopejascenas.grid(row=12, columnspan=5, pady=10, padx=10)

def aprekinat():
    kopejascenas.delete(0, END)  # Izdzēš iepriekšējos ierakstus
    detalas = 0
    darbs = 0
    laiks = 0

    # Aprēķina kopējās cenas un darba laiku, ņemot vērā izvēlētos pakalpojumus
    for pak, info in pak_info.items():
        if pak.cget("variable") and logs.getvar(pak.cget("variable")) == '1':
            detalas += info[0]
            darbs += info[1]
            laiks += info[2]

    kop = detalas + darbs  # Kopējā cena
    # Ievieto aprēķinātos datus listboxā
    kopejascenas.insert(END, f"Aptuvenā detaļu cena: {detalas:.2f} EUR")
    kopejascenas.insert(END, f"Aptuvenā darba cena: {darbs:.2f} EUR")
    kopejascenas.insert(END, f"Aptuvenā kopējā cena: {kop:.2f} EUR")
    kopejascenas.insert(END, f"Aptuvenais darba ilgums: {laiks:.1f} h")

# Saglabāšana
def saglabat():
    aprekinat()
    pakalpojumi = []
    detalas = 0
    darbs = 0
    laiks = 0
    for pak, info in pak_info.items():
        if pak.cget("variable") and logs.getvar(pak.cget("variable")) == '1':
            detalas += info[0]
            darbs += info[1]
            laiks += info[2]
            pakalpojumi.append(pak.cget("text"))
    with open("dati.csv", "a", newline='', encoding="utf-8") as fails:
        rakstitajs = csv.writer(fails)
        rakstitajs.writerow([marka.get(), modelis.get(), "; ".join(pakalpojumi), f"{detalas:.2f}", f"{darbs:.2f}", f"{laiks:.1f}"])
    kopejascenas.insert(END, "Dati saglabāti CSV failā.\n")

Button(logs, text="Saglabāt", font=("Helvetica", 12, "bold"), command=saglabat).grid(row=13, column=1, columnspan=2, pady=10, sticky="e")
ttk.Label(logs, text="Saziņa ar servisu: +37112345678  vwserviss@epasts.com", font=("Helvetica",15,"bold")).grid(row=14, column=2, columnspan=2,pady=1, padx=1)

logs.mainloop()






# import tkinter as tk
# from tkinter import *
# from tkinter import ttk
# from PIL import Image, ImageTk
# import csv

# logs = Tk()
# logs.geometry("1130x850")
# logs.title("Auto servisa kalkulators")

# foto_frame = tk.Frame(logs)
# foto_frame.grid(row=1, column=1, padx=5, pady=5)
# foto_image = Image.open("vw logo.png")
# resized_foto = foto_image.resize((200, 200))
# foto = ImageTk.PhotoImage(resized_foto)
# foto_label = ttk.Label(foto_frame, image=foto)
# foto_label.grid(row=1, column=1,columnspan=2, padx=10, pady=40)

# ttk.Label(logs, text="Auto servisa remonta kalkulators", font=("Helvetica", 27, "bold")).grid(row=1, column=2, columnspan=3, pady=40, padx=5)

# ttk.Label(logs, text="Auto marka:", font=("Helvetica", 14)).grid(row=2, column=1, pady=5, padx=10, sticky="e")
# marka = ttk.Combobox(logs, state="readonly", values=["Volkswagen"])
# marka.current(0)
# marka.grid(row=2, column=2, pady=5, padx=10, sticky="w")

# ttk.Label(logs, text="Auto modelis:", font=("Helvetica", 14)).grid(row=2, column=3, pady=5, padx=10,sticky="e", columnspan=1)
# modelis = ttk.Combobox(logs, state="readonly", values=["Golf 5"])
# modelis.current(0)
# modelis.grid(row=2, column=4, pady=5, padx=10, sticky="w", columnspan=1)

# ttk.Label(logs, text="Izvēlieties nepieciešamos pakalpojumus:", font=("Helvetica", 12, "bold")).grid(row=3, column=1, columnspan=4, sticky="w", padx=10, pady=10)


# e1 = BooleanVar()
# pak1 = Checkbutton(logs, text="Eļļas maiņa (+ filtrs)", variable=e1)
# pak1.grid(row=4, column=1, padx=10,sticky="w")
# pak1.var = e1

# e2 = BooleanVar()
# pak2 = Checkbutton(logs,text="Filtru maiņa (degvielas, gaisa, salona)", variable=e2)
# pak2.grid(row=5, column=1, padx=10,sticky="w")
# pak2.var = e2

# e3 = BooleanVar()
# pak3 = Checkbutton(logs,text="Dzesēšanas šķidruma maiņa", variable=e3)
# pak3.grid(row=6, column=1, padx=10,sticky="w")
# pak3.var = e3

# e4 = BooleanVar()
# pak4 = Checkbutton(logs,text="Kondicioniera uzpilde", variable=e4)
# pak4.grid(row=7, column=1, padx=10,sticky="w")
# pak4.var = e4

# e5 = BooleanVar()
# pak5 = Checkbutton(logs,text="Bremžu disku un kluču maiņa", variable=e5)
# pak5.grid(row=8, column=1, padx=10,sticky="w")
# pak5.var = e5

# e6 = BooleanVar()
# pak6 = Checkbutton(logs,text="Auto diagnostika", variable=e6)
# pak6.grid(row=9, column=1, padx=10,sticky="w")
# pak6.var = e6

# e7 = BooleanVar()
# pak7 = Checkbutton(logs,text="Kvēpu filtra tīrīšana", variable=e7)
# pak7.grid(row=10, column=1, padx=10,sticky="w")
# pak7.var = e7

# e8 = BooleanVar()
# pak8 = Checkbutton(logs,text="Kvēlsveču maiņa", variable=e8)
# pak8.grid(row=4, column=2, padx=10,sticky="w")
# pak8.var = e8

# e9 = BooleanVar()
# pak9 = Checkbutton(logs,text="Savirzes regulēšana", variable=e9)
# pak9.grid(row=5, column=2, padx=10,sticky="w")
# pak9.var = e9

# e10 = BooleanVar()
# pak10 = Checkbutton(logs,text="Amortizātoru maiņa", variable=e10)
# pak10.grid(row=6, column=2, padx=10,sticky="w")
# pak10.var = e10

# e11 = BooleanVar()
# pak11 = Checkbutton(logs,text="Atsperu maiņa", variable=e11)
# pak11.grid(row=7, column=2, padx=10,sticky="w")
# pak11.var = e11

# e12 = BooleanVar()
# pak12 = Checkbutton(logs,text="Stūres pastiprinātāja remonts", variable=e12)
# pak12.grid(row=8, column=2, padx=10,sticky="w")
# pak12.var = e12

# e13 = BooleanVar()
# pak13 = Checkbutton(logs,text="Eļļas noplūdes novēršana (blīvju maiņa)", variable=e13)
# pak13.grid(row=9, column=2, padx=10,sticky="w")
# pak13.var = e13

# e14 = BooleanVar()
# pak14 = Checkbutton(logs,text="Bremžu šķidruma maiņa", variable=e14)
# pak14.grid(row=10, column=2, padx=10,sticky="w")
# pak14.var = e14

# e15 = BooleanVar()
# pak15 = Checkbutton(logs,text="Degvielas sūkņa maiņa", variable=e15)
# pak15.grid(row=4, column=3, padx=10,sticky="w")
# pak15.var = e15

# e16 = BooleanVar()
# pak16 = Checkbutton(logs,text="Ātrumkārbas eļļas maiņa", variable=e16)
# pak16.grid(row=5, column=3, padx=10,sticky="w")
# pak16.var = e16

# e17 = BooleanVar()
# pak17 = Checkbutton(logs,text="Lukturu maiņa un regulēšana", variable=e17)
# pak17.grid(row=6, column=3, padx=10,sticky="w")
# pak17.var = e17

# e18 = BooleanVar()
# pak18 = Checkbutton(logs,text="Ūdens sūkņa maiņa", variable=e18)
# pak18.grid(row=7, column=3, padx=10,sticky="w")
# pak18.var = e18

# e19 = BooleanVar()
# pak19 = Checkbutton(logs,text="Ģenerātora maiņa", variable=e19)
# pak19.grid(row=8, column=3, padx=10,sticky="w")
# pak19.var = e19

# e20 = BooleanVar()
# pak20 = Checkbutton(logs,text="Turbīnas maiņa", variable=e20)
# pak20.grid(row=9, column=3, padx=10,sticky="w")
# pak20.var = e20

# e21 = BooleanVar()
# pak21 = Checkbutton(logs,text="Zobsiksnas maiņa", variable=e21)
# pak21.grid(row=10, column=3, padx=10,sticky="w")
# pak21.var = e21

# e22 = BooleanVar()
# pak22 = Checkbutton(logs,text="Akumulātora maiņa", variable=e22)
# pak22.grid(row=4, column=4, padx=10,sticky="w")
# pak22.var = e22

# e23 = BooleanVar()
# pak23 = Checkbutton(logs,text="Mehāniskās ātrumkārbas remonts un maiņa", variable=e23)
# pak23.grid(row=5, column=4, padx=10,sticky="w")
# pak23.var = e23

# e24 = BooleanVar()
# pak24 = Checkbutton(logs,text="Automātiskās ātrumkārbas remonts un maiņa", variable=e24)
# pak24.grid(row=6, column=4, padx=10,sticky="w")
# pak24.var = e24

# e25 = BooleanVar()
# pak25 = Checkbutton(logs,text="Stūres mehānisma remonts", variable=e25)
# pak25.grid(row=7, column=4, padx=10,sticky="w")
# pak25.var = e25

# e26 = BooleanVar()
# pak26 = Checkbutton(logs,text="Sprauslu remonts un maiņa", variable=e26)
# pak26.grid(row=8, column=4, padx=10,sticky="w")
# pak26.var = e26

# e27 = BooleanVar()
# pak27 = Checkbutton(logs,text="Tiltu bukšu maiņa", variable=e27)
# pak27.grid(row=9, column=4, padx=10,sticky="w")
# pak27.var = e27

# e28 = BooleanVar()
# pak28 = Checkbutton(logs,text="Radiatora maiņa", variable=e28)
# pak28.grid(row=10, column=4, padx=10,sticky="w")
# pak28.var = e28

# pak_info = {
#     pak1: [30, 15, 0.5],
#     pak2: [30, 15, 0.7],
#     pak3: [15, 20, 1],
#     pak4: [40, 20, 1],
#     pak5: [80, 40, 1.5],
#     pak6: [0, 10, 0.3],
#     pak7: [0, 350, 3],
#     pak8: [65, 30, 1],
#     pak9: [0, 20, 0.5],
#     pak10: [120, 30, 2],
#     pak11: [80, 30, 2],
#     pak12: [40, 40, 2],
#     pak13: [20, 30, 2],
#     pak14: [10, 20, 0.5],
#     pak15: [35, 20, 1.5],
#     pak16: [20, 15, 1],
#     pak17: [15, 15, 0.5],
#     pak18: [40, 20, 1.5],
#     pak19: [150, 30, 2],
#     pak20: [350, 40, 2],
#     pak21: [100, 40, 2],
#     pak22: [100, 5, 0.1],
#     pak23: [500, 150, 6],
#     pak24: [650, 200, 8],
#     pak25: [60, 60, 3],
#     pak26: [100, 60, 2],
#     pak27: [30, 100, 5],
#     pak28: [60, 30, 1.5],
# }

# def saglabat():
#     izvēlētie_pakalpojumi = []
#     kop_cena = 0
#     kop_laiks = 0

#     for checkbox, dati in pak_info.items():
#         if checkbox.var.get():
#             materiālu_cena, darba_cena, laiks = dati
#             izvēlētie_pakalpojumi.append(checkbox.cget("text"))
#             kop_cena += materiālu_cena + darba_cena
#             kop_laiks += laiks

#     kopejascenas.delete(0, tk.END)
#     kopejascenas.insert(tk.END, f"Kopējā cena: {kop_cena:.2f} EUR")
#     kopejascenas.insert(tk.END, f"Aptuvenais darba laiks: {kop_laiks:.1f} h")

#     with open("auto_servisa_dati.csv", "a", newline="", encoding="utf-8") as csvfile:
#         writer = csv.writer(csvfile)
#         writer.writerow([
#             marka.get(),
#             modelis.get(),
#             ", ".join(izvēlētie_pakalpojumi),
#             f"{kop_cena:.2f} EUR",
#             f"{kop_laiks:.1f} h"
#         ])

# ttk.Label(logs, text="Ja nepieciešams cits pakalpojums lūdzu sazinaties ar servisu!", font=("Helvetica",15,"bold")).grid(row=11, column=2, columnspan=2,pady=10, padx=1)

# kopejascenas=tk.Listbox(logs, width=40, height=5, bg="black", fg="white", font=("Helvetica", 16, "bold"))
# kopejascenas.grid(row=12, columnspan=5, pady=10, padx=1)

# Button(logs, text="Saglabāt", font=("Helvetica", 12, "bold"), command=saglabat).grid(row=13, column=1, columnspan=2, pady=10, sticky="e")
# ttk.Label(logs, text="Saziņa ar servisu: +37112345678  vwserviss@epasts.com", font=("Helvetica",15,"bold")).grid(row=14, column=2, columnspan=2,pady=1, padx=1)

# logs.mainloop()