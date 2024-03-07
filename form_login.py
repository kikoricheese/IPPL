import tkinter as tk
from tkinter import messagebox

def validate_credentials(username, password):
    # Validasi kredensial disini
    # Misal, menggunakan basis data atau API
    if username == "admin" and password == "123":
        return True
    return False

def login():
    username = user_var.get()
    password = password_var.get()

    if validate_credentials(username, password):
        # Login berhasil
        messagebox.showinfo("Success", "Login successful.")
    else:
        # Menampilkan pesan kesalahan jika validasi kredensial gagal
        messagebox.showerror("Error", "User not found.")

root = tk.Tk()

user_var = tk.StringVar()
password_var = tk.StringVar()

tk.Label(root, text="Username:").pack()
tk.Entry(root, textvariable=user_var).pack()

tk.Label(root, text="Password:").pack()
tk.Entry(root, textvariable=password_var, show="*").pack()

tk.Button(root, text="Login", command=login).pack()

root.mainloop()