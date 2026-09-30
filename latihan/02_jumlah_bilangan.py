# Program Menghitung Jumlah Bilangan

n = int(input("Masukkan jumlah bilangan: "))

total = 0

for i in range(1, n + 1):
    bilangan = int(input(f"Masukkan bilangan ke-{i}: "))
    total += bilangan

print(f"\nJumlah seluruh bilangan = {total}")