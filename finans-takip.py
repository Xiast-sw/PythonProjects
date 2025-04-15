import tkinter as tk
from tkinter import messagebox
import json

# Verilerin saklanacağı dosya
DATA_FILE = "finance_data.json"

# JSON verilerini yükleme
def load_data():
    try:
        with open(DATA_FILE, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return {"income": [], "expenses": []}

# JSON verilerini kaydetme
def save_data(data):
    with open(DATA_FILE, "w") as file:
        json.dump(data, file, indent=4)

# Gelir ekleme
def add_income():
    amount = entry_amount.get()
    desc = entry_desc.get()
    if amount.isdigit() and desc:
        data["income"].append({"amount": int(amount), "description": desc})
        save_data(data)
        update_summary()
        entry_amount.delete(0, tk.END)
        entry_desc.delete(0, tk.END)
        messagebox.showinfo("Başarılı", "Gelir eklendi!")
    else:
        messagebox.showerror("Hata", "Geçerli bir tutar ve açıklama girin!")

# Gider ekleme
def add_expense():
    amount = entry_amount.get()
    desc = entry_desc.get()
    if amount.isdigit() and desc:
        data["expenses"].append({"amount": int(amount), "description": desc})
        save_data(data)
        update_summary()
        entry_amount.delete(0, tk.END)
        entry_desc.delete(0, tk.END)
        messagebox.showinfo("Başarılı", "Gider eklendi!")
    else:
        messagebox.showerror("Hata", "Geçerli bir tutar ve açıklama girin!")

# Özeti güncelleme
def update_summary():
    total_income = sum(item["amount"] for item in data["income"])
    total_expenses = sum(item["amount"] for item in data["expenses"])
    net_balance = total_income - total_expenses

    label_income.config(text=f"Toplam Gelir: {total_income} TL")
    label_expenses.config(text=f"Toplam Gider: {total_expenses} TL")
    label_balance.config(text=f"Net Bakiye: {net_balance} TL")

# Arayüz oluşturma
data = load_data()
root = tk.Tk()
root.title("Finans Takip Uygulaması")

# Tutar ve açıklama giriş
tk.Label(root, text="Tutar (TL):").grid(row=0, column=0, padx=5, pady=5)
entry_amount = tk.Entry(root)
entry_amount.grid(row=0, column=1, padx=5, pady=5)

tk.Label(root, text="Açıklama:").grid(row=1, column=0, padx=5, pady=5)
entry_desc = tk.Entry(root)
entry_desc.grid(row=1, column=1, padx=5, pady=5)

# Butonlar
btn_income = tk.Button(root, text="Gelir Ekle", command=add_income)
btn_income.grid(row=2, column=0, padx=5, pady=5)

btn_expense = tk.Button(root, text="Gider Ekle", command=add_expense)
btn_expense.grid(row=2, column=1, padx=5, pady=5)

# Özet bilgileri
label_income = tk.Label(root, text="Toplam Gelir: 0 TL", fg="green")
label_income.grid(row=3, column=0, columnspan=2, padx=5, pady=5)

label_expenses = tk.Label(root, text="Toplam Gider: 0 TL", fg="red")
label_expenses.grid(row=4, column=0, columnspan=2, padx=5, pady=5)

label_balance = tk.Label(root, text="Net Bakiye: 0 TL", fg="blue")
label_balance.grid(row=5, column=0, columnspan=2, padx=5, pady=5)

# Uygulamayı başlatma
update_summary()
root.mainloop()
