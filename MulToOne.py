import csv

csv.field_size_limit(500 * 1024 * 1024)
with open('./output.csv', 'w', encoding='gbk', errors='ignore',newline='') as csv_out:
    fieldnames = ['isSend', 'createTime', 'content']
    writer = csv.DictWriter(csv_out, fieldnames)
    writer.writeheader()

with open('./11111.csv','r',encoding = 'gbk',errors='ignore',newline='') as csv_file:   #代提取文件
    csv_reader = csv.DictReader(csv_file)
    for row in csv_reader:
        #print(row['content'])
        if(row['type']=='1'):   #消息类型
            if(row['talker']=='wxid_pa7yyh5lv5ut22'):   #消息人
                print(row['content'])
                with open('./output.csv','a',encoding = 'gbk',errors='ignore',newline='') as csv_out:
                    fieldnames = ['isSend','createTime','content']
                    writer = csv.DictWriter(csv_out,fieldnames)
                    writer.writerow({'isSend':row['isSend'],'createTime':row['createTime'],'content':row['content']})