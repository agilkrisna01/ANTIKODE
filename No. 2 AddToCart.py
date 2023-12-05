import time
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys

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

# Isi formulir Login
# Input email
email_input = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.ID, 'email'))
)
email_input.send_keys('agilsindy2021@gmail.com')
time.sleep(1)

# Input password
password_input = driver.find_element(By.ID, 'password')
password_input.send_keys('agilkrisna123') 
time.sleep(1)

password_input.send_keys(Keys.ENTER)

# Klik tombol x untuk menutup iklan voucher
close_button = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, "//div[@class='close']//i[@class='ail ai-times']"))
)
close_button.click()

time.sleep(5)

# Menunggu hingga tombol "Shop" dapat diklik dan kemudian mengkliknya
shop_button = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, "(//span[contains(text(),'Shop Now')])[2]"))
)
shop_button.click()

# Klik Item Retrograde Slip On Kawung Cream
shoes_button = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, "//h4[normalize-space()='Retrograde Slip On Kawung Cream']"))
)
shoes_button.click()

# Klik Size
shoes_button = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, "//span[normalize-space()='EU 36']"))
)
shoes_button.click()

# Klik Add to Bag
shoes_button = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, "(//span[contains(text(),'Add to Bag')])[1]"))
)
shoes_button.click()