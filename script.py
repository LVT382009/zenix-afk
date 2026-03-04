from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import chromedriver_autoinstaller
import time

# ===== CÀI ĐẶT =====
EMAIL = "levantam.98.2324@gmail.com"
PASSWORD = "Tamduc123@"
# ====================

def create_driver():
    options = Options()
    options.add_argument("--headless")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--disable-gpu")
    chromedriver_autoinstaller.install()
    return webdriver.Chrome(options=options)

def login(driver, email, password):
    driver.get("https://dash.zenix.sg/login")
    time.sleep(2)
    driver.find_element(By.NAME, "email").send_keys(email)
    driver.find_element(By.NAME, "password").send_keys(password)
    driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()
    time.sleep(3)
    print("✅ Đã login thành công!")

def stay_afk(driver):
    driver.get("https://dash.zenix.sg/dashboard/afk")
    print("🚀 AFK farming đã bắt đầu...")
    count = 0
    while True:
        time.sleep(60)
        count += 1
        print(f"⏱️ {count} phút đã qua. +{count} coin.")

if __name__ == "__main__":
    driver = create_driver()
    login(driver, EMAIL, PASSWORD)
    stay_afk(driver)