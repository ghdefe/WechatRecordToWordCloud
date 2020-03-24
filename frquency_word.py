import jieba
import csv
txt = open("all_out.txt", "r").read()
words  = jieba.lcut(txt)
counts = {}
for word in words:
    if len(word) == 1:  #排除单个字符的分词结果
        continue
    else:
        counts[word] = counts.get(word,0) + 1
items = list(counts.items())
items.sort(key=lambda x:x[1], reverse=True)
for i in range(1000):
    word, count = items[i]
    print ("{0:<10}{1:>5}".format(word, count))
with open('frequency.csv','w')as writer:
    cw = csv.writer(writer,lineterminator = '\n')

    cw.writerows(items)
#把这个写入csv


