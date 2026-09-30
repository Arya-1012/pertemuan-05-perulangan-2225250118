# Program Menghitung Bilangan Genap

n = int(input("Masukkan batas bilangan: "))

jumlah = 0

print("\nBilangan genap:")

for i in range(1, n + 1):
    if i % 2 == 0:
        print(i, end=" ")
        jumlah += i

print(f"\n\nJumlah bilangan genap = {jumlah}")