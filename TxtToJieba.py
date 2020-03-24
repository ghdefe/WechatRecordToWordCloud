import jieba
import wordcloud

with open('all_out.txt','r',encoding='gbk')as txt:
    txt = txt.read()
    jieba.load_userdict('user_dict.txt')
    seg_list = jieba.cut(txt)
    seg_list1 = []
    for seg in seg_list:
        if(len(seg)==1):
            continue
        seg_list1.append(seg)
    res_data = ' '.join(seg_list1)
    with open('all_jieba.txt','w')as writer:
        writer.write(res_data)