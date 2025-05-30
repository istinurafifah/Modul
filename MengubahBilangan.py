def desimal_to_biner(n):
    return bin(n)[2:]

def desimal_to_oktal(n):
    return oct(n)[2:]

def desimal_to_hexadesimal(n):
    return hex(n)[2:].upper()

def menu_ubah_bilangan():
    while True:
        print("\nMenu Ubah Bilangan:")
        print("1. Desimal to Biner")
        print("2. Desimal to Oktal")
        print("3. Desimal to Hexadesimal")
        print("4. Menu Utama")

        pilihan = input("Pilih konversi (1-4): ")
        if pilihan == '4':
            break
        if pilihan not in ['1','2','3']:
            print("Pilihan tidak valid. Coba lagi.")
            continue
        
        try:
            nilai = int(input("Masukkan bilangan desimal (integer): "))
            if nilai < 0:
                print("Masukkan bilangan bulat positif.")
                continue
        except ValueError:
            print("Input harus berupa bilangan bulat positif. Coba lagi.")
            continue

        if pilihan == '1':
            hasil = desimal_to_biner(nilai)
            print(f"desimal {nilai} = biner {hasil}")
        elif pilihan == '2':
            hasil = desimal_to_oktal(nilai)
            print(f"desimal {nilai} = oktal {hasil}")
        elif pilihan == '3':
            hasil = desimal_to_hexadesimal(nilai)
            print(f"desimal {nilai} = hexadesimal {hasil}")