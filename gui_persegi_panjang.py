import tkinter as tk
from tkinter import messagebox

def hitung():
	try:
		panjang = float(input_panjang.get())
		lebar = float(input_lebar.get())
        luas = panjang * lebar
		keliling = 2 * (panjang+lebar)
        hasil_luas.config(text= f"Luas: {luas:.2f}")
		hasil_keliling.config(text= f"keliling: {keliling:.2f}")
	except ValueError:
		messagebox.showerror("Error", "Masukkan angka yang valid")
window = tk.Tk()
window.title("Kalkulator Persegi panjang")
window.geometry("400x300")
label_panjang = tk.Label(window, text= "Panjang:")
label_panjang.pack()
input_panjang = tk.Entry(window)
input_panjang.pack()
label_lebar = tk.Label(window, text= "Lebar")
label_lebar.pack()
input_lebar = tk.Entry(window)
input_lebar.pack()
button_hitung = tk.Button(window, text="Hitung", command=hitung)
button_hitung.pack()
hasil_luas = tk.Label(window, text= "Luas: ")
hasil_luas.pack()
hasil_keliling = tk.Label(window, text= "keliling: ")
hasil_keliling.pack()
window.mainloop()
