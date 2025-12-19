from dask.distributed import Client
import time
import os

# Fungsi yang akan dijalankan oleh Dask Worker
# Fungsi ini akan tidur sejenak untuk mensimulasikan pekerjaan yang berat
def hitung_kuadrat(x):
    """Menghitung kuadrat dari x dan menunggu sebentar."""
    # Menunggu 1 detik
    time.sleep(1)
    # Mencetak di mana kode ini dijalankan (hanya untuk debugging worker)
    # print(f"Menghitung {x}**2 pada proses: {os.getpid()}", flush=True)
    return x * x

if __name__ == '__main__':
    # 1. Sambungkan ke Dask Scheduler
    # Alamat scheduler di host lokal: localhost:8786
    try:
        # Menghubungkan ke Dask Scheduler yang dijalankan oleh Docker Compose
        client = Client("tcp://localhost:8786")
        print("✅ Berhasil tersambung ke Dask Cluster!")
        print(f"Info Cluster: {client}")
        
        # 2. Buat daftar input
        data_input = list(range(10)) # [0, 1, 2, ..., 9]
        
        start_time = time.time()
        
        # 3. Kirim tugas ke Cluster (komputasi terdistribusi)
        # client.submit() mengembalikan objek Future segera
        futures = client.map(hitung_kuadrat, data_input)
        
        print(f"\n🚀 Mengirim {len(futures)} tugas ke cluster...")

        # 4. Tunggu hasil dan ambil (Pull)
        # client.gather() akan menunggu sampai semua Future selesai
        # dan mengembalikan hasilnya ke proses Python lokal
        results = client.gather(futures)
        
        end_time = time.time()
        
        # 5. Tampilkan hasil
        print("\n✨ Hasil komputasi terdistribusi:")
        print(results)
        
        # Bandingkan waktu eksekusi
        execution_time = end_time - start_time
        print(f"\n⏳ Total waktu eksekusi: {execution_time:.2f} detik")
        
        # 6. Tutup koneksi
        client.close()

    except ConnectionRefusedError:
        print("❌ GAGAL tersambung ke Dask Scheduler. Pastikan Docker Compose sudah berjalan.")
    except Exception as e:
        print(f"Terjadi error: {e}")