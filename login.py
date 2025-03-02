from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Data login
EMAIL = "namaakunkamu@gmail.com"
PASSWORD = "Creelo2001!"

# Setup browser
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

options = webdriver.ChromeOptions()
options.add_argument("--start-maximized")
options.add_argument("--disable-blink-features=AutomationControlled")  # Hindari deteksi bot
options.add_argument("--disable-gpu")  # Perbaiki error GPU

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

# Buka Gmail login page
driver.get("https://accounts.google.com/signin")

# Tunggu input email muncul dan masukkan email
WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "identifierId"))).send_keys(EMAIL)
driver.find_element(By.ID, "identifierId").send_keys(Keys.RETURN)

# Tunggu beberapa detik agar halaman password bisa termuat sempurna
time.sleep(3)  

# Tunggu sampai elemen password bisa diklik (bukan hanya muncul)
password_input = WebDriverWait(driver, 15).until(
    EC.element_to_be_clickable((By.XPATH, "//input[@type='password']"))
)

# Coba klik dulu sebelum input
password_input.click()
time.sleep(1)  # Beri jeda sebentar

# Masukkan password
password_input.send_keys(PASSWORD)
password_input.send_keys(Keys.RETURN)

# Tunggu proses login selesai
time.sleep(5)

print("Login berhasil!")

# Buka halaman Gmail setelah login
driver.get("https://mail.google.com/mail/u/0/#inbox")

# Tunggu hingga halaman inbox termuat
WebDriverWait(driver, 15).until(
    EC.presence_of_element_located((By.CSS_SELECTOR, "table.F.cf.zt"))  # Tabel daftar email
)

print("Inbox terbuka!")

# Ambil daftar email pertama
emails = driver.find_elements(By.CSS_SELECTOR, "tr.zA")  # Setiap email ada dalam tag <tr> dengan class 'zA'

if emails:
    emails[0].click()  # Klik email pertama
    print("Email pertama dibuka!")
else:
    print("Inbox kosong atau elemen tidak ditemukan.")

# Tunggu sebentar sebelum menutup
time.sleep(5)

# Jangan lupa close browser setelah selesai
# driver.quit()

# Jangan lupa close browser setelah selesai
# driver.quit()
