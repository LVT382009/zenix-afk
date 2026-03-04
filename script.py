from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import chromedriver_autoinstaller
import time
import os

# ===== ĐỌC TỪ GITHUB SECRETS =====
EMAIL = os.environ.get("EMAIL")
PASSWORD = os.environ.get("PASSWORD")
# ==================================

def create_driver():
    options = Options()
    options.add_argument("--headless")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--disable-gpu")
    options.add_argument("--window-size=1920,1080")
    chromedriver_autoinstaller.install()
    return webdriver.Chrome(options=options)

def login(driver, email, password):
    print("🔐 Đang login...")
    driver.get("https://dash.zenix.sg/login")
    time.sleep(3)
    
    driver.find_element(By.NAME, "email").send_keys(email)
    driver.find_element(By.NAME, "password").send_keys(password)
    driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()
    
    time.sleep(3)
    print("✅ Đã login thành công!")

def stay_afk(driver):
    print("🚀 Đang vào trang AFK...")
    driver.get("https://dash.zenix.sg/dashboard/afk")
    time.sleep(2)
    
    count = 0
    while True:
        time.sleep(60)
        count += 1
        print(f"⏱️ {count} phút đã qua. +{count} coin.")

if __name__ == "__main__":
    if not EMAIL or not PASSWORD:
        print("❌ Lỗi: Không tìm thấy EMAIL hoặc PASSWORD trong secrets!")
        exit(1)

    driver = create_driver()
    
    try:
        login(driver, EMAIL, PASSWORD)
        stay_afk(driver)
    except Exception as e:
        print(f"❌ Lỗi: {e}")
        driver.quit()