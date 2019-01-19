import csv

with open('data/books.csv','r',encoding='gbk') as rf:
    reader = csv.reader(rf,dialect=csv.excel)
    for row in reader:
        print('|'.join(row))
