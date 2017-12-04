import csv

def clean_data(infile, outfile, endcol=6):
    with open(infile, 'r', encoding='utf-8') as inf, open(outfile, 'w', encoding='utf-8', newline='') as outf:
        incsv = csv.reader(inf)
        outcsv = csv.writer(outf)
        headline = next(incsv)
        outcsv.writerow(headline)

        for line in incsv:
            not_none = True
            for item in line[:endcol]:
                if item == '':
                    not_none = False

            if not_none:
                outcsv.writerow(line)

if __name__ == '__main__':
    infile = '../data/Artists.csv'
    outfile = '../data/cleaned_artists.csv'
    clean_data(infile, outfile)
