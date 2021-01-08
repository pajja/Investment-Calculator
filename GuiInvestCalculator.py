import math
from tkinter import *
import tkinter as tk
from tkinter import messagebox

def calculator(first, addition, year, proc):
    i = 0
    months = 12
    while (i < (months * year)):
        ats = first * (proc * 0.01 + 1)
        first = ats
        first += addition
        i += 1
    final = round(float(ats), 2)
    return final

def contribution(first, addition, year):
    i = 0
    months = 12
    while (i < (months * year)):
        ats = first
        first = ats + addition
        i += 1
    final = round(float(ats), 2)
    return final

root = tk.Tk(className="Investment Calculator")
root.configure(bg="#F5DEB3")

tk.Label(root, text="Starting amount", bg="#F5DEB3").grid(column=0, row=0)
tk.Label(root, text="Additional amount per month", bg="#F5DEB3").grid(column=0, row=1)
tk.Label(root, text="Duration in years", bg="#F5DEB3").grid(column=0, row=2)
tk.Label(root, text="Growth per month in proc", bg="#F5DEB3").grid(column=0, row=3)

first_str = tk.StringVar()
addition_str = tk.StringVar()
year_str = tk.StringVar()
proc_str = tk.StringVar()

def answer():
    first = first_str.get()
    try:
        first = float(first)
    except:
        messagebox.showerror("Error", "Check for error in your input.")
        return 1
    addition = addition_str.get()
    try:
        addition = float(addition)
    except:
        messagebox.showerror("Error", "Check for error in your input.")
        return 1
    year = year_str.get()
    try:
        year = float(year)
    except:
        messagebox.showerror("Error", "Check for error in your input.")
        return 1
    proc = proc_str.get()
    try:
        proc = float(proc)
    except:
        messagebox.showerror("Error", "Check for error in your input.")
        return 1


    answ = calculator(float(first), float(addition), float(year), float(proc))
    answ_com = f"{answ:,}"
    tk.Label(root, text=answ_com, width=16, bg="#FFA500").grid(column=1, row=9)
    tk.Label(root, text="Result: ", width=22, bg="#FFA500").grid(column=0, row=9)
    
    contr = contribution(float(first), float(addition), float(year))
    contr_com = f"{contr:,}"
    tk.Label(root, text=contr_com, width=16, bg="#F5DEB3").grid(column=1, row=10)
    tk.Label(root, text="Contribution: ", width=22, bg="#F5DEB3").grid(column=0, row=10)

    intr = float(answ) - float(contr)
    intr = round(float(intr), 2)
    intr_com = f"{intr:,}"
    tk.Label(root, text=intr_com, width=16, bg="#F5DEB3").grid(column=1, row=11)
    tk.Label(root, text="Interest: ", width=22, bg="#F5DEB3").grid(column=0, row=11)

    tk.Label(root, text="Starting amount:", bg="#F5DEB3").grid(column=0, row=5)
    tk.Label(root, text="Additional amount per month:", bg="#F5DEB3").grid(column=0, row=6)
    tk.Label(root, text="Duration in years:", bg="#F5DEB3").grid(column=0, row=7)
    tk.Label(root, text="Growth per month in proc:", bg="#F5DEB3").grid(column=0, row=8)

    tk.Label(root, text=f"{float(first):,}", bg="#F5DEB3").grid(column=1, row=5)
    tk.Label(root, text=f"{float(addition):,}", bg="#F5DEB3").grid(column=1, row=6)
    tk.Label(root, text=f"{float(year):,}", bg="#F5DEB3").grid(column=1, row=7)
    tk.Label(root, text=f"{float(proc):,}", bg="#F5DEB3").grid(column=1, row=8)

    first_str.set("")
    addition_str.set("")
    year_str.set("")
    proc_str.set("")

tk.Entry(root, textvariable=first_str).grid(column=1, row=0)
tk.Entry(root, textvariable=addition_str).grid(column=1, row=1)
tk.Entry(root, textvariable=year_str).grid(column=1, row=2)
tk.Entry(root, textvariable=proc_str).grid(column=1, row=3)

tk.Button(root, text="Calculate", bg="#FFC594", width="16",
          command=answer).grid(column=1, row=4)

root.mainloop()
