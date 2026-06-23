# Python-Search-item
# Sistem Manajemen Item Game Berbasis CRUD

Program manajemen data item dalam sebuah game berbasis konsol yang ditulis menggunakan bahasa pemrograman Python. Program ini mengimplementasikan operasi CRUD (Create, Read, Update, Delete) dengan memanfaatkan algoritma Binary Search untuk pencarian data secara efisien, serta menyimpan data secara persisten ke dalam file CSV.

---

## Daftar Isi

- [Deskripsi Program](#deskripsi-program)
- [Fitur](#fitur)
- [Struktur Data](#struktur-data)
- [Algoritma yang Digunakan](#algoritma-yang-digunakan)
- [Cara Menjalankan Program](#cara-menjalankan-program)
- [Contoh Penggunaan](#contoh-penggunaan)
- [Struktur File](#struktur-file)

---

## Deskripsi Program

Program ini dirancang sebagai sistem manajemen inventori item game yang memungkinkan pengguna untuk mengelola data item seperti senjata, armor, dan potion. Data disimpan dalam format CSV sehingga dapat diakses dan diperbarui secara persisten antar sesi program.

Program dikembangkan sebagai implementasi praktis dari konsep struktur data dan algoritma, khususnya penggunaan **Binary Search** pada data terurut dan pengelolaan list dinamis menggunakan modul `bisect`.

---

## Fitur

| No | Fitur | Keterangan |
|----|-------|------------|
| 1 | **Tambah Item** | Menambahkan item baru dengan ID unik, nama, tipe, dan harga |
| 2 | **Cari Item** | Mencari item berdasarkan ID menggunakan Binary Search |
| 3 | **Tampilkan Semua Item** | Menampilkan seluruh item dengan pilihan urutan (ID / Nama / Tipe / Harga) |
| 4 | **Perbarui Item** | Memperbarui nama, tipe, atau harga item berdasarkan ID |
| 5 | **Hapus Item** | Menghapus item dari daftar berdasarkan ID |
| 6 | **Simpan ke CSV** | Menyimpan seluruh perubahan ke file `item.csv` |
| 7 | **Keluar** | Keluar dari program dengan opsi menyimpan perubahan |

---

## Struktur Data

Setiap item direpresentasikan sebagai dictionary Python dengan atribut berikut:

```python
{
    "id"    : int,   # Identifikasi unik item
    "name"  : str,   # Nama item
    "type"  : str,   # Tipe item (Pedang, Busur Panah, Armor, Shield, Potion)
    "price" : int    # Harga item dalam satuan koin
}
```

Data disimpan dalam list yang selalu dipertahankan dalam keadaan **terurut berdasarkan ID** agar Binary Search dapat bekerja dengan benar.

---

## Algoritma yang Digunakan

### 1. Binary Search
Diimplementasikan secara manual pada fungsi `cari_biner()`. Digunakan untuk:
- Mencari item berdasarkan ID (menu Cari)
- Memvalidasi duplikasi ID saat menambah item baru
- Menemukan posisi item yang akan diperbarui atau dihapus

**Kompleksitas waktu:** O(log n)

### 2. Bisect (Insertion Sort Teroptimasi)
Menggunakan modul `bisect` bawaan Python pada fungsi `tambah_item()` untuk menyisipkan item baru di posisi yang tepat sehingga list tetap terurut tanpa perlu melakukan sorting ulang.

**Kompleksitas waktu:** O(log n) untuk pencarian posisi, O(n) untuk penyisipan

---

## Cara Menjalankan Program

### Persyaratan
- Python 3.x

### Langkah-langkah

1. Clone atau unduh repository ini
2. Pastikan file `Tugas_akhir.py` berada di direktori kerja
3. Jalankan program melalui terminal:

```bash
python Tugas_akhir.py
```

4. Jika file `item.csv` belum ada, program akan otomatis membuat 20 data item default
5. Ikuti instruksi menu yang ditampilkan di layar

---

## Contoh Penggunaan

```
========================================
     MENU CRUD ITEM GAME
========================================
1. Tambah Item
2. Cari berdasarkan ID - Binary Search
3. Tampilkan Semua Item dengan Urutan
4. Perbarui Item
5. Hapus Item
6. Simpan ke CSV
7. Keluar
========================================
Pilih (1-7):
```

---

## Struktur File

```
crud-item-game/
│
├── Tugas_akhir.py   # File program utama
├── item.csv         # File penyimpanan data (dibuat otomatis)
└── README.md        # Dokumentasi program
```

---

## Tipe Item yang Tersedia

- **Pedang** — Senjata jarak dekat
- **Busur Panah** — Senjata jarak jauh
- **Armor** — Pelindung tubuh
- **Shield** — Perisai pertahanan
- **Potion** — Item pemulihan

![Flowchart Struktur Data](images/Flowchart%20Struktur%20data.jpg)
