from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

chrome_option = webdriver.ChromeOptions()
chrome_option.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=chrome_option)
driver.get("https://www.daraz.pk/#hp-just-for-you")

# elem = driver.find_element(By.CLASS_NAME, "price")
# elem = driver.find_element(By.CSS_SELECTOR, ".fs-origin-price .price")


#right click > copy > copy xpath > past
elem = driver.find_element(By.XPATH, '//*[@id="461817480"]/div[2]/div[2]/div/span[2]')

print(elem.text)



driver.close()