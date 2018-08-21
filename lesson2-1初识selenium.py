from selenium import webdriver
from time import sleep
# import time

# 打开浏览器
driver=webdriver.Chrome()
driver.maximize_window()
# 访问百度
driver.get('https://www.baidu.com')

# 智能等待20秒
driver.implicitly_wait(20)

# sleep(2)
# 找到搜索框，并输入python关键字
# driver.find_element_by_id('kw').send_keys('selenium')
# driver.find_element_by_css_selector('input.s_ipt').send_keys('selenium')
input1=driver.find_element_by_xpath('//*[@id="kw"]').send_keys('selenium')

# sleep(2)
# 找到搜索按钮，并点击
# driver.find_element_by_id('su').click()
# driver.find_element_by_css_selector('input.bg.s_btn').click()
driver.find_element_by_xpath('//*[@id="su"]').click()

# sleep(2)

driver.find_element_by_xpath('//*[@id="kw"]').clear()

# 等待2秒
# sleep(2)

# driver.find_element_by_xpath('//*[@id="4001"]/div[1]/h3/a[1]').click()

# sleep(2)

str=driver.find_element_by_xpath('//*[@id="4001"]/div[1]/h3/a[1]/font').text
print(str)
# sleep(2)

if str=="selenium":
    print("test result:OK")
else:
    print("test result:FAIL")
# 关闭浏览器
#driver.close()
driver.quit()