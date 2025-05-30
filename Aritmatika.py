def penjumlahan(a, b):
    return a + b

def perpangkatan(a, b):
    return a ** b

def perkalian(a, b):
    return a * b

def menu_aritmatika():
    while True:
        print("\nMenu Aritmatika:")
        print("1. Penjumlahan")
        print("2. Perpangkatan")
        print("3. Perkalian")
        print("4. Kembali ke Menu Utama")
        
        pilihan = input("Pilih operasi (1-4): ")
        if pilihan == '4':
            break
        if pilihan not in ['1','2','3']:
            print("Pilihan tidak valid. Coba lagi.")
            continue
        
        try:
            a = float(input("Masukkan bilangan pertama: "))
            b = float(input("Masukkan bilangan kedua: "))
        except ValueError:
            print("Harus berupa angka. Coba lagi.")
            continue

        if pilihan == '1':
            hasil = penjumlahan(a,b)
            print(f"Hasil: {hasil}")
        elif pilihan == '2':
            hasil = perpangkatan(a,b)
            print(f"Hasil: {hasil}")
        elif pilihan == '3':
            hasil = perkalian(a,b)
            print(f"Hasil: {hasil}")