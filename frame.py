import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

driver=webdriver.Chrome(executable_path="F:\pycharm\drivers\chromedriver.exe")
driver.get("https://ui.vision/demo/webtest/frames/")
driver.maximize_window()

driver.switch_to.frame("mytext1")
#driver.find_elements(By.NAME,"mytext1")
driver.find_element(By.XPATH,"//*[@id='id1'']/div/input").send_keys("sai")


time.sleep(3)
#driver.quit()
