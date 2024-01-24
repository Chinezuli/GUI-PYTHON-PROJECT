import tkinter as tk
from tkinter import messagebox


# Funcția pentru afisarea manualului într-un pop-up
#Aici poti sa pui cate manuale vrei sau sa editezi
def afiseaza_manual():
    manual_text = """
    Manual de foc

    1. Descrierea funcționalității principale...
    2. Instrucțiuni de utilizare...
    3. Detalii despre diferitele funcții și butoane...

    Pentru asistență suplimentară, contactați suportul tehnic.
    """
    messagebox.showinfo("Manual de Utilizare", manual_text)
def afiseaza_manual2():
    manual_text = """
    Manual de Utilizare

    1. Descrierea funcționalității principale...
    2. Instrucțiuni de utilizare...
    3. Detalii despre diferitele funcții și butoane...

    Pentru asistență suplimentară, contactați suportul tehnic.
    """
    messagebox.showinfo("Manual de Utilizare", manual_text)

