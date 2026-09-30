# Kuis 2 - Deret Aritmetika

print("=== PROGRAM DERET ARITMETIKA ===")

a = float(input("Masukkan suku pertama (a): "))
b = float(input("Masukkan beda (b): "))
n = int(input("Masukkan banyak suku (n): "))

# Menghitung suku ke-n
Un = a + (n - 1) * b

# Menghitung jumlah n suku
Sn = (n / 2) * (2 * a + (n - 1) * b)

print("\n=== HASIL PERHITUNGAN ===")
print(f"Suku pertama (a) = {a}")
print(f"Beda (b) = {b}")
print(f"Banyak suku (n) = {n}")
print(f"Suku ke-{n} (Un) = {Un}")
print(f"Jumlah {n} suku pertama (Sn) = {Sn}")