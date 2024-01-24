# importam librariile
import tkinter as tk
from tkinter import ttk
import customtkinter as ctk
import pygame
from pygame.locals import *
import ttkbootstrap
from login import user_entry, user_pass, login
from PIL import Image, ImageTk
from ttkthemes import ThemedTk
import time
from playlist import slides
from tkinter import messagebox
import threading
from test import afiseaza_manual, afiseaza_manual2
import random
from tkinter import Label



# Ideei :
    # Vreau sa fac cumva un compass functional, un manual, un calculator modern si emergency call
# Variabile globale 
titlu = "SurvivalLife" # Iti schimbi titlul aplicatiei
logo = Image.open("poza1.png") # Iti schimbi logo aplicatiei

ctk.set_appearance_mode("System")
ctk.set_default_color_theme("blue")
#definirea clock-ului
class Clock(tk.Label):
    def __init__(self, parent):
        super().__init__(parent, font=('calibri', 12, 'bold'), background="#242424", foreground='white')
        self.update_time()

    def update_time(self):
        current_time = time.strftime('%H:%M:%S')
        self.config(text=current_time)
        self.after(1000, self.update_time)

#definirea aplicatiei
class App2(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("ScriptCoders")
        self.geometry(f"{1100}x{580}")

        self.grid_columnconfigure(1, weight=1)
        self.grid_columnconfigure((2, 3), weight=0)
        self.grid_rowconfigure((0, 1, 2), weight=1)

        self.sidebar_frame = ctk.CTkFrame(self, width=140, corner_radius=0)
        self.sidebar_frame.grid(row=0, column=0, rowspan=2, sticky="nsew")
        self.sidebar_frame.grid_rowconfigure(5, weight=1)

        # Logo label cu imagine
        self.logo_label = ctk.CTkLabel(self.sidebar_frame, text=titlu, font=ctk.CTkFont(size=20, weight="bold")) #TODO move title name to global variable = rezolvat
        self.logo_label.grid(row=0, column=0, padx=0, pady=(20, 10))
        
        image =  logo #TODO move picture name to global variable = rezolvat
        image = image.resize((35, 35))
        photo = ImageTk.PhotoImage(image)
        
        # Eticheta imaginii
        image_label = ctk.CTkLabel(self.sidebar_frame, image=photo, text="")
        image_label.image = photo  
        image_label.grid(row=0, column=0, padx=0, sticky='w')
        clock = Clock(self)
        clock.grid(row=0, column=1, sticky='ne')

        self.sidebar_button_1 = ctk.CTkButton(self.sidebar_frame, text="Animale salbatice")
        self.sidebar_button_1.grid(row=1, column=0, padx=20, pady=10)
        self.sidebar_button_1.bind("<Button-1>", self.optiunea1)
        self.sidebar_button_2 = ctk.CTkButton(self.sidebar_frame, text="Compass")
        self.sidebar_button_2.grid(row=2, column=0, padx=20, pady=10)
        self.sidebar_button_2.bind("<Button-1>", self.optiunea2)
        self.sidebar_button_3 = ctk.CTkButton(self.sidebar_frame, text="Manual de supravetuire")
        self.sidebar_button_3.grid(row=3, column=0, padx=20, pady=10)
        self.sidebar_button_3.bind("<Button-1>", self.optiunea3)
        self.sidebar_button_4 = ctk.CTkButton(self.sidebar_frame, text="Urgente")
        self.sidebar_button_4.grid(row=4, column=0, padx=20, pady=10)
        self.sidebar_button_4.bind("<Button-1>", self.optiuni)

        self.center_window(400, 300)

    def optiunea1(self, event):

        pygame.init()

        width, height = 700, 400
        screen = pygame.display.set_mode((width, height))
        pygame.display.set_caption('Animale salbatice')

        slides = [
            {'image_path': 'ceva.jpg', 'text': "Ursul Brun"},
            {'image_path': 'oaie.jpg', 'text': "Vulpea"},
            {'image_path': 'OIG.jpg', 'text': "Lupul"}
        ]
        current_slide = 0

        def load_image(image_path):
            image = pygame.image.load(image_path).convert()
            return pygame.transform.scale(image, (width, height))

        def show_current_slide():
            screen.blit(slides[current_slide]['image'], (0, 0))
            font = pygame.font.SysFont(None, 24)
            text = font.render(slides[current_slide]['text'], True, (255, 255, 255))
            screen.blit(text, (20, height - 50))

        slides[current_slide]['image'] = load_image(slides[current_slide]['image_path'])

        running = True
        while running:
            for event in pygame.event.get():
                if event.type == QUIT:
                    running = False
                if event.type == KEYDOWN:
                    if event.key == K_RIGHT:
                        current_slide = (current_slide + 1) % len(slides)
                        slides[current_slide]['image'] = load_image(slides[current_slide]['image_path'])
                    elif event.key == K_LEFT:
                        current_slide = (current_slide - 1) % len(slides)
                        slides[current_slide]['image'] = load_image(slides[current_slide]['image_path'])

            screen.fill((0, 0, 0))
            show_current_slide()

            # Desenare buton "Next"
            next_button = pygame.draw.rect(screen, (50, 50, 255), (600, 350, 80, 30))
            font = pygame.font.SysFont(None, 24)
            text = font.render('Next', True, (255, 255, 255))
            screen.blit(text, (615, 355))

            # Desenare buton "Previous"
            prev_button = pygame.draw.rect(screen, (50, 50, 255), (20, 350, 100, 30))
            font = pygame.font.SysFont(None, 24)
            text = font.render('Previous', True, (255, 255, 255))
            screen.blit(text, (30, 355))

            # Verificare evenimente pentru butoane
            mouse_pos = pygame.mouse.get_pos()
            if event.type == MOUSEBUTTONDOWN:
                if next_button.collidepoint(mouse_pos):
                    current_slide = (current_slide + 1) % len(slides)
                    slides[current_slide]['image'] = load_image(slides[current_slide]['image_path'])
                elif prev_button.collidepoint(mouse_pos):
                    current_slide = (current_slide - 1) % len(slides)
                    slides[current_slide]['image'] = load_image(slides[current_slide]['image_path'])

            pygame.display.flip()
    pygame.quit()

    def optiunea2(self, event):
        new_window = ThemedTk(theme="equilux")  
        new_window.title("Compass")
        new_window.geometry("700x400")

        # Adăugăm o etichetă pentru a afișa direcția busolei
        label_compass = Label(new_window, text="Compass Heading:")
        label_compass.pack()

        def get_compass_heading():
            # În acest exemplu, generăm o direcție aleatoare (simulare)
            return random.uniform(0, 360)

        def update_compass_label():
            # Obținem direcția busolei și actualizăm eticheta
            heading = get_compass_heading()
            label_compass.config(text=f"Compass Heading: {heading:.2f} degrees")

            # Programăm actualizarea la fiecare 1000 de milisecunde (1 secundă)
            new_window.after(1000, update_compass_label)

        # Inițializăm funcția de actualizare a etichetei
        update_compass_label()

        # Pornim bucla principala
        new_window.mainloop()


    def optiunea3(self, event):
        new_window = ThemedTk(theme="equilux")  
        new_window.title("Manual de instructiuni")
        new_window.geometry("700x400")
        def click_buton1():
            afiseaza_manual()
        def click_buton():
            afiseaza_manual2()
        buton_manual = tk.Button(new_window, text="Deschide Manual", command=click_buton1)
        buton_manual.pack(padx=20, pady=10)
        button_ceva = tk.Button(new_window, text="Ceva", command=click_buton)
        button_ceva.pack(padx=22, pady=11)
        new_window.mainloop()

    def optiuni(self, event):
        # Funcție pentru opțiunile din fereastră
        def make_call():
            # Funcție pentru efectuarea efectivă a apelului
            print("Apelul pentru ajutor a fost efectuat!")

        def confirm_call():
            answer = messagebox.askokcancel("Confirmare apel", "Ești sigur că vrei să faci apel pentru ajutor?")
            if answer:
                # Așteaptă 10 secunde și efectuează apelul
                print("Așteaptă 10 secunde până la efectuarea apelului...")
                thread = threading.Thread(target=call_after_10s, args=(make_call,))
                thread.start()

        def call_after_10s(func):
            # Așteaptă 10 secunde și apoi efectuează apelul
            new_window.after(10000, func)

        new_window = tk.Toplevel(self)
        new_window.title("Urgente")
        new_window.geometry("700x400")

        # Crearea butonului "Call Help" în noua fereastră
        call_button = tk.Button(new_window, text="Call Help", command=confirm_call, bg="red", fg="white")
        call_button.pack(padx=20, pady=40)

        new_window.mainloop()
    def center_window(self, width, height):
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()
        x = (screen_width // 2) - (width // 2)
        y = (screen_height // 2) - (height // 2)
        self.geometry(f"{width}x{height}+{x}+{y}")

    def check_authentication(self):
        try:
            if user_entry.get() == "ceva":
                authenticated = login(user_entry, user_pass)
                return authenticated
        except NameError:
            print("Variabilele user_entry și user_pass nu sunt definite sau nu au fost importate corect.")

if __name__ == "__main__":
    app2 = App2()
    app2.mainloop()
