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
driver.implicitly_wait(20)
sleep(2)
# 找到登录连接，点击
input1=driver.find_element_by_xpath('//*[@id="u1"]/a[7]').click()

sleep(5)
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


from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

# 显式等待5秒，每0.5秒看一下想要的控件能不能找到
locator = (By.XPATH, '//*[@id="img_out_55480999"]')
try:
    WebDriverWait(driver,15,0.5).until_not(EC.presence_of_element_located(locator))
except:
    print (driver.find_element_by_xpath('//*[@id="TANGRAM__PSP_10__footerULoginBtn"]').get_attribute('title'))


# 切换到默认的frame
# driver.switch_to.default_content()
# 切换到原始的页面的页面
driver.switch_to.window(handles[0])
print('2current_handles:',driver.current_window_handle)


# locator = (By.XPATH, '//*[@id="TANGRAM__PSP_10__footerULoginBtn"]')

# driver.find_element_by_xpath('//*[@id="kw"]').send_keys('selenium')
# driver.find_element_by_xpath('//*[@id="su"]').click()


# 鼠标移动到用户名连接上
m=driver.find_element_by_xpath('//*[@id="s_username_top"]/span')
ActionChains(driver).move_to_element(m).perform()

# 校验弹出的列表上有没有'个人中心'//*[@id="s_user_name_menu"]/div/a[1]
str=driver.find_element_by_xpath('//*[@id="s_user_name_menu"]/div/a[1]').text
print(str)
# sleep(2)
if str=="个人中心":
    print("test result:OK",str)
else:
    print("test result:FAIL",str)

# 执行js的方式打开一个页签
# url='https://graph.qq.com/oauth2.0/show?which=Login&display=pc&client_id=100312028&response_type=code&display=pc&state=1528199419&redirect_uri=https%3A%2F%2Fpassport.baidu.com%2Fphoenix%2Faccount%2Fafterauth%3Fmkey%3Df4147c914f20d9f47162780050f2fa2f&scope=get_user_info,get_other_info,add_t,add_share'
# # js='window.open("%s");'%url
# js='window.open("'+url+'");'
# driver.execute_script(js)
# # 新开一个页签之后，当前driver的handle不变，要操作新开页签的页面元素，必须切换driver的handle
# old_handle=driver.current_window_handle
# print(old_handle)

# # 遍历所有的页签句柄，driver切换到当前最新打开的页签的句柄
# for handle in all_handle:
#     if handle != old_handle:
#         driver.switch_to.window(handle)
#         newhandle=handle
#         print(handle)
# print(driver.current_window_handle)
#

# 关闭当前窗口
driver.close()

# 关闭所有窗口
driver.quit()