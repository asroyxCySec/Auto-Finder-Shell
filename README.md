# **Author: AsroyxCySec**


# Fitur-Fitur Tambahan
### 1. Multithreading
Skrip ini menggunakan threading untuk memeriksa beberapa path di beberapa URL secara bersamaan, sehingga meningkatkan kecepatan pencarian.
Pengaturan jumlah thread dapat dilakukan melalui parameter `--threads`.  

  
### 2. Proxy
Fitur proxy memungkinkan penyembunyian alamat IP asli selama pencarian.


Konfigurasi proxy dilakukan melalui parameter `--proxy`.

Format
`http://user:password@proxyserver:port`  


### 3. Autentikasi HTTP
Skrip ini mendukung autentikasi HTTP dasar untuk mengakses URL yang memerlukan login.


Gunakan parameter `--auth`.


Format:
`username:password`  

### 4. Queue untuk Multithreading
Menggunakan queue untuk mengelola URL yang diperiksa setiap thread.
Setiap thread memproses URL dalam antrian dan mencetak hasil, meningkatkan efisiensi pencarian.  

### 5. Pencarian Path secara Otomatis
Daftar path atau endpoint yang diperiksa untuk shell dapat diperluas dengan menambahkannya ke daftar `shell_paths`.


Ini memungkinkan pencarian yang lebih luas dan fleksibel.      




        
# Penggunaan
### Tanpa Proxy dan Autentikasi:
`python auto_finder_shell.py http://targetsite.com`


### Dengan Proxy:
`python auto_finder_shell.py http://targetsite.com --proxy http://user:password@proxyserver:port`


### Dengan Autentikasi HTTP:
`python auto_finder_shell.py http://targetsite.com --auth username:password`



### Dengan Multithreading:
`python auto_finder_shell.py http://targetsite.com --threads 10`


## Catatan
#### 1. Skrip ini hanya untuk tujuan edukasi dan untuk digunakan dalam pengujian penetrasi yang sah, dengan izin eksplisit dari pemilik situs atau sistem. Penggunaan tanpa izin dapat melanggar hukum.


#### 2. Proxy membantu menghindari pemblokiran IP saat mencari kerentanan.



#### 3. Multithreading mempercepat pencarian, tetapi bisa membebani server target jika tidak digunakan dengan bijak.



#### 4. Anda dapat menambahkan lebih banyak path atau fitur untuk menyesuaikan skenario pengujian tertentu.

#### 5. Skrip dapat dikembangkan lebih lanjut untuk:
a) Pencarian direktori lebih mendalam.


b) Integrasi dengan alat eksploitasi otomatis.


c) Pencatatan hasil dalam format laporan.




# Support This Project

If you would like to support this project, you can make a donation through the following platforms:

- **[Ko-fi](https://ko-fi.com/AsroyxCySec)**
- **[Saweria](https://saweria.co/AsroyxCySec)**

Thank you for your support! 🙏
