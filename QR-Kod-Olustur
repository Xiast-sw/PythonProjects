import qrcode
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox, filedialog

def generate_qr():
    url = url_entry.get()
    if not url.strip():
        messagebox.showerror("Hata", "Lütfen bir URL giriniz!")
        return

    try:
        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_H,
            box_size=10,
            border=4,
        )
        qr.add_data(url)
        qr.make(fit=True)
        
        img = qr.make_image(fill_color="black", back_color="white")
        
        file_path = filedialog.asksaveasfilename(
            defaultextension=".png",
            filetypes=[("PNG Files", "*.png"), ("All Files", "*.*")]
        )
        
        if file_path:
            img.save(file_path)
            messagebox.showinfo("Başarılı", f"QR kod başarıyla kaydedildi: {file_path}")
    except Exception as e:
        messagebox.showerror("Hata", f"QR kod oluşturulurken bir hata oluştu: {e}")

# tkinter GUI
root = tk.Tk()
root.title("QR Kod Oluşturucu")
root.geometry("360x200")
root.resizable(False, False)

# Tema Seçimi
style = ttk.Style()
style.theme_use('clam')

# Başlık
title_label = ttk.Label(root, text="QR Kod Oluşturucu", font=("Arial", 16, "bold"))
title_label.pack(pady=10)

# URL Girişi
frame = ttk.Frame(root, padding=(10, 10, 10, 10))
frame.pack(fill="both", expand=True)

url_label = ttk.Label(frame, text="URL:")
url_label.grid(row=0, column=0, padx=5, pady=5, sticky="w")

url_entry = ttk.Entry(frame, width=40)
url_entry.grid(row=0, column=1, padx=5, pady=5)

# QR Kod Oluştur Butonu
generate_button = ttk.Button(frame, text="QR Kod Oluştur", command=generate_qr)
generate_button.grid(row=1, column=0, columnspan=2, pady=10)

# Uygulama Çalıştırma
root.mainloop()
