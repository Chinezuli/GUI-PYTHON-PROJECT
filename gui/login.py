import customtkinter as ctk
import tkinter.messagebox as tkmb



ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("dark-blue")

app = ctk.CTk()


def center_window(window, width, height):
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()

    x = (screen_width // 2) - (width // 2)
    y = (screen_height // 2) - (height // 2)

    window.geometry(f'{width}x{height}+{x}+{y}')

window_width = 400
window_height = 300
center_window(app, window_width, window_height)
app.title("ScriptCoders")
def login(user_entry, user_pass):
    user = "Test"
    parola = "12345"
    if user_entry.get() == user and user_pass.get() == parola:
        tkmb.showinfo(title="Login Successful", message="Te-ai logat!")
        app.destroy()
    elif user_entry.get() == user and user_pass.get() != parola:
        tkmb.showwarning(title='Wrong password', message='Verifica parola')
    elif user_entry.get() != user and user_pass.get() == parola:
        tkmb.showwarning(title='Wrong username', message='Verifica username-ul')
    else:
        tkmb.showerror(title="Login Failed", message="Nici parola si nici username-ul nu sunt valide")

frame = ctk.CTkFrame(master=app)
frame.pack(pady=20, padx=40, fill='both', expand=True)

label = ctk.CTkLabel(master=frame, text='Logheaza-te te rog')
label.pack(pady=12, padx=10)

user_entry = ctk.CTkEntry(master=frame, placeholder_text="User")
user_entry.pack(pady=12, padx=10)

user_pass = ctk.CTkEntry(master=frame, placeholder_text="Parola", show="*")
user_pass.pack(pady=12, padx=10)

button = ctk.CTkButton(master=frame, text='Logheazate', command=lambda: login(user_entry, user_pass))
button.pack(pady=12, padx=10)

checkbox = ctk.CTkCheckBox(master=frame, text='Tine-ma minte')
checkbox.pack(pady=12, padx=10)

app.mainloop()
