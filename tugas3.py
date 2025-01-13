# Nama: ADDIN

print('Dibuat oleh ADDIN\n\n')

print("Masukkan 2 kali berupa ANGKA untuk dibagikan dibawah ini: ")

def tugas_addin():
	while True:
		try:
			angka1 = float(input("Masukkan angka pertama: "))
			angka2 = float(input("Masukkan angka kedua: "))
			hasil = angka1 / angka2
			print(f"Hasil pembagian dari {angka1} dan {angka2} adalah: {hasil}")
			break
		except ValueError:
			print("Input yang dimasukkan bukan angka atau nol. Silakan coba lagi.")
			continue
		except ZeroDivisionError:
			print("Pembagian dengan nol tidak diperbolehkan. Silakan coba lagi.")
			continue




tugas_addin()