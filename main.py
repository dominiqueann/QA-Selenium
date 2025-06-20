from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
import time

driver = webdriver.Chrome()

driver.get ("https://www.booking.com/")
time.sleep(10)

txtUsername = driver.find_element(By.NAME, "email")
txtUsername.send_keys("odnimerjeffreyd@gmail.com")
time.sleep(3)

txtPassword = driver.find_element(By.NAME, "password")
txtPassword.send_keys("123456789")
time.sleep(3)

button = driver.find_element(By.NAME, "login")
button.click()

element = driver.find_element(By.CSS_SELECTOR, "Login Successful!")
driver.execute_script("arguments[0].click();", element)

wait = WebDriverWait(driver, timeout=2)
alert = wait.until(lambda d : d.switch_to.alert)
text = alert.text
alert.dismiss()
#button.click()
# buttonStudent = driver.find_element(By.NAME, "Students")
