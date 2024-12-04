import tkinter as tk
from tkinter import ttk
import random
import matplotlib.pyplot as plt

# Rastgele sayılar üret ve istatistikleri hesapla
def generate_random_numbers():
    counts = {i: 0 for i in range(1, 11)}  # 1-10 arasındaki sayılar için sayaç
    
    for _ in range(1000):
        number = random.randint(1, 10)
        counts[number] += 1
    
    return counts

# Tabloyu doldur
def display_table(data):
    for i, (number, count) in enumerate(data.items(), start=1):
        table.insert("", "end", values=(number, count))

# Grafik oluştur
def plot_graph(data):
    numbers = list(data.keys())
    frequencies = list(data.values())
    
    plt.bar(numbers, frequencies, color="skyblue")
    plt.title("1-10 Arasında Sayıların Frekansları")
    plt.xlabel("Sayı")
    plt.ylabel("Frekans")
    plt.xticks(numbers)
    plt.grid(axis="y", linestyle="--", alpha=0.7)
    plt.show()

# Rastgele sayıları işle ve arayüzü güncelle
def analyze_data():
    data = generate_random_numbers()
    display_table(data)
    plot_graph(data)

# Tkinter arayüzü
root = tk.Tk()
root.title("Rastgele Sayı Analizi")
root.geometry("400x400")
root.resizable(False, False)

# Başlık
title_label = tk.Label(root, text="1-10 Arası Rastgele Sayı Analizi", font=("Helvetica", 14, "bold"))
title_label.pack(pady=10)

# Tablo oluştur
table = ttk.Treeview(root, columns=("Sayı", "Frekans"), show="headings", height=10)
table.heading("Sayı", text="Sayı")
table.heading("Frekans", text="Frekans")
table.column("Sayı", anchor="center", width=100)
table.column("Frekans", anchor="center", width=100)
table.pack(pady=10)

# Analiz butonu
analyze_button = tk.Button(root, text="Analiz Et ve Grafik Çiz", command=analyze_data, font=("Helvetica", 12))
analyze_button.pack(pady=20)

# Uygulamayı çalıştır
root.mainloop()
