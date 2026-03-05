from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import chromedriver_autoinstaller
import time
import os

EMAIL = os.environ.get("EMAIL")
PASSWORD = os.environ.get("PASSWORD")

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
    wait = WebDriverWait(driver, 10)
    wait.until(EC.presence_of_element_located((By.ID, "email"))).send_keys(email)
    driver.find_element(By.ID, "password").send_keys(password)
    driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()
    time.sleep(3)
    print("✅ Đã login thành công!")

def get_coins(driver):
    try:
        coin_span = driver.find_element(
            By.CSS_SELECTOR,
            "div.bg-blue-950\\/30 span.font-semibold.text-blue-400"
        )
        return int(coin_span.text.strip())
    except:
        return None

def reset_afk(driver):
    print("🔄 Đang reset AFK...")
    driver.get("https://dash.zenix.sg/dashboard")
    time.sleep(2)
    driver.get("https://dash.zenix.sg/dashboard/afk")
    time.sleep(2)
    print("✅ Đã reset xong!")

def stay_afk(driver):
    print("🚀 Đang vào trang AFK...")
    driver.get("https://dash.zenix.sg/dashboard/afk")
    time.sleep(2)

    count = 0
    last_coin = get_coins(driver)
    print(f"💰 Coin hiện tại: {last_coin}")

    while True:
        time.sleep(60)
        count += 1

        current_coin = get_coins(driver)
        print(f"⏱️ {count} phút | 💰 Coin: {current_coin}")

        if current_coin is None or current_coin <= last_coin:
            print("🚨 Coin không tăng! Đang reset...")
            reset_afk(driver)
            last_coin = get_coins(driver)
            print(f"💰 Coin sau reset: {last_coin}")
        else:
            last_coin = current_coin

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
