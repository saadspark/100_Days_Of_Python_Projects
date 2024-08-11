from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

chrome_option = webdriver.ChromeOptions()
chrome_option.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=chrome_option)
driver.get("https://www.linkedin.com/uas/login?session_redirect=https%3A%2F%2Fwww.linkedin.com%2Ffeed%2F")

name = driver.find_element(By.ID, 'username')
name.send_keys('')

password = driver.find_element(By.ID, 'password')
password.send_keys('')

submit = driver.find_element(By.CSS_SELECTOR, '.login__form_action_container button')
submit.click()
time.sleep(60)

search = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.CLASS_NAME, 'search-global-typeahead__input'))
)
search.send_keys('Python')
search.send_keys(Keys.RETURN)

jobs = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, '/html/body/div[5]/div[3]/div[2]/section/div/nav/div/ul/li[1]/button'))
)
jobs.click()

easy_apply = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, '/html/body/div[5]/div[3]/div[4]/section/div/section/div/div/div/ul/li[7]/div/button'))
)
easy_apply.click()

list_jobs = driver.find_elements(By.CSS_SELECTOR, '.scaffold-layout__list-container')
for job in list_jobs:
    job.find_element(By.CSS_SELECTOR, '.jobs-search-results__list-item').click()
   
    # easy_apply_two = driver.find_element(By.CSS_SELECTOR, '.jobs-apply-button--top-card button')
 
    # easy_apply_two.click()
# driver.quit()