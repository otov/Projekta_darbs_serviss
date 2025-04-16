import tkinter as tk
from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
import csv

logs = Tk()
logs.geometry("1300x800")
logs.title("Auto servisa kalkulators")

#Attēls
foto_frame = tk.Frame(logs)
foto_frame.grid(row=1, column=1, padx=5, pady=5)
foto_image = Image.open("vw logo.png")
resized_foto = foto_image.resize((100, 100))
foto = ImageTk.PhotoImage(resized_foto)
foto_label = ttk.Label(foto_frame, image=foto)
foto_label.grid(row=1, column=1, padx=10, pady=40)

# Virsraksts
ttk.Label(logs, text="Auto servisa remonta kalkulators", font=("Helvetica", 26, "bold")).grid(row=1, column=3, pady=40, padx=5)

# Auto marka/modelis
ttk.Label(logs, text="Auto marka:", font=("Helvetica", 14)).grid(row=2, column=1, pady=5, padx=5, sticky="e")
marka = ttk.Combobox(logs, state="readonly", values=["Volkswagen"])
marka.current(0)
marka.grid(row=2, column=2, pady=5, padx=5)

ttk.Label(logs, text="Auto modelis:", font=("Helvetica", 14)).grid(row=2, column=3, pady=5, padx=5, sticky="e")
modelis = ttk.Combobox(logs, state="readonly", values=["Golf 5"])
modelis.current(0)
modelis.grid(row=2, column=4, pady=5, padx=5)

# Pakalpojumu virsraksts
ttk.Label(logs, text="Izvēlieties nepieciešamos pakalpojumus:", font=("Helvetica", 12, "bold")).grid(row=3, column=1, columnspan=4, sticky="w", padx=30, pady=10)

# Katrs pakalpojums atsevišķi ar koordinātām
elp1 = BooleanVar()
pak1 = Checkbutton(logs, text="Eļļas maiņa (+ filtrs)", variable=elp1)
pak1.grid(row=4, column=1, sticky="w", padx=10)

elp2 = BooleanVar()
pak2 = Checkbutton(logs, text="Degvielas filtra maiņa", variable=elp2)
pak2.grid(row=4, column=2, sticky="w", padx=10)

elp3 = BooleanVar()
pak3 = Checkbutton(logs, text="Gaisa filtra maiņa", variable=elp3)
pak3.grid(row=4, column=3, sticky="w", padx=10)

elp4 = BooleanVar()
pak4 = Checkbutton(logs, text="Savirzes regulēšana", variable=elp4)
pak4.grid(row=4, column=4, sticky="w", padx=10)

elp5 = BooleanVar()
pak5 = Checkbutton(logs, text="Diagnostika", variable=elp5)
pak5.grid(row=5, column=1, sticky="w", padx=10)

elp6 = BooleanVar()
pak6 = Checkbutton(logs, text="Bremžu kluču maiņa (priekšā)", variable=elp6)
pak6.grid(row=5, column=2, sticky="w", padx=10)

elp7 = BooleanVar()
pak7 = Checkbutton(logs, text="Bremžu kluču maiņa (aizmugurē)", variable=elp7)
pak7.grid(row=5, column=3, sticky="w", padx=10)

elp8 = BooleanVar()
pak8 = Checkbutton(logs, text="Amortizatoru maiņa", variable=elp8)
pak8.grid(row=5, column=4, sticky="w", padx=10)

elp9 = BooleanVar()
pak9 = Checkbutton(logs, text="Ritošās daļas pārbaude", variable=elp9)
pak9.grid(row=6, column=1, sticky="w", padx=10)

elp10 = BooleanVar()
pak10 = Checkbutton(logs, text="Stūres savienojuma pārbaude", variable=elp10)
pak10.grid(row=6, column=2, sticky="w", padx=10)

elp11 = BooleanVar()
pak11 = Checkbutton(logs, text="Akumulatora maiņa", variable=elp11)
pak11.grid(row=6, column=3, sticky="w", padx=10)

elp12 = BooleanVar()
pak12 = Checkbutton(logs, text="Sveces maiņa", variable=elp12)
pak12.grid(row=6, column=4, sticky="w", padx=10)

elp13 = BooleanVar()
pak13 = Checkbutton(logs, text="Zobsiksnas maiņa", variable=elp13)
pak13.grid(row=7, column=1, sticky="w", padx=10)

elp14 = BooleanVar()
pak14 = Checkbutton(logs, text="Kondicioniera uzpilde", variable=elp14)
pak14.grid(row=7, column=2, sticky="w", padx=10)

elp15 = BooleanVar()
pak15 = Checkbutton(logs, text="Kondicioniera pārbaude", variable=elp15)
pak15.grid(row=7, column=3, sticky="w", padx=10)

elp16 = BooleanVar()
pak16 = Checkbutton(logs, text="Auto mazgāšana", variable=elp16)
pak16.grid(row=7, column=4, sticky="w", padx=10)

elp17 = BooleanVar()
pak17 = Checkbutton(logs, text="Spoileru uzstādīšana", variable=elp17)
pak17.grid(row=8, column=1, sticky="w", padx=10)

elp18 = BooleanVar()
pak18 = Checkbutton(logs, text="Riepu montāža", variable=elp18)
pak18.grid(row=8, column=2, sticky="w", padx=10)

elp19 = BooleanVar()
pak19 = Checkbutton(logs, text="ABS sistēmas pārbaude", variable=elp19)
pak19.grid(row=8, column=3, sticky="w", padx=10)

elp20 = BooleanVar()
pak20 = Checkbutton(logs, text="Eļļas līmeņa pārbaude", variable=elp20)
pak20.grid(row=8, column=4, sticky="w", padx=10)

# Cits pakalpojums
ttk.Label(logs, text="Cits pakalpojums:", font=("Helvetica", 12)).grid(row=9, column=1, sticky="w", padx=10)
cits_pakalpojums = Entry(logs, width=50)
cits_pakalpojums.grid(row=9, column=2, columnspan=3, padx=5, pady=5, sticky="w")

# Rezultātu logs
rezultats = Text(logs, height=5, width=80, bg="black", fg="white", font=("Courier", 12))
rezultats.grid(row=11, column=1, columnspan=4, pady=20, padx=5)

# Pakalpojumu dati (izmaksas un laiks)
pak_info = {
    pak1: [20, 15, 1.0],
    pak2: [10, 12, 0.5],
    pak3: [8, 10, 0.3],
    pak4: [0, 25, 1.0],
    pak5: [0, 30, 0.5],
    pak6: [35, 20, 1.5],
    pak7: [35, 20, 1.5],
    pak8: [50, 40, 2.0],
    pak9: [0, 15, 0.5],
    pak10: [0, 20, 0.7],
    pak11: [60, 10, 0.3],
    pak12: [25, 15, 0.6],
    pak13: [80, 70, 3.0],
    pak14: [30, 20, 1.0],
    pak15: [0, 15, 0.5],
    pak16: [0, 10, 0.5],
    pak17: [70, 40, 2.0],
    pak18: [10, 25, 1.0],
    pak19: [0, 20, 0.6],
    pak20: [0, 5, 0.2],
}

# Aprēķins
def aprekinat():
    rezultats.delete('1.0', END)
    detalas = 0
    darbs = 0
    laiks = 0
    pak_nosaukumi = []

    for pak, info in pak_info.items():
        if pak.cget("variable") and logs.getvar(pak.cget("variable")) == '1':
            detalas += info[0]
            darbs += info[1]
            laiks += info[2]
            pak_nosaukumi.append(pak.cget("text"))

    if cits_pakalpojums.get().strip():
        pak_nosaukumi.append(cits_pakalpojums.get().strip())

    kop = detalas + darbs

    rezultats.insert(END, f"Aptuvenās detaļu izmaksas: {detalas:.2f} EUR\n")
    rezultats.insert(END, f"Aptuvenās darba izmaksas: {darbs:.2f} EUR\n")
    rezultats.insert(END, f"Aptuvenās kopējās izmaksas: {kop:.2f} EUR\n")
    rezultats.insert(END, f"Aptuvenais darba ilgums: {laiks:.1f} h\n")

    return pak_nosaukumi, detalas, darbs, laiks

# Saglabāšana
def saglabat():
    pakalpojumi, detalas, darbs, laiks = aprekinat()
    with open("dati.csv", "a", newline='', encoding="utf-8") as fails:
        rakstitajs = csv.writer(fails)
        rakstitajs.writerow([marka.get(), modelis.get(), "; ".join(pakalpojumi), f"{detalas:.2f}", f"{darbs:.2f}", f"{laiks:.1f}"])
    rezultats.insert(END, "Dati saglabāti CSV failā.\n")

# Poga
Button(logs, text="Saglabāt", font=("Helvetica", 12, "bold"), command=saglabat, bg="lightblue").grid(row=12, column=1, columnspan=4, pady=10)

logs.mainloop()