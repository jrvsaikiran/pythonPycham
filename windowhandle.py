import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome(executable_path="F:\pycharm\drivers\chromedriver.exe")
driver.get("http://demo.automationtesting.in/Windows.html")
driver.maximize_window()
time.sleep(4)

driver.title
driver.find_element(By.XPATH, "//button[text()='    click   ']").click()

print("current one window", driver.current_window_handle)

all = driver.window_handles
for each in all:
    driver.switch_to.window(each)
    print(driver.title)

driver.find_element(By.XPATH, "//span[text()='Downloads']").click()
print(driver.title)
time.sleep(4)
if driver.title == "Downloads | Selenium":
    driver.close()

# driver.quit()    #all windows
