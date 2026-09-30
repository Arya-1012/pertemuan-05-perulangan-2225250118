# Program Validasi Input

while True:
    try:
        angka = int(input("Masukkan bilangan bulat positif: "))

        if angka > 0:
            print(f"Input valid: {angka}")
            break
        else:
            print("Input harus lebih dari 0.")

    except ValueError:
        print("Input tidak valid. Masukkan bilangan bulat.")