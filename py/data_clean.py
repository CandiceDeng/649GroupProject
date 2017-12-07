import csv

def clean_data(infile, outfile, endcol=6):
    nation_2_country = {}
    with open('../data/demonyms.csv', 'r', encoding='utf-8') as f:
        csvf = csv.reader(f)
        for line in csvf:
            nation_2_country[line[0]] = line[1]

    with open(infile, 'r', encoding='utf-8') as inf, open(outfile, 'w', encoding='utf-8', newline='') as outf:
        incsv = csv.reader(inf)
        outcsv = csv.writer(outf)
        headline = next(incsv)
        outcsv.writerow(headline)

        for line in incsv:
            # Nationality, gender, date, url
            # print(line[18])
            if line[4] == '()' or line[7] == '()' or line[8] == 'Unknown' or line[8] == 'n.d.' or 'http' not in line[18]:
                continue

            nations = line[4].replace(')', ' ').replace('(', '')
            nations = nations.split()

            try:
                nation = nations[0]
                country = nation_2_country[nation]
            except:
                continue

            gender = line[7].split(')')[0].replace('(', '')

            outlist = line[:4] + [country] + line[5:7] + [gender] + line[8:]
            outcsv.writerow(outlist)



if __name__ == '__main__':
    infile = '../data/Artworks.csv'
    outfile = '../data/cleaned_artworks.csv'
    clean_data(infile, outfile)
