from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
import time

service = Service('chromedriver.exe')  
driver = webdriver.Chrome(service=service)
wait = WebDriverWait(driver, 15)
driver.maximize_window()

try:
    driver.get("https://ecommerce-playground.lambdatest.io/")
    time.sleep(2)

    wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "a[role='button'][href*='account/account']"))).click()
    time.sleep(1)
    wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "Login"))).click()
    time.sleep(2)

    wait.until(EC.presence_of_element_located((By.ID, "input-email"))).send_keys("dominiqueannaquino@gmail.com")
    time.sleep(1)
    driver.find_element(By.ID, "input-password").send_keys("134340ann")
    time.sleep(1)
    driver.find_element(By.CSS_SELECTOR, "input.btn.btn-primary").click()
    time.sleep(2)

    wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "a[role='button'][href*='account/account']")))

    home_button = wait.until(EC.element_to_be_clickable(
        (By.XPATH, '//*[@id="widget-navbar-217834"]/ul/li[1]/a')
    ))
    home_button.click()
    time.sleep(2)

    wait.until(EC.element_to_be_clickable((
        By.XPATH, "//img[@alt='Desktops']"
    ))).click()
    time.sleep(2)

    wait.until(EC.element_to_be_clickable((
        By.XPATH, '//*[@id="mz-filter-panel-0-2"]/div/div[1]/div/label'
    ))).click()
    print("🧭 Selected Mac subcategory")
    time.sleep(2)

    wait.until(EC.element_to_be_clickable((
        By.XPATH, "//img[@alt='iPod Nano' and contains(@class, 'lazy-load')]"
    ))).click()
    time.sleep(3)

    add_to_cart_btn = wait.until(EC.presence_of_element_located((
        By.CSS_SELECTOR, "button.btn-cart")
    ))
    driver.execute_script("arguments[0].scrollIntoView(true);", add_to_cart_btn)
    time.sleep(1.5)
    driver.execute_script("arguments[0].click();", add_to_cart_btn)
    time.sleep(2)

    # 10. Click View Cart
    wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "View Cart"))).click()
    time.sleep(10)

    # 11. Click Continue Shopping
    wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "Continue Shopping"))).click()
    time.sleep(2)
    
    wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "a[role='button'][href*='account/account']"))).click()
    time.sleep(1)
    wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "Logout"))).click()
    time.sleep(2)

except Exception as e:
    print(f"❌ Error: {e}")

finally:
    time.sleep(5)
    driver.quit()
