# Belanja-Mandiri
Belanja Mandiri adalah program python yang dibuat untuk memenuhi tugas belajar Sekolah Data Pacmann

Alur program ini secara sederhana adalah sebagai berikut:
1. Program akan meminta user untuk memasukkan kode transaksi. Kode transaksi harus numerik jika berupa string maka akan muncul pesan error
2. Setelah user memasukkan kode transaksi selanjutnya program akan menampilkan menu:
   - Tambah item
   - Hapus item
   - Revisi item
   - Selesai
3. Jika memilih "Tambah item" maka user akan diminta memasukkan 'nama item', 'jumlah item', 'harga satuan'
4. Jika memilih 'Hapus item' maka user akan diminta memasukkan 'nama item' yang akan dihapus setelahh itu proogram akan menghapus seluruh data terkait item tersebut
5. Jika memilih 'Revisi item' maka user akan diminta memasukkan 'nama item' yang akan direvisi kemudian program akan meminta user memasukkan jumlah item yang baru dan harga satuannya
6. Setiap kali user menyelesaikan penambahan item atau penghapusan item atau revisi item, maka proogram akan menampilkan daftar barang yanag sudah diinput yaitu 'nama item', 'jumlah item', 'harga satuan' dan program juga akan menghitung total nilai belanja setiap item yang diinput.
7. Jika user memilih selesai maka prgoram akan  menampilkan daftar barang yanag sudah diinput yaitu 'nama item', 'jumlah item', 'harga satuan' dan program juga akan menghitung total nilai belanja setiap barang yang diinput dan total nilai belanja seluruh barang.
8. Program juga akan menghitung apakah user mendapatkan diskon atau tidak berdasarkan total nilai belanja seluruh barang.
9. Jika total belanja lebih dari 500 ribu mendapatkan diskon 10% dari total belanja
10. Jika total belanja lebih dari 300 ribu s/d 500 ribu mendapatkan diskon 8% dari total belanja
11. Jika total belanja lebi dari  200 ribu s/d 300 ribu mendapatkan diskon 5% dari total belanja
12. Program akan menghitung total pembayaran adalah total belanja dikurangi diskon
