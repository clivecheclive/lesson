# coding: utf-8
import pandas as pd
# from pyecharts import Bar, Line,Overlap,Geo
from pyecharts import Bar, Line,Geo
import jieba
from wordcloud import WordCloud,ImageColorGenerator
import matplotlib.pyplot as plt
from collections import Counter

love_apartment_com = pd.read_excel('爱情公寓.xls',encoding='utf-8')
# love_apartment_com = pd.read_excel('爱情公寓.xls')
grouped = love_apartment_com.groupby(['city'])
grouped_pct = grouped['score']

city_com = grouped_pct.agg(['mean', 'count'])
city_com.reset_index(inplace=True)
city_com['mean'] = round(city_com['mean'], 2)
data = [(city_com['city'][i], city_com['count'][i]) for i in range(0, city_com.shape[0])]
geo = Geo('《爱情公寓》全国热力图', title_color="#fff",title_pos="center", width=1200, height=600, background_color='#404a59')
attr, value = geo.cast(data)
geo.add("", attr, value, type="heatmap",  is_visualmap=True, visual_range=[0, 20],visual_text_color="#fff")
geo.render('爱情公寓全国观影图.html')