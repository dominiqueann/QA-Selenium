from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

service = Service('chromedriver.exe') 
driver = webdriver.Chrome(service=service)
wait = WebDriverWait(driver, 15)
driver.maximize_window()

try:
    driver.get("https://ecommerce-playground.lambdatest.io/")
    print("✅ Opened homepage")
    time.sleep(2)

    account_btn = wait.until(EC.element_to_be_clickable(
        (By.CSS_SELECTOR, "a[role='button'][href*='account/account']")))
    account_btn.click()
    time.sleep(2)

    register_btn = wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "Register")))
    register_btn.click()
    time.sleep(2)

    wait.until(EC.presence_of_element_located((By.ID, "input-firstname"))).send_keys("Dominique Ann")
    time.sleep(1)
    driver.find_element(By.ID, "input-lastname").send_keys("Aquino")
    time.sleep(1)
    driver.find_element(By.ID, "input-email").send_keys("dominiqueannaquino@gmail.com")
    time.sleep(1)
    driver.find_element(By.ID, "input-telephone").send_keys("09634819468")
    time.sleep(1)
    driver.find_element(By.ID, "input-password").send_keys("134340ann")
    time.sleep(1)
    driver.find_element(By.ID, "input-confirm").send_keys("134340ann")
    time.sleep(1)
    print("✅ Filled in form fields")

    agree_checkbox = wait.until(EC.presence_of_element_located((By.ID, "input-agree")))
    driver.execute_script("arguments[0].click();", agree_checkbox)
    time.sleep(1)
    print("✅ Checked 'I agree' checkbox using JavaScript")

    continue_button = driver.find_element(By.CSS_SELECTOR, "#content > form > div > div > input")
    continue_button.click()
    print("🚀 Clicked Continue")

    time.sleep(3)
    if "success" in driver.current_url or "Your Account Has Been Created!" in driver.page_source:
        print("🎉 Registration successful!")
    else:
        print("⚠️ Registration may have failed — check for existing email or form error.")

except Exception as e:
    print(f"❌ Error: {e}")

finally:
    time.sleep(5)
    driver.quit()
