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
driver.implicitly_wait(20)
# sleep(2)
# 找到登录连接，点击
# input1=driver.find_element_by_xpath('//*[@id="u1"]/a[7]').click()

# sleep(2)
#鼠标移入设置连接
# n=driver.find_element_by_xpath('//*[@id="u1"]/a[8]').click()
# ActionChains(n).move_to_element()

# sleep(5)
# 在弹出框找到登录连接，点击
# driver.find_element_by_xpath('//*[@id="TANGRAM__PSP_10__footerULoginBtn"]').click()

# sleep(2)
# 找到用户名输入框，输入用户名
# driver.find_element_by_xpath('//*[@id="TANGRAM__PSP_10__userName"]').send_keys('username')
#
# # 找到密码输入框，输入密码
# sleep(2)
# driver.find_element_by_xpath('//*[@id="TANGRAM__PSP_10__password"]').send_keys('password')

# 在弹出框找到qq快捷登录连接，点击
# driver.find_element_by_xpath('//*[@id="pass_phoenix_btn"]/ul/li[1]/a').click()
# driver.find_element_by_xpath('//*[@id="pass_phoenix_btn"]/ul/li[1]/a').click()

handles=driver.current_window_handle
print(handles)

# 使用js打开一个新的页签
url='https://graph.qq.com/oauth2.0/show?which=Login&display=pc&client_id=100312028&response_type=code&display=pc&state=1528199419&redirect_uri=https%3A%2F%2Fpassport.baidu.com%2Fphoenix%2Faccount%2Fafterauth%3Fmkey%3Df4147c914f20d9f47162780050f2fa2f&scope=get_user_info,get_other_info,add_t,add_share'
# js='window.open("%s");'%url
js='window.open("'+url+'");'
driver.execute_script(js)
# 新开一个页签之后，当前driver的handle不变，要操作新开页签的页面元素，必须切换driver的handle
old_handle=driver.current_window_handle
print(old_handle)

# 获取所有的页签句柄，返回值是一个元组
all_handle=driver.window_handles

print(all_handle)
# 遍历所有的页签句柄，driver切换到当前最新打开的页签的句柄
for handle in all_handle:
    if handle != old_handle:
        driver.switch_to.window(handle)
        newhandle=handle
        print(handle)

print(driver.current_window_handle)
# 点击qq图标进行登录

driver.switch_to.frame('ptlogin_iframe')
driver.find_element_by_xpath('//*[@id="img_out_55480999"]').click()
driver.switch_to.default_content()

driver.switch_to.window(old_handle)

driver.find_element_by_xpath('//*[@id="kw"]').send_keys('selenium')


# //*[@id="img_out_55480999"]
# 点击登录按钮
# driver.find_element_by_xpath('//*[@id="TANGRAM__PSP_10__submit"]').click

# 鼠标移到用户名上
# m=driver.find_element_by_xpath('//*[@id="s_username_top"]/span')
# ActionChains(m).move_to_element()
# 等待2秒




# 关闭浏览器
#driver.close()
# driver.quit()