from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

driver= webdriver.Chrome(executable_path="F:\pycharm\drivers\chromedriver.exe")
driver.get("http://www.expedia.com/")
driver.maximize_window()
driver.implicitly_wait(10)      #implicity wait

driver.find_element(By.XPATH,"//span[text()='Flights']").click()

wait = WebDriverWait(driver,1)
element = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[@aria-label='Leaving from']"))) #explicit wait
#element.click()
time.sleep(3)

#print links

tag=driver.find_elements(By.TAG_NAME,"a")
print(len(tag))

for link in tag:
    print(link.text)
    #print(link)

#click on link text
driver.find_element(By.LINK_TEXT,"Cars").click()
driver.find_element(By.PARTIAL_LINK_TEXT,"Pack").click()

time.sleep(3)
driver.quit()