from selenium import webdriver
from selenium.webdriver.common.by import By

chrome_option = webdriver.ChromeOptions()
chrome_option.add_experimental_option("detach", True)
drive = webdriver.Chrome(options=chrome_option)
drive.get("https://www.python.org/")

times = drive.find_elements(By.CSS_SELECTOR, ".event-widget time")
events = drive.find_elements(By.CSS_SELECTOR, ".event-widget a")
event_list = [event.text for event in events]
time_list = [time.text for time in times]

dis = [{"time": time_list[i], "name": event_list[i]} for i in range(len(time_list))]
print(dis)




drive.quit()