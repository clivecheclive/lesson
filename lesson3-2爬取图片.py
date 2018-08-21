import requests
from bs4 import BeautifulSoup
import os

# 爬取的数据为‘斗鱼’直播的图片连接
downloadURL='https://www.douyu.com/directory/all'

headers={
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36'
}
# 获取网页的内容
data=requests.get(downloadURL,headers=headers).content

soup=BeautifulSoup(data,"html.parser")
# 找含有data-original标签的数据
img=soup('img',{'data-original':True})


if not os.path.exists('d:/testpythonIMG1/'):
    os.makedirs('d:/testpythonIMG1/')

for i in img:
    # 打印图片的url
    url=i['data-original']
    print (i['data-original'])

    # a=os.path.splitext(url)[1]

    file_name = url.split('/')[-1]

    print (file_name)
    data=requests.get(url,headers=headers).content
    with open("d:/testpythonIMG1/"+file_name+".jpg","wb") as file:
        file.write(data)