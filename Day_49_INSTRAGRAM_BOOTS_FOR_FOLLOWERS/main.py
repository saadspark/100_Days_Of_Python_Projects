from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys

class InstagramBoat :
    def __init__(self, username, password):
        chrome_option = webdriver.ChromeOptions()
        chrome_option.add_experimental_option("detach", True)
      
        self.driver = webdriver.Chrome(options=chrome_option)
        self.driver.get("https://www.instagram.com/")
        self.driver.implicitly_wait(10)
        self.username = username
        self.password = password

    def login(self):
        username_field = self.driver.find_element(By.NAME, "username")
        username_field.send_keys(self.username)
        password_field = self.driver.find_element(By.NAME, "password")
        password_field.send_keys(self.password)
        password_field.send_keys(Keys.RETURN)
        self.driver.implicitly_wait(20)

    def search(self, hashtag):
        search_field = self.driver.find_element(By.CLASS_NAME, '//*[@id="mount_0_0_XM"]/div/div/div[2]/div/div/div[1]/div[1]/div[2]/div/div/div/div/div[2]/div[2]/span/div')
        search_field.click()
        find = self.driver.find_element(By.XPATH, '//*[@id="mount_0_0_O6"]/div/div/div[2]/div/div/div[1]/div[1]/div[2]/div/div/div[2]/div/div/div[2]/div/div/div[1]/div/div/input')
        find.send_keys(hashtag)
        self.driver.implicitly_wait(10)
        find.send_keys(Keys.RETURN)
        self.driver.implicitly_wait(10)
        find.send_keys(Keys.RETURN)
        self.driver.implicitly_wait(10)

    def like_photos(self, number_of_photos):
        photo_links = self.driver.find_elements(By.XPATH, "//a[@class='_ac69']")
        for i in range(number_of_photos):
            photo_links[i].click()
            like_button = self.driver.find_element(By.XPATH, "//span[@class='_aamw']")
            like_button.click()
            close_button = self.driver.find_element(By.XPATH, "//button[@class='_ac69']")
            close_button.click()
            self.driver.implicitly_wait(10)

    # def close(self):
    #     self.driver.quit()


boot = InstagramBoat('','')
boot.login()
boot.search('BABAR AZAM')