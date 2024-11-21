import requests
import argparse
import os
import threading
from queue import Queue
from urllib.parse import urljoin

# Fungsi untuk memeriksa shell pada path yang ditemukan
def check_shell(url, proxy=None):
    # Daftar file dan direktori yang umum untuk shell upload
    shell_paths = [
        "/shell.php", "/uploads/shell.php", "/admin/shell.php", "/wp-content/uploads/shell.php",
        "/images/shell.php", "/files/shell.php", "/uploads/php/shell.php",
        "/upload/shell.php", "/scripts/shell.php"
    ]
    
    for path in shell_paths:
        target_url = urljoin(url, path)
        try:
            response = requests.get(target_url, proxies=proxy, timeout=5)
            if response.status_code == 200:
                print(f"[!] Shell ditemukan di: {target_url}")
            else:
                print(f"[-] Tidak ada shell di: {target_url}")
        except requests.exceptions.RequestException as e:
            print(f"Error saat mencoba ke {target_url}: {e}")

# Fungsi untuk mencari shell di banyak path dengan multithreading
def search_shells_in_threads(target_url, proxy=None):
    threads = []
    q = Queue()

    for _ in range(5):  # Jumlah thread bisa disesuaikan
        t = threading.Thread(target=worker, args=(q, target_url, proxy))
        t.start()
        threads.append(t)
    
    # Mengisi antrian dengan URL yang akan diperiksa
    for i in range(5):  # Bisa disesuaikan dengan jumlah path yang ingin diperiksa
        q.put(target_url)

    # Menunggu semua thread selesai
    for t in threads:
        t.join()

# Fungsi worker untuk thread
def worker(q, target_url, proxy):
    while not q.empty():
        url = q.get()
        check_shell(url, proxy)
        q.task_done()

# Fungsi utama untuk menerima input dan menjalankan pengecekan
def main():
    parser = argparse.ArgumentParser(description="Auto Finder Shell untuk Bug Hunting")
    parser.add_argument("url", help="URL target untuk mencari shell. Misalnya: http://example.com")
    parser.add_argument("--proxy", help="Proxy (format http://user:pass@proxyserver:port)", default=None)
    parser.add_argument("--auth", help="Autentikasi HTTP (format user:password)", default=None)
    parser.add_argument("--threads", help="Jumlah thread yang digunakan (default 5)", type=int, default=5)
    args = parser.parse_args()

    target_url = args.url.rstrip('/')
    proxy = None
    if args.proxy:
        proxy = {"http": args.proxy, "https": args.proxy}
    
    auth = None
    if args.auth:
        auth = tuple(args.auth.split(":"))

    print(f"Memulai pengecekan shell di: {target_url}")
    search_shells_in_threads(target_url, proxy)

if __name__ == "__main__":
    main()
