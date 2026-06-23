import csv
import bisect

FILE_CSV = "item.csv"

def muat_data():
    """Membaca data dari CSV. Jika file tidak ada, buat 20 data default."""
    daftar_item = []
    try:
        with open(FILE_CSV, mode='r', encoding='utf-8') as file:
            pembaca = csv.DictReader(file)
            for baris in pembaca:
                item = {
                    "id": int(baris["id"]),
                    "name": baris["name"],
                    "type": baris["type"],
                    "price": int(baris["price"])
                }
                daftar_item.append(item)
        daftar_item.sort(key=lambda x: x["id"])
        print("Data berhasil dimuat dari", FILE_CSV, "(", len(daftar_item), "item)")
    except FileNotFoundError:
        print("File", FILE_CSV, "tidak ditemukan. Membuat 20 data default.")
        data_default = [
            {"id": 1, "name": "Pedang Besi", "type": "Pedang", "price": 500},
            {"id": 2, "name": "Busur Panjang", "type": "Busur Panah", "price": 750},
            {"id": 3, "name": "Armor Kulit", "type": "Armor", "price": 1200},
            {"id": 4, "name": "Shield Kayu", "type": "Shield", "price": 400},
            {"id": 5, "name": "Potion Heal", "type": "Potion", "price": 100},  
        ]
        simpan_data(data_default)
        return data_default
    except Exception as e:
        print("Gagal membaca CSV:", e, "Memulai dengan data kosong.")
    return daftar_item

def simpan_data(daftar_item):
    """Menyimpan daftar item ke file CSV."""
    with open(FILE_CSV, mode='w', newline='', encoding='utf-8') as file:
        kolom = ["id", "name", "type", "price"]
        penulis = csv.DictWriter(file, fieldnames=kolom)
        penulis.writeheader()
        penulis.writerows(daftar_item)
    print("Data berhasil disimpan ke", FILE_CSV)

def cari_biner(daftar_item, target_id):
    """Mengembalikan indeks item dengan ID target, atau -1 jika tidak ditemukan."""
    kiri, kanan = 0, len(daftar_item) - 1
    while kiri <= kanan:
        tengah = (kiri + kanan) // 2
        id_tengah = daftar_item[tengah]["id"]
        if id_tengah == target_id:
            return tengah
        elif id_tengah < target_id:
            kiri = tengah + 1
        else:
            kanan = tengah - 1
    return -1

def tambah_item(daftar_item):
    """CREATE - Menambahkan item baru."""
    try:
        id_baru = int(input("Masukkan ID (bilangan bulat): "))
        if cari_biner(daftar_item, id_baru) != -1:
            print("ID sudah digunakan, silakan gunakan ID lain.")
            return
        nama = input("Nama item: ").strip()
        tipe = input("Tipe (Pedang/Busur Panah/Armor/Shield/Potion): ").strip()
        harga = int(input("Harga: "))
        item_baru = {"id": id_baru, "name": nama, "type": tipe, "price": harga}
        list_id = [item["id"] for item in daftar_item]
        posisi = bisect.bisect_left(list_id, id_baru)
        daftar_item.insert(posisi, item_baru)
        print("Item berhasil ditambahkan.")
    except ValueError:
        print("Input tidak valid. ID dan harga harus berupa angka.")

def cari_item(daftar_item):
    """READ by ID - Mencari item menggunakan binary search."""
    try:
        target = int(input("Masukkan ID yang dicari: "))
        indeks = cari_biner(daftar_item, target)
        if indeks == -1:
            print("Item tidak ditemukan.")
        else:
            item = daftar_item[indeks]
            print("ID:", item["id"], "| Nama:", item["name"], "| Tipe:", item["type"], "| Harga:", item["price"])
    except ValueError:
        print("ID harus berupa angka.")

def tampilkan_semua(daftar_item, urutan="id"):
    """
    Menampilkan semua item dengan urutan tertentu.
    Parameter urutan: 'id', 'name', 'type', 'price'
    """
    if not daftar_item:
        print("Belum ada data.")
        return
    # Buat salinan agar tidak mengubah urutan asli
    salinan = daftar_item.copy()
    if urutan == "id":
        salinan.sort(key=lambda x: x["id"])
    elif urutan == "name":
        salinan.sort(key=lambda x: x["name"])
    elif urutan == "type":
        salinan.sort(key=lambda x: x["type"])
    elif urutan == "price":
        salinan.sort(key=lambda x: x["price"])
    else:
        salinan.sort(key=lambda x: x["id"])  # default

    print("\n" + "=" * 50)
    print("    DAFTAR ITEM (diurutkan berdasarkan", urutan.upper(), ")")
    print("=" * 50)
    print(" ID | Nama             | Tipe           | Harga")
    print("-" * 50)
    for item in salinan:
        print(f" {item['id']:2} | {item['name']:15} | {item['type']:12} | {item['price']:6}")
    print("=" * 50 + "\n")

def perbarui_item(daftar_item):
    """UPDATE - Memperbarui data item berdasarkan ID."""
    try:
        target = int(input("Masukkan ID item yang akan diperbarui: "))
        indeks = cari_biner(daftar_item, target)
        if indeks == -1:
            print("Item tidak ditemukan.")
            return
        print("Kosongkan input jika tidak ingin mengubah nilai.")
        nama_baru = input("Nama baru (sekarang: " + daftar_item[indeks]["name"] + "): ").strip()
        tipe_baru = input("Tipe baru (sekarang: " + daftar_item[indeks]["type"] + "): ").strip()
        harga_baru = input("Harga baru (sekarang: " + str(daftar_item[indeks]["price"]) + "): ").strip()
        if nama_baru:
            daftar_item[indeks]["name"] = nama_baru
        if tipe_baru:
            daftar_item[indeks]["type"] = tipe_baru
        if harga_baru:
            daftar_item[indeks]["price"] = int(harga_baru)
        print("Item berhasil diperbarui.")
    except ValueError:
        print("Harga harus berupa angka.")

def hapus_item(daftar_item):
    """DELETE - Menghapus item berdasarkan ID."""
    try:
        target = int(input("Masukkan ID item yang akan dihapus: "))
        indeks = cari_biner(daftar_item, target)
        if indeks == -1:
            print("Item tidak ditemukan.")
        else:
            item_hapus = daftar_item.pop(indeks)
            print("Item dengan ID", item_hapus["id"], "('" + item_hapus["name"] + "') berhasil dihapus.")
    except ValueError:
        print("ID harus berupa angka.")

def pilih_urutan():
    """Menampilkan menu pilihan urutan dan mengembalikan kunci urutan."""
    print("\nPilih urutan tampilan:")
    print("1. ID (default)")
    print("2. Nama (A-Z)")
    print("3. Tipe (A-Z)")
    print("4. Harga (termurah ke termahal)")
    pilihan = input("Masukkan angka (1-4): ")
    if pilihan == "1":
        return "id"
    elif pilihan == "2":
        return "name"
    elif pilihan == "3":
        return "type"
    elif pilihan == "4":
        return "price"
    else:
        print("Pilihan tidak valid, menggunakan urutan ID.")
        return "id"

def main():
    daftar_item = muat_data()
    while True:
        print("\n" + "=" * 40)
        print("        MENU ITEM GAME")
        print("=" * 40)
        print("1. Tambah Item")
        print("2. Cari berdasarkan ID - Binary Search")
        print("3. Tampilkan Semua Item dengan Urutan")
        print("4. Perbarui Item")
        print("5. Hapus Item")
        print("6. Simpan ke CSV")
        print("7. Keluar")
        print("=" * 40)
        pilihan = input("Pilih (1-7): ")

        if pilihan == "1":
            tambah_item(daftar_item)
        elif pilihan == "2":
            cari_item(daftar_item)
        elif pilihan == "3":
            urutan = pilih_urutan()
            tampilkan_semua(daftar_item, urutan)
        elif pilihan == "4":
            perbarui_item(daftar_item)
        elif pilihan == "5":
            hapus_item(daftar_item)
        elif pilihan == "6":
            simpan_data(daftar_item)
        elif pilihan == "7":
            simpan = input("Simpan perubahan ke CSV? (y/n): ").lower()
            if simpan == "y":
                simpan_data(daftar_item)
            print("Program selesai. Terima kasih.")
            break
        else:
            print("Pilihan tidak valid, silakan coba lagi.")

if __name__ == "__main__":
    main()