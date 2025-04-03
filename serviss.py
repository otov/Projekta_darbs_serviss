import tkinter as tk
from tkinter import*
from tkinter import ttk
from PIL import Image, ImageTk

logs = Tk()
logs.geometry("1300x700")
logs.title("Auto servisa kalkulators")


foto_frame=tk.Frame(logs)
foto_frame.grid(row=1,column=1,padx=5,pady=5)
foto_image=Image.open("vw logo.png")
resized_foto=foto_image.resize((100,100))
foto = ImageTk.PhotoImage(resized_foto)
foto_label=ttk.Label(foto_frame,image=foto)
foto_label.grid(row=1,column=1,padx=10,pady=40)

ttk.Label(logs,text="Auto servisa remonta kalkulators", font=("Helvetica",30,"bold")).grid(row=1,column=3,pady=40,padx=5)
ttk.Label(logs,text="Auto marka:", font=("Helvetica",14,"bold")).grid(row=2,column=1,pady=5,padx=5)
ttk.Label(logs,text="Auto modelis:", font=("Helvetica",14,"bold")).grid(row=2,column=3,pady=5,padx=5)

marka=ttk.Combobox(logs)
marka.grid(row=2,column=2,pady=5,padx=5)
marka["values"] = ("Volkswagen")
marka = ttk.Combobox(state="readonly")


model = ttk.Combobox(logs)
model.grid(row=2, column=4,pady=5,padx=5)
model["values"] = ("Golf 5","")
logs.mainloop()