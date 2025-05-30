def cm_to_m(cm):
    return cm / 100

def m_to_cm(m):
    return m * 100

def menu_konversi():
    while True:
        print("\nMenu Konversi:")
        print("1. CM to M")
        print("2. M to CM")
        print("3. Menu Utama")

        pilihan = input("Pilih konversi (1-3): ")
        if pilihan == '3':
            break
        if pilihan not in ['1','2']:
            print("Pilihan tidak valid. Coba lagi.")
            continue
        
        try:
            nilai = float(input("Masukkan bilangan desimal: "))
        except ValueError:
            print("Input harus berupa angka desimal. Coba lagi.")
            continue
        
        if pilihan == '1':
            hasil = cm_to_m(nilai)
            print(f"{nilai} cm = {hasil} m")
        elif pilihan == '2':
            hasil = m_to_cm(nilai)
            print(f"{nilai} m = {hasil} cm")

def cm_to_m(cm):
    return cm / 100

def m_to_cm(m):
    return m * 100

def menu_konversi():
    while True:
        print("\nMenu Konversi:")
        print("1. CM to M")
        print("2. M to CM")
        print("3. Kembali ke Menu Utama")

        pilihan = input("Pilih konversi (1-3): ")
        if pilihan == '3':
            break
        if pilihan not in ['1','2']:
            print("Pilihan tidak valid. Coba lagi.")
            continue

        try: 
            nilai = float(input("Masukkan bilangan desimal: "))
        except ValueError:
            print("Harus berupa angka desimal. Coba lagi.")

        if pilihan == '1':
            hasil = cm_to_m(nilai)
            print(f"{nilai} cm = {hasil} m")
        elif pilihan == '2':
            hasil = m_to_cm(nilai)
            print(f"{nilai} m = {hasil} cm")