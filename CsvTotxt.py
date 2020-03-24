import csv

with open('output.csv','r',encoding = 'gbk',errors='ignore',newline='') as csv_file:
    csv_reader = csv.DictReader(csv_file)
    temp_txt = []
    for row in csv_reader:

            #print(row)
        temp_txt.append(row['content']+'\n')
    with open('all_out.txt','w',encoding = 'gbk') as txt_file:
        for row in temp_txt:
            txt_file.write(row)