import time
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Mencari direktori dari driver
firefox_options = Options()
firefox_options.binary_location = r'C:\Program Files\Mozilla Firefox\firefox.exe'  # Ganti dengan path Firefox Anda

# Inisialisasi WebDriver Firefox
driver = webdriver.Firefox(options=firefox_options)

# Membuka situs web
driver.get('https://www.sepatucompass.com')

# Klik tombol x untuk menutup iklan voucher
close_button = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, "//div[@class='close']//i[@class='ail ai-times']"))
)
close_button.click()

time.sleep(2)

# Klik tombol icon "User"
user_button = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, "//i[@class='aib ai-profile-compass nav-icon'][1]"))
)
user_button.click()

time.sleep(2)

# Klik tombol "Register"
register_button = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, "//div[contains(@class,'form-wrapper')]//div[contains(@class,'form-nav row row-0')]//span[contains(text(),'Register')]"))
)
register_button.click()

time.sleep(2)

# Isi formulir pendaftaran
# Input Name
name_input = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.ID, 'name'))
)
name_input.send_keys('Agil Krisna')
time.sleep(1)

# Input Email
email_input = driver.find_element(By.XPATH, "(//input[@id='email'])[2]")
email_input.send_keys('agilkrisna01@gmail.com') 
time.sleep(1)

# Input Phone Number
phone_input = driver.find_element(By.ID, 'mobileNumber')
phone_input.send_keys('085156350536') 
time.sleep(1)

#Input Date of Birth
dob_input = driver.find_element(By.ID, 'dob')
dob_input.send_keys('1996-12-12')  
time.sleep(1)

# Input Password
password_input = driver.find_element(By.ID, 'password')
password_input.send_keys('password123')
time.sleep(2)

# Klik tombol "Register"
create_account_button = driver.find_element(By.XPATH, "(//span[contains(text(),'Register')])[5]")
create_account_button.click()

# Tutup browser setelah selesai
driver.quit()
