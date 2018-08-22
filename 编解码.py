# coding: utf-8
name='语文'
f = open(name+'.csv','w')
f.write('123,语文')
f.close()
#修改编码
import codecs
f = open(unicode(name+'.csv','utf-8'),'w')  # 文件名不乱码
f.write(codecs.BOM_UTF8)  # excel打开内容不乱码的核心语句**
f.write('123,语文')
f.close()
