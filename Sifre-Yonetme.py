import tkinter as tk
from tkinter import messagebox, ttk
from cryptography.fernet import Fernet
import os
import json

# Anahtar ve şifreleme işlemleri
def load_key():
    if not os.path.exists("key.key"):
        key = Fernet.generate_key()
        with open("key.key", "wb") as key_file:
            key_file.write(key)
    else:
        with open("key.key", "rb") as key_file:
            key = key_file.read()
    return key

KEY = load_key()
cipher = Fernet(KEY)

def load_master_password():
    if os.path.exists("master_password.key"):
        with open("master_password.key", "rb") as file:
            encrypted_password = file.read()
        return cipher.decrypt(encrypted_password).decode()
    return None

def save_master_password(password):
    encrypted_password = cipher.encrypt(password.encode())
    with open("master_password.key", "wb") as file:
        file.write(encrypted_password)

MASTER_PASSWORD = load_master_password()

# İlk giriş ekranı
def login_screen():
    def set_master_password():
        new_password = new_password_entry.get()
        confirm_password = confirm_password_entry.get()
        if new_password and new_password == confirm_password:
            save_master_password(new_password)
            messagebox.showinfo("Başarılı", "Ana parola başarıyla kaydedildi!")
            root.destroy()
            main_screen()
        else:
            messagebox.showerror("Hata", "Parolalar uyuşmuyor veya boş bırakılamaz!")
    
    def check_password():
        if password_entry.get() == MASTER_PASSWORD:
            messagebox.showinfo("Başarılı", "Giriş yapıldı!")
            root.destroy()
            main_screen()
        else:
            messagebox.showerror("Hata", "Yanlış parola!")

    root = tk.Tk()
    root.title("Şifre Yöneticisi - Giriş")
    root.geometry("350x300")

    if MASTER_PASSWORD is None:
        tk.Label(root, text="Yeni Ana Parola Belirle").pack(pady=5)
        new_password_entry = tk.Entry(root, show="*", width=20)
        new_password_entry.pack(pady=5)
        tk.Label(root, text="Parolayı Onayla").pack(pady=5)
        confirm_password_entry = tk.Entry(root, show="*", width=20)
        confirm_password_entry.pack(pady=5)
        tk.Button(root, text="Kaydet", command=set_master_password).pack(pady=10)
    else:
        tk.Label(root, text="Ana Parola:").pack(pady=5)
        password_entry = tk.Entry(root, show="*", width=20)
        password_entry.pack(pady=5)
        tk.Button(root, text="Giriş", command=check_password).pack(pady=10)

    root.mainloop()

# Ana ekran
def main_screen():
    def add_password():
        site = site_entry.get()
        username = username_entry.get()
        password = password_entry.get()
        if site and username and password:
            encrypted_password = cipher.encrypt(password.encode()).decode()
            data[site] = {"username": username, "password": encrypted_password}
            save_data()
            refresh_table()
            messagebox.showinfo("Başarılı", "Şifre eklendi!")
            site_entry.delete(0, tk.END)
            username_entry.delete(0, tk.END)
            password_entry.delete(0, tk.END)
        else:
            messagebox.showerror("Hata", "Tüm alanları doldurun!")

    def save_data():
        with open("passwords.json", "w") as file:
            json.dump(data, file, indent=4)

    def load_data():
        if os.path.exists("passwords.json"):
            with open("passwords.json", "r") as file:
                return json.load(file)
        return {}

    def refresh_table():
        for row in tree.get_children():
            tree.delete(row)
        for site, info in data.items():
            decrypted_password = cipher.decrypt(info["password"].encode()).decode()
            tree.insert("", "end", values=(site, info["username"], decrypted_password))

    def on_item_select(event):
        selected_item = tree.focus()
        if not selected_item:
            return
        item = tree.item(selected_item)["values"]
        selected_site.set(item[0])
        selected_username.set(item[1])
        selected_password.set(item[2])

    def delete_selected():
        site = selected_site.get()
        if site in data:
            del data[site]
            save_data()
            refresh_table()
            messagebox.showinfo("Başarılı", "Seçili şifre silindi!")
        else:
            messagebox.showerror("Hata", "Seçili şifre bulunamadı!")

    def update_selected():
        site = selected_site.get()
        if site in data:
            new_username = selected_username.get()
            new_password = selected_password.get()
            if new_username and new_password:
                encrypted_password = cipher.encrypt(new_password.encode()).decode()
                data[site] = {"username": new_username, "password": encrypted_password}
                save_data()
                refresh_table()
                messagebox.showinfo("Başarılı", "Şifre güncellendi!")
            else:
                messagebox.showerror("Hata", "Kullanıcı adı veya şifre boş bırakılamaz!")
        else:
            messagebox.showerror("Hata", "Seçili şifre bulunamadı!")

    def logout():
        app.destroy()
        login_screen()

    data = load_data()

    app = tk.Tk()
    app.title("Şifre Yöneticisi")
    app.geometry("650x600")

    selected_site = tk.StringVar()
    selected_username = tk.StringVar()
    selected_password = tk.StringVar()

    # Giriş alanları
    tk.Label(app, text="Site Adı:").grid(row=0, column=0, pady=5, padx=5)
    site_entry = tk.Entry(app, width=30)
    site_entry.grid(row=0, column=1, pady=5, padx=5)

    tk.Label(app, text="Kullanıcı Adı:").grid(row=1, column=0, pady=5, padx=5)
    username_entry = tk.Entry(app, width=30)
    username_entry.grid(row=1, column=1, pady=5, padx=5)

    tk.Label(app, text="Şifre:").grid(row=2, column=0, pady=5, padx=5)
    password_entry = tk.Entry(app, width=30)
    password_entry.grid(row=2, column=1, pady=5, padx=5)

    tk.Button(app, text="Şifre Ekle", command=add_password).grid(row=3, column=1, pady=10)

    # Tablo
    tree = ttk.Treeview(app, columns=("Site", "Kullanıcı Adı", "Şifre"), show="headings", height=10)
    tree.heading("Site", text="Site")
    tree.heading("Kullanıcı Adı", text="Kullanıcı Adı")
    tree.heading("Şifre", text="Şifre")
    tree.grid(row=4, column=0, columnspan=2, pady=20, padx=20)
    tree.bind("<<TreeviewSelect>>", on_item_select)

    # Seçili veriyi güncelle/sil alanları
    tk.Label(app, text="Seçili Kullanıcı Adı:").grid(row=5, column=0, pady=5, padx=5)
    tk.Entry(app, textvariable=selected_username, width=30).grid(row=5, column=1, pady=5, padx=5)

    tk.Label(app, text="Seçili Şifre:").grid(row=6, column=0, pady=5, padx=5)
    tk.Entry(app, textvariable=selected_password, width=30).grid(row=6, column=1, pady=5, padx=5)

    tk.Button(app, text="Güncelle", command=update_selected).grid(row=7, column=0, pady=10)
    tk.Button(app, text="Sil", command=delete_selected).grid(row=7, column=1, pady=10)

    tk.Button(app, text="Çıkış", command=logout).grid(row=8, column=0, columnspan=2, pady=10)

    refresh_table()
    app.mainloop()

# Uygulamayı başlat
login_screen()
