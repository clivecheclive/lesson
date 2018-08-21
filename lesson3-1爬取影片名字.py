import requests
from bs4 import BeautifulSoup
import codecs

# 爬取的数据为‘豆瓣电影 Top 250’的电影名
downloadURL="https://movie.douban.com/top250"

def download_page (url):
    # 设置http请求头的UA字段
    headers={
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36'
    }
    # 获取网页的内容
    data=requests.get(url,headers=headers).content
    return data

def parse_html(html):
    soup=BeautifulSoup(html,"html.parser")
    # 找到标签的class属性等于grid_view的所以ol标签
    movie_list_soup=soup.find('ol',attrs={'class':'grid_view'})
    movie_name_list=[]
    for movie_li in movie_list_soup.find_all('li'):
        # 找到存放信息的div
        detail=movie_li.find('div',attrs={'class':'hd'})
        # 找到存放title信息的span,并取它的文本信息
        movie_name=detail.find('span',attrs={'class':'title'}).getText()
        # 把电影名字，放进movie_name_list列表中
        movie_name_list.append(movie_name)


        #################### 把中文名和英文名字都打印出来##################
        # movie_names=detail.find_all('span',attrs={'class':'title'})
        # for movie_name1 in movie_names:
        #     movie_name_list.append(movie_name1.getText())
        #################### 把中文名和英文名字都打印出来##################

    # 找第二页的数据
    # 找到翻页连接'后页'的连接a标签
    next_page=soup.find('span',attrs={'class':'next'}).find('a')
    if next_page:
        # 如果没有到最后一页，则返回当前页爬到的数据和下一页的连接
        return movie_name_list,downloadURL+next_page['href']
    # 如果到了最后一页，则返回当前页爬到的数据
    return movie_name_list,None

def mian():
    url=downloadURL

    with codecs.open('movie.txt','wb',encoding='utf-8') as fp:
        while url:
            html=download_page(url)
            movies,url=parse_html(html)
            print(movies)
            fp.write(u'{movies}\n'.format(movies='\n'.join(movies)))
            # 跟下面的写法效果一样
            # fp.write(u'{abc}\n'.format(abc='\n'.join(movies)))

if __name__ == '__main__':
    mian()