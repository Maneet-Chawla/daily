from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time


# Launch Chrome automatically with correct driver
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

driver.get("https://rahulshettyacademy.com/client")


email = driver.find_element(By.ID,"userEmail")
password=driver.find_element(By.ID,"userPassword")
driver.find_element(By.ID,"login").click()
email.send_keys("maneet@gmil.com")
password.send_keys("12345")
time.sleep(30)
input("type something on terminal")

