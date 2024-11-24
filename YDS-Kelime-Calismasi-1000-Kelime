import tkinter as tk
import csv
import random

# Kelimeleri CSV dosyasından okuma fonksiyonu
def kelimeleri_yukle():
    kelimeler = []
    with open('yds_kelimeler.csv', mode='r', encoding='utf-8') as file:
        reader = csv.reader(file)
        next(reader)  # Başlık satırını atla
        for row in reader:
            kelimeler.append(row)
    return kelimeler

# Yeni kelime sorusu
def yeni_soru():
    global kelimeler
    kelime = random.choice(kelimeler)
    kelime_text.set(kelime[0])
    global dogru_cevap
    dogru_cevap = kelime[1]

# Cevap kontrolü
def cevapla():
    kullanici_cevap = cevap_entry.get()
    if kullanici_cevap.lower() == dogru_cevap.lower():
        sonuc_label.config(text="Doğru!", fg="green")
    else:
        sonuc_label.config(text=f"Yanlış! Doğru cevap: {dogru_cevap}", fg="red")
    cevap_entry.delete(0, tk.END)  # Cevap alanını temizle
    yeni_soru()  # Yeni soru sormak için çağır

# Tkinter arayüzü
root = tk.Tk()
root.title("YDS Kelime Oyunu")
root.geometry("400x300")

# Başlangıçta kelimeleri yükle
kelimeler = kelimeleri_yukle()

# Değişkenler
kelime_text = tk.StringVar()
dogru_cevap = ""

# Soru gösterimi
kelime_label = tk.Label(root, text="Kelime:", font=("Arial", 16))
kelime_label.pack(pady=20)

kelime_display = tk.Label(root, textvariable=kelime_text, font=("Arial", 24, "bold"))
kelime_display.pack(pady=20)

# Kullanıcı cevabı
cevap_entry = tk.Entry(root, font=("Arial", 14))
cevap_entry.pack(pady=10)

# Cevap butonu
cevap_button = tk.Button(root, text="Cevapla", font=("Arial", 14), command=cevapla)
cevap_button.pack(pady=10)

# Sonuç etiketini ekle
sonuc_label = tk.Label(root, text="", font=("Arial", 14))
sonuc_label.pack(pady=10)

# İlk soru
yeni_soru()

# Uygulamayı başlat
root.mainloop()
