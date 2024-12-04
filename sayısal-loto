import tkinter as tk
import random

# Rastgele loto sonuçlarını oluşturma
def generate_lottery():
    return sorted(random.sample(range(1, 50), 6))

# Kullanıcının tahminlerini kontrol etme
def check_results():
    user_input = entry.get()
    try:
        # Kullanıcı girişini kontrol et
        user_numbers = sorted(map(int, user_input.split(',')))

        if len(user_numbers) != 6 or any(n < 1 or n > 49 for n in user_numbers) or len(set(user_numbers)) != 6:
            raise ValueError

        # Loto sonuçlarını üret
        lottery_numbers = generate_lottery()

        # Doğru tahminleri bul
        matching_numbers = set(user_numbers).intersection(lottery_numbers)

        # Sonucu alt kısma yazdır
        result_label.config(
            text=f"Loto Sonuçları: {', '.join(map(str, lottery_numbers))}\n"
                 f"Sizin Tahminleriniz: {', '.join(map(str, user_numbers))}\n"
                 f"Doğru Tahmin: {len(matching_numbers)} "
                 f"({', '.join(map(str, matching_numbers)) if matching_numbers else 'Yok'})",
            fg="green"
        )

    except ValueError:
        result_label.config(
            text="Hatalı giriş! Lütfen 1-49 arası 6 farklı sayı girin. (Örnek: 5,12,23,34,45,49)",
            fg="red"
        )

# Tkinter arayüzü oluşturma
root = tk.Tk()
root.title("Sayısal Loto Uygulaması")
root.geometry("500x400")
root.resizable(False, False)

# Başlık
title_label = tk.Label(root, text="Sayısal Loto Tahmin Uygulaması", font=("Helvetica", 16, "bold"))
title_label.pack(pady=10)

# Açıklama
instructions_label = tk.Label(root, text="1-49 arası 6 farklı sayı girin (virgülle ayırarak):", font=("Helvetica", 12))
instructions_label.pack(pady=5)

# Kullanıcı girişi
entry = tk.Entry(root, font=("Helvetica", 14), justify="center", width=25)
entry.pack(pady=10)

# Kontrol butonu
check_button = tk.Button(root, text="Sonuçları Kontrol Et", font=("Helvetica", 12), command=check_results)
check_button.pack(pady=10)

# Sonuç alanı
result_label = tk.Label(root, text="", font=("Helvetica", 12), justify="center")
result_label.pack(pady=20)

# Çıkış butonu
exit_button = tk.Button(root, text="Çıkış", font=("Helvetica", 12), command=root.quit)
exit_button.pack(pady=10)

# Uygulamayı çalıştırma
root.mainloop()
