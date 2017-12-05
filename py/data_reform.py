import csv
import json

with open('../data/cleaned_artworks.csv', 'r', encoding='utf-8') as f:
    incsv = csv.reader(f)
    next(incsv)
    data = []
    for line in incsv:
        title = line[0]
        date = line[8]
        if len(date) != 4:
            continue
        temp = {'name': title, 'data': [date]}
        data.append(temp)

f = open('../data/artworks.json', 'w', encoding='utf-8')
json.dump(data, f)
f.close()
