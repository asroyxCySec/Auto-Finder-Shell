import requests
import argparse
import threading
from queue import Queue
from urllib.parse import urljoin


# Fungsi untuk memeriksa shell pada path yang ditemukan
def check_shell(full_url, proxy=None):
    try:
        response = requests.get(full_url, proxies=proxy, timeout=10)
        if response.status_code == 200:
            print(f"[!] Shell ditemukan di: {full_url}")
        else:
            print(f"[-] Tidak ada shell di: {full_url}")
    except requests.exceptions.RequestException as e:
        print(f"[Error] Tidak dapat mengakses {full_url}: {e}")


# Fungsi worker untuk memproses URL dalam antrian
def worker(queue, target_url, proxy):
    while not queue.empty():
        path = queue.get()
        full_url = urljoin(target_url, path)
        check_shell(full_url, proxy)
        queue.task_done()


# Fungsi untuk mencari shell dengan multithreading
def search_shells_in_threads(target_url, proxy=None, num_threads=5):
    # Daftar path shell
    shell_paths = [
        # Root-level directories
        "/shell.php", "/phpinfo.php", "/cmd.php", "/evil.php", "/malware.php",
        "/backdoor.php", "/exploit.php", "/webshell.php", "/hack.php",
        "/upload.php", "/config.php", "/tmp.php", "/test.php", "/error.php",
        "/access.php", "/admin.php", "/control.php", "/debug.php",
        "/password.php", "/info.php", "/portal.php", "/connect.php",
        "/home.php", "/web.php", "/init.php", "/install.php", "/setup.php",
        "/panel.php", "/config/settings.php", "/auth.php",
        # Upload directories
        "/uploads/shell.php", "/uploads/cmd.php", "/uploads/backdoor.php",
        "/uploads/evil.php", "/uploads/webshell.php", "/uploads/malware.php",
        # WordPress directories
        "/wp-content/uploads/shell.php", "/wp-content/shell.php",
        "/wp-includes/shell.php", "/wp-admin/shell.php",
        "/wp-content/plugins/shell.php", "/wp-content/themes/shell.php",
        # Common media directories
        "/images/shell.php", "/img/shell.php", "/media/shell.php",
        "/assets/shell.php", "/files/shell.php",
        # Temporary directories
        "/temp/shell.php", "/tmp/shell.php", "/cache/shell.php",
        # Admin or control panels
        "/admin/shell.php", "/control/shell.php", "/panel/shell.php",
        "/management/shell.php", "/cpanel/shell.php", "/root/shell.php",
        # Backup directories
        "/backup/shell.php", "/old/shell.php", "/bak/shell.php",
        "/backups/shell.php", "/restore/shell.php", "/previous/shell.php",
        # Scripts and executables
        "/scripts/shell.php", "/cgi-bin/shell.php",
        # Framework-specific
        "/laravel/shell.php", "/symfony/shell.php", "/django/shell.php",
        "/rails/shell.php", "/nodejs/shell.php", "/express/shell.php",
        "/flask/shell.php", "/codeigniter/shell.php", "/yii/shell.php",
        # FTP and cloud storage
        "/ftp/shell.php", "/sftp/shell.php", "/cloud/shell.php",
        "/onedrive/shell.php", "/dropbox/shell.php", "/google-drive/shell.php",
        # Logs and debugging
        "/logs/shell.php", "/debug/shell.php",
        # Miscellaneous
        "/misc/shell.php", "/core/shell.php", "/system/shell.php",
        "/default/shell.php", "/hidden/shell.php",
        # User-related
        "/user/shell.php", "/users/shell.php",
        # Random and obfuscated patterns
        "/xyz/shell.php", "/abc/shell.php", "/random/shell.php",
        # Complex nesting
        "/uploads/tmp/shell.php", "/uploads/images/tmp/shell.php",
        "/admin/uploads/tmp/shell.php",
    ]

    # Isi antrian dengan path-path yang akan diperiksa
    queue = Queue()
    for path in shell_paths:
        queue.put(path)

    # Buat dan jalankan thread
    threads = []
    for _ in range(num_threads):
        t = threading.Thread(target=worker, args=(queue, target_url, proxy))
        t.start()
        threads.append(t)

    # Tunggu semua thread selesai
    for t in threads:
        t.join()


# Fungsi utama untuk menerima input dan menjalankan pengecekan
def main():
    parser = argparse.ArgumentParser(description="Auto Finder Shell untuk Bug Hunting")
    parser.add_argument("url", help="URL target untuk mencari shell. Misalnya: http://example.com")
    parser.add_argument("--proxy", help="Proxy (format http://user:pass@proxyserver:port)", default=None)
    parser.add_argument("--threads", help="Jumlah thread yang digunakan (default 5)", type=int, default=5)
    args = parser.parse_args()

    target_url = args.url.rstrip('/')
    proxy = None
    if args.proxy:
        proxy = {"http": args.proxy, "https": args.proxy}

    print(f"Memulai pengecekan shell di: {target_url}")
    search_shells_in_threads(target_url, proxy, args.threads)


if __name__ == "__main__":
    main()
