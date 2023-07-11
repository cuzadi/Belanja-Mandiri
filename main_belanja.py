from modul_pelanggan import Pelanggan

# Fungsi untuk mengecek input apakah merupakan angka valid
def is_valid_number(input_number):
    try:
        float(input_number)
        return True
    except ValueError:
        return False

def main():
    # Memasukkan ID Transaksi Customer
    transaction_id = input("Masukkan ID Transaksi Customer: ")

    # Membuat objek Pelanggan
    pelanggan = Pelanggan(transaction_id)

    # Looping untuk menambah, menghapus, atau revisi item
    while True:
        print("\nPilihan:")
        print("1. Tambah Item")
        print("2. Hapus Item")
        print("3. Revisi Item")
        print("4. Selesai")
        pilihan = input("Masukkan pilihan: ")

        if pilihan == '1':
            # Menambahkan item
            nama_item = input("Masukkan Nama Item: ")
            jumlah_item = input("Masukkan Jumlah Item: ")
            harga_satuan = input("Masukkan Harga Satuan: ")

            if is_valid_number(jumlah_item) and is_valid_number(harga_satuan):
                pelanggan.tambah_item(nama_item, float(jumlah_item), float(harga_satuan))
                print("Item berhasil ditambahkan!")
                pelanggan.rekap_sementara()
            else:
                print("Input Jumlah Item dan Harga Satuan harus berupa angka.")

        elif pilihan == '2':
            # Menghapus item
            nama_item = input("Masukkan Nama Item yang akan dihapus: ")
            pelanggan.hapus_item(nama_item)
            print(f"Item {nama_item} berhasil dihapus!")
            pelanggan.rekap_sementara()

        elif pilihan == '3':
            # Revisi item
            nama_item = input("Masukkan Nama Item yang akan direvisi: ")
            jumlah_item = input("Masukkan Jumlah Item yang baru: ")
            harga_satuan = input("Masukkan Harga Satuan yang baru: ")

            if is_valid_number(jumlah_item) and is_valid_number(harga_satuan):
                pelanggan.hapus_item(nama_item)
                pelanggan.tambah_item(nama_item, float(jumlah_item), float(harga_satuan))
                print("Item berhasil direvisi!")
                pelanggan.rekap_sementara()
            else:
                print("Input Jumlah Item dan Harga Satuan harus berupa angka.")

        elif pilihan == '4':
            # Selesai
            pelanggan.rekap_belanja()
            break
main()