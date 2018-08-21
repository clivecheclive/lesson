from support  import login
from support  import search
from support  import change_avata
from selenium import webdriver

url="http://www.baidu.com"

driver=webdriver.Chrome()
search(url,driver,'autoTest')
driver.quit()

driver=webdriver.Chrome()
login(url,driver)
driver.quit()

driver=webdriver.Chrome()
change_avata(url,driver,r'C:\Users\Bingbing.Che\Pictures\Camera Roll\1.JPG')
driver.quit()