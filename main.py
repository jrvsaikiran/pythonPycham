from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import chrome
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome(executable_path="F:\pycharm\drivers\chromedriver.exe")
driver.maximize_window()
driver.get("https://www.facebook.com/r.php?locale=en_GB&display=page")
driver.implicitly_wait(5)
print(driver.title)
#assert "Sign up for Facebook | Facebook" in driver.title
print(driver.current_url)
#print(driver.page_source)
element = driver.find_element(By.NAME,"firstname")
print(element.is_enabled())
print(element.is_displayed())
print(element.size)
driver.find_element(By.NAME,"firstname").send_keys("sai kiran")


#select class
day=driver.find_element(By.NAME,"birthday_day")
drp=Select(day)
drp.select_by_index(13)
time.sleep(4)
drp.select_by_value("22")
time.sleep(4)
drp.select_by_visible_text("1")

#count no.of options
print("length is ",len(drp.options))


#capture options indropdown

allopt = drp.options
for option in allopt:  #for each loop
    print("NO:-",option.text)



driver.find_element(By.XPATH,"//input[@class ='_8esa' and @value='1']").click()
radio=driver.find_element(By.XPATH,"//input[@class ='_8esa' and @value='1']")
print(radio.is_selected())


time.sleep(2)
driver.quit()
