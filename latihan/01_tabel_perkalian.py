# Program Tabel Perkalian

angka = int(input("Masukkan angka: "))

print(f"\nTabel perkalian {angka}:")
for i in range(1, 11):
    hasil = angka * i
    print(f"{angka} x {i} = {hasil}")