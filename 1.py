import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options = options,service=Service(ChromeDriverManager().install()))
driver.get("https://www.shufersal.co.il")
driver.maximize_window()



def open_browser():
 print(driver.current_url)
 print(driver.title)

def test_search():
 input_box1 = driver.find_element(By.XPATH,"/html[1]/body[1]/main[1]/header[1]/div[1]/div[2]/div[2]/form[2]/fieldset[1]/div[1]/span[1]/input[1]")
 time.sleep(5)
 input_box1.send_keys("Avocado")
 click_button = driver.find_element(By.XPATH,"//header/div[1]/div[2]/div[2]/form[2]/fieldset[1]/div[1]/div[1]/button[1]/i[1]")
 click_button.click()
 catch_error = driver.find_element(By.XPATH,"//h2[contains(text(),'נסו לבדוק אם לא חלה טעות כתיב או נסו להקליד ביטוי ')]")
 print(catch_error)
 driver.quit()

 #Run the test
open_browser()

test_search()
