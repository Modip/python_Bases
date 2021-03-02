import csv

with open('google_stock_data.csv', 'r') as file :
    dialect = csv.Sniffer().sniff(file.readline())
    file.seek(0)
    datas = list(csv.reader(file,dialect=dialect))
print(datas[:5])

listDate = [mor[0] for mor in datas]

print('\n -----------\n')
print(listDate[:15])
print('\n -----------\n')

print(datas[0:1])