# Input data

data = input("Masukkan nama kamu, simple: ")

print("Nama kamu adalah: ", data, "\ntype data ini kamu adalah: ", type(data))

#data yang dimasukkan haslnya akan: string

# Kalau mau merubah tipe data string ke integer, maka gunakan int()

data_integer = int(input("Masukkan jumlah umur kamu: "))
print("Umur kamu adalah: ", data_integer, "\nType data ini adalah: ", type(data_integer))

if data_integer == 17:
	print("Kamu sudah dewasa! wkwkwk :v")

#data yang dimasukkan hasilnya akan: integer

# Kalau mau merubah tipe data string ke float, maka gunakan float()
data_float = float(input("Masukkan jumlah umur kamu (kasih dengan bulan juga dengan .): "))
print("Umur kamu adalah: ", data_float, "bulan", "\nType data ini adalah: ", type(data_float))

if data_float == 17:
	print("Kamu sudah dewasa! wkwkwk :v")

#data yang dimasukkan hasilnya akan: float

# Kalau mau merubah tipe data string ke boolean, maka gunakan bool()

biner = bool(int(input("Masukkan angka 0 atau 1: ")))
print("Angka yang kamu masukkan adalah: ", biner, "\nType data ini adalah: ", type(biner))

if biner == True:
	print("Kamu memasukkan angka 1")