class Pelanggan:
    def __init__(self, transaction_id):
        self.transaction_id = transaction_id
        self.items = []
    
    def tambah_item(self, nama_item, jumlah_item, harga_satuan):
        item = {
            'nama_item': nama_item,
            'jumlah_item': jumlah_item,
            'harga_satuan': harga_satuan
        }
        self.items.append(item)
    
    def hapus_item(self, nama_item):
        for item in self.items:
            if item['nama_item'] == nama_item:
                self.items.remove(item)
                break

    def rekap_sementara(self):
        print(f"ID Transaksi Customer: {self.transaction_id}\n")
        print("| No | Nama Item | Jumlah Item | Harga Satuan | Total Harga |")
        print("|----|-----------|-------------|--------------|-------------|")
        for idx, item in enumerate(self.items, start=1):
            total_harga = item['jumlah_item'] * item['harga_satuan']
            print(f"| {idx}  | {item['nama_item']}      | {item['jumlah_item']}           | {item['harga_satuan']}         | {total_harga}       |")
        print("|-----------------------------------------------------------|")
      
    def rekap_belanja(self):
        print(f"ID Transaksi Customer: {self.transaction_id}\n")
        print("| No | Nama Item | Jumlah Item | Harga Satuan | Total Harga |")
        print("|----|-----------|-------------|--------------|-------------|")
        total_belanja = 0
        for idx, item in enumerate(self.items, start=1):
            total_harga = item['jumlah_item'] * item['harga_satuan']
            total_belanja += total_harga
            print(f"| {idx}  | {item['nama_item']}      | {item['jumlah_item']}           | {item['harga_satuan']}         | {total_harga}       |")
        print("|-----------------------------------------------------------|")
        print(f"|Total Belanja                                |{total_belanja}        |")
        print("|---------------------------------------------|-------------|")
        potongan_harga = 0
        if total_belanja > 500000:
            potongan_harga = total_belanja * 0.1
        elif total_belanja > 300000:
            potongan_harga = total_belanja * 0.08
        elif total_belanja > 200000:
            potongan_harga = total_belanja * 0.05
        print(f"|Total Potongan Harga                         |{potongan_harga}            |")
        print("|---------------------------------------------|-------------|")
        total_pembayaran = total_belanja - potongan_harga
        print(f"|Total Pembayaran                             |{total_pembayaran}        |\n\n Silahkan selesaikan pembayaran Anda. Terima kasih")