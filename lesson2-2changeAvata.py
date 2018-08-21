from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from time import sleep
import urllib.request

try:
    # url="http://www.baidu.com8/xx/xx"
    url="http://www.baidu.com"
    res=urllib.request.urlopen(url)
    print('res.code',res.code)
    print('res.reson',res.reason)
except urllib.request.URLError as e:
    if hasattr(e,'code'):
        print('e.code:',e.code)
    if hasattr(e,'reason'):
        print('e.reason:',e.reason)
    exit()



# 打开浏览器
driver=webdriver.Chrome()
driver.maximize_window()
# 访问百度
driver.get(url)
# 隐性等待
driver.implicitly_wait(10)
# sleep(2)
# 找到登录连接，点击
input1=driver.find_element_by_xpath('//*[@id="u1"]/a[7]').click()

# sleep(5)
# 在弹出框找到登录连接，点击
driver.find_element_by_xpath('//*[@id="TANGRAM__PSP_10__footerULoginBtn"]').click()

# 在弹出框找到qq快捷登录连接，点击
driver.find_element_by_xpath('//*[@id="pass_phoenix_btn"]/ul/li[1]/a').click()
driver.find_element_by_xpath('//*[@id="pass_phoenix_btn"]/ul/li[1]/a').click()

# 打印出当前的窗口句柄和所有的窗口句柄
current_handle=driver.current_window_handle
handles=driver.window_handles
print('current_handle:',current_handle)
print('all_handles:',handles)

# driver切换到弹出的qq快捷登录页的句柄
driver.switch_to.window(handles[1])

print('1current_handles:',driver.current_window_handle)
# 切换到qq登录图标所在的frame
driver.switch_to.frame('ptlogin_iframe')
# 点击qq快捷登录连接
driver.find_element_by_xpath('//*[@id="img_out_55480999"]').click()
# 点击后要等待几秒，因为该页面有一个3秒的倒计时
# sleep(5)

# 切换到默认的frame
driver.switch_to.default_content()

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

# 显式等待5秒，每0.5秒看一下想要的控件能不能找到
locator = (By.XPATH, '//*[@id="img_out_55480999"]')
try:
    WebDriverWait(driver,15,0.5).until_not(EC.presence_of_element_located(locator))
except:
    print (driver.find_element_by_xpath('//*[@id="TANGRAM__PSP_10__footerULoginBtn"]').get_attribute('title'))


# 切换到原始的页面的handle
driver.switch_to.window(handles[0])
print('2current_handles:',driver.current_window_handle)


# 显式等待5秒，每0.5秒看一下想要的控件能不能找到
locator = (By.XPATH, '//*[@id="s_username_top"]/span')
try:
    WebDriverWait(driver,15,0.5).until(EC.presence_of_element_located(locator))
except:
    print (u'找不到个人信息连接')

# 点击个人信息连接
driver.find_element_by_xpath('//*[@id="s_username_top"]/span').click()


current_handle=driver.current_window_handle
handles=driver.window_handles
print('3current_handle:',current_handle)
print('3all_handles:',handles)
print('3handle【1】:',handles[1])

# 切换到个人信息页面
driver.switch_to.window(handles[1])


# 鼠标移动到头像上
m=driver.find_element_by_xpath('//*[@id="ibx-uc"]/div/div[1]/div')
ActionChains(driver).move_to_element(m).perform()

# 点击隐藏的更换头像连接
driver.find_element_by_xpath('//*[@id="ibx-uc"]/div/div[1]/div/a').click()

current_handle=driver.current_window_handle
handles=driver.window_handles
print('3current_handle:',current_handle)
print('3all_handles:',handles)
print('3handle【2】:',handles[2])

# 切换到百度个人设置页面
driver.switch_to.window(handles[2])

driver.find_element_by_xpath('//*[@id="fileImg"]').send_keys(r'C:\Users\Bingbing.Che\Pictures\Camera Roll\1.JPG')


# 显式样等待保存图像按钮
locator = (By.XPATH, '//*[@id="savePortrait"]')
try:
    WebDriverWait(driver,20,0.5).until(EC.visibility_of_element_located(locator))
except:
    print (u'')


sleep(6)
#点击保存图像按钮
driver.find_element_by_xpath('//*[@id="savePortrait"]').click()
# 关掉前一个页面
# driver.close()
#
#
# driver.quit()