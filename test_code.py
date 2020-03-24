import numpy as np
from PIL import Image
import re
import jieba
from wordcloud import WordCloud,ImageColorGenerator,STOPWORDS
import  matplotlib.pyplot as plt

# 打开存放项目名称的txt文件
with open('all_out1.txt','r',encoding='utf-8') as f:
    word= (f.read())
    f.close()

# 图片模板和字体
#image=np.array(Image.open('ditu.jpg'))
#font=r'C:\\Windows\\fonts\\msyh.ttf'

# 去掉英文，保留中文
resultword=re.sub("[A-Za-z0-9\[\`\~\!\@\#\$\^\&\*\(\)\=\|\{\}\'\:\;\'\,\[\]\.\<\>\/\?\~\。\@\#\\\&\*\%]", "",word)
wordlist_after_jieba = jieba.cut(resultword)
wl_space_split = " ".join(wordlist_after_jieba)

# 设置停用词
sw = set(STOPWORDS)
sw.add("研发")
sw.add("系列")
sw.add("这里不多写了，根据自己情况添加")

# 关键一步
my_wordcloud = WordCloud(scale=4,font_path='CPo3HKS-Bold.otf',stopwords=sw,background_color='white',
                         ).generate(wl_space_split)

#显示生成的词云
plt.imshow(my_wordcloud)
plt.axis("off")
plt.show()

#保存生成的图片
my_wordcloud.to_file('result.jpg')