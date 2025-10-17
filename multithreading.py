import threading
import time
import random

# 1. Definisikan fungsi (tugas) yang akan dijalankan oleh thread
def tugas_koki(nama_tugas, durasi_langkah):
    """
    Fungsi ini mensimulasikan pekerjaan yang memakan waktu.
    """
    print(f">>> {nama_tugas} dimulai.")
    
    # Simulasikan beberapa langkah kerja
    for i in range(1, 4):
        print(f"    {nama_tugas}: Langkah ke-{i}")
        # Jeda sejenak untuk mensimulasikan waktu tunggu (misalnya, I/O)
        time.sleep(durasi_langkah) 
        
    print(f"<<< {nama_tugas} selesai.")

# 2. Program Utama

if __name__ == "__main__":
    
    start_time = time.time()
    
    print("Program Utama dimulai. Chef mulai bekerja! 🧑‍🍳")
    
    # Mendefinisikan tugas dan argumennya
    # Tugas 1: Membuat Kopi (durasi langkah 0.5 detik)
    thread_kopi = threading.Thread(
        target=tugas_koki, 
        args=("Tugas Kopi ☕", 0.5)
    )
    
    # Tugas 2: Memanggang Roti (durasi langkah 1.0 detik, lebih lama)
    thread_roti = threading.Thread(
        target=tugas_koki, 
        args=("Tugas Roti 🍞", 1.0)
    )
    
    # Memulai eksekusi thread
    thread_kopi.start()
    thread_roti.start()
    
    # Perintah join() memastikan program utama menunggu kedua thread selesai
    # sebelum mencetak "Program Utama selesai."
    thread_kopi.join()
    thread_roti.join()
    
    end_time = time.time()
    elapsed_time = end_time - start_time
    print(f"Total waktu eksekusi dengan Multithreading: {elapsed_time:.2f} detik")
    print("Program Utama selesai. (Semua pesanan terkirim!)")
    
    print("===== Ini Cara Serial tanpa Multithreading =====")
    start_time_serial = time.time()
    tugas_koki("Tugas Kopi ☕", 0.5)
    tugas_koki("Tugas Roti 🍞", 1.0)
    end_time_serial = time.time()
    elapsed_time_serial = end_time_serial - start_time_serial
    print(f"Total waktu eksekusi serial: {elapsed_time_serial:.2f} detik")