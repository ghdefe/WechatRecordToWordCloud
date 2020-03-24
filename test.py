import csv

with open('./111.csv','r') as csv_file:
    csv_reader = csv.DictReader(csv_file)
    for row in csv_reader:
        print(row)
        if(row['M'] == '2'):
            with open('./output.csv','w') as csv_out:
                fieldnames = ['one','two','three']
                writer = csv.DictWriter(csv_out,fieldnames)
                writer.writeheader()
                writer.writerow({'one':row[''],'two':row['N'],'three':row['M']})