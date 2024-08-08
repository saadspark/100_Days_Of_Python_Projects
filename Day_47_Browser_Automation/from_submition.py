from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import time
chrome_option = webdriver.ChromeOptions()
chrome_option.add_experimental_option("detach", True)
drive = webdriver.Chrome(options=chrome_option)
drive.get("https://secure-retreat-92358.herokuapp.com/")

name = drive.find_element(By.NAME , "fName")
name.send_keys("Saad")

lName = drive.find_element(By.NAME , "lName")
lName.send_keys("Ahmad")

email = drive.find_element(By.NAME , "email")
email.send_keys("epsaadi01@gmail.com")


sub = drive.find_element(By.TAG_NAME , "button")
sub.click()

time.delay(delay=1)
drive.quit()

