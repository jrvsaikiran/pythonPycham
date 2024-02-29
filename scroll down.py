import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

driver=webdriver.Chrome(executable_path="F:\pycharm\drivers\chromedriver.exe")
driver.get("https://www.countries-ofthe-world.com/flags-of-the-world.html")
driver.maximize_window()
time.sleep(3)

#sceolldown by pixcel number
driver.execute_script("window.scrollBy(0,3000)","")
time.sleep(2)

#scrolldown till element found
india= driver.find_element(By.XPATH,"//td[text()='India']")
driver.execute_script("arguments[0].scrollIntoView();",india)
time.sleep(2)


#scrolldown till last
driver.execute_script("window.scrollBy(0,document.body.scrollHeight)")


time.sleep(3)

driver.quit()