import tkinter as tk
from tkinter import messagebox
from tkcalendar import DateEntry
from datetime import datetime

def hesapla():
    try:
        tarih1 = calendar_tarih1.get_date()
        tarih2 = calendar_tarih2.get_date()

        format_tarih = "%Y-%m-%d"
        tarih1 = datetime.strptime(str(tarih1), format_tarih)
        tarih2 = datetime.strptime(str(tarih2), format_tarih)

        fark = abs((tarih2 - tarih1).days)

        label_sonuc.config(text=f"Gün Sayısı: {fark} gün")

    except ValueError:
        messagebox.showerror("Hata", "Tarih formatı hatalı. Lütfen geçerli bir tarih seçin.")

root = tk.Tk()
root.title("Tarih Farkı Hesaplama")
root.geometry("500x350")  
root.config(bg="#f0f0f0")  

label_baslik = tk.Label(root, text="İki Tarih Arasındaki Gün Sayısını Hesapla", 
                        font=("Helvetica", 16, "bold"), bg="#f0f0f0", fg="#333")
label_baslik.pack(pady=20)

label_tarih1 = tk.Label(root, text="Tarih 1:", font=("Helvetica", 12), bg="#f0f0f0", fg="#333")
label_tarih1.pack(pady=5)
calendar_tarih1 = DateEntry(root, date_pattern='yyyy-mm-dd', font=("Helvetica", 12), width=20)
calendar_tarih1.pack(pady=5)

label_tarih2 = tk.Label(root, text="Tarih 2:", font=("Helvetica", 12), bg="#f0f0f0", fg="#333")
label_tarih2.pack(pady=5)
calendar_tarih2 = DateEntry(root, date_pattern='yyyy-mm-dd', font=("Helvetica", 12), width=20)
calendar_tarih2.pack(pady=5)

buton_hesapla = tk.Button(root, text="Hesapla", command=hesapla, font=("Helvetica", 12), bg="#4CAF50", fg="white", width=20)
buton_hesapla.pack(pady=20)

label_sonuc = tk.Label(root, text="Gün Sayısı: ", font=("Helvetica", 14), bg="#f0f0f0", fg="#333")
label_sonuc.pack(pady=10)

root.mainloop()
