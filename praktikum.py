import tkinter as tk
from tkinter import messagebox

def hasil_prediksi():
    try:
        for entry in nilai_entries:
            nilai = int(entry.get())
            if not (0 <= nilai <= 100):
                raise ValueError("Nilai harus antara 0 dan 100.")
        hasil_label.config(text="Prodi Pilihan: Teknologi Informasi")
    except ValueError as e:
        messagebox.showerror("Input Error", "Pastikan semua input adalah angka antara 0 dan 100")

root = tk.Tk()
root.title("Aplikasi Prediksi Prodi Pilihan")
root.geometry("500x600")
root.configure(bg="#C0C0C0")

judul_label = tk.Label(root, text="Aplikasi Prediksi Prodi Pilihan", font=("Arial", 16, "bold"))
judul_label.pack(pady=20)

frame_nilai = tk.Frame(root)
frame_nilai.pack(pady=10)

nilai_entries = []
for i in range(10):
    label = tk.Label(frame_nilai, text=f"Nilai Mata Pelajaran {i + 1}:")
    label.grid(row=i, column=0, padx=5, pady=5, sticky="w")
    entry = tk.Entry(frame_nilai)
    entry.grid(row=i, column=1, padx=5, pady=5)
    nilai_entries.append(entry)

prediksi_button = tk.Button(root, text="Hasil Prediksi", command=hasil_prediksi)
prediksi_button.pack(pady=20)

hasil_label = tk.Label(root, text="Prodi Pilihan: ", font=("Arial", 12))
hasil_label.pack(pady=10)

root.mainloop()
