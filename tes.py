def get_number(prompt):
	while True:
		try:
			return float(input(prompt))
		except ValueError:
			print("Input harus berupa angka. Silakan coba lagi.")

def main():
	print("Masukkan dua angka untuk operasi matematika.")
	num1 = get_number("Masukkan angka pertama: ")
	num2 = get_number("Masukkan angka kedua: ")

	print(f"Hasil penjumlahan: {num1 + num2}")
	print(f"Hasil pengurangan: {num1 - num2}")
	print(f"Hasil perkalian: {num1 * num2}")
	if num2 != 0:
		print(f"Hasil pembagian: {num1 / num2}")
	else:
		print("Pembagian dengan nol tidak diperbolehkan.")

if __name__ == "__main__":
	main()