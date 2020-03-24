import wordcloud
import numpy as np
from PIL import Image
from wordcloud import ImageColorGenerator
with open('all_jieba.txt','r')as f:
    f = f.read()
    with open('stop_word.txt','r')as temp:
        temp = temp.read()
    stop_wd = temp
    stop_wd += ''

    mask = np.array(Image.open('heart.png'))
    genclr = ImageColorGenerator(mask)
    word_pic = wordcloud.WordCloud(font_path='CPo3HKS-Bold.otf',
                                   background_color='pink',
                                   scale=7,
                                   #min_font_size=1,
                                   #max_font_size=10,
                                   stopwords=stop_wd,
                                   max_words=1000,
                                   mode='RGB',
                                   collocations=False,  #不重复
                                   mask = mask,
                                   color_func=genclr

                                   )
    word_pic.generate(f)
    word_pic.to_file('all_out.png')
