import time

from selenium import webdriver

driver=webdriver.Chrome(executable_path="F:\pycharm\drivers\chromedriver.exe")
driver.get("https://www.amazon.in/")
driver.maximize_window()

#capture all cookies created by browser
cookies = driver.get_cookies()
print(len(cookies))
print(cookies)

#add cookies to browser

cookies2= {'name':'Mycookie','value':'5458945'}
driver.add_cookie(cookies2)

cookies = driver.get_cookies()
print(len(cookies))
print(cookies)

#delete cookie
driver.delete_all_cookies()
cookie= driver.get_cookies()
print(len(cookie))
print(cookie)








time.sleep(3)
driver.close()