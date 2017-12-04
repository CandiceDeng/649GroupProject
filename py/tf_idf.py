import re
import csv
import nltk
import math
import json
from nltk.corpus import stopwords
from collections import Counter

def load_data(file):
    with open(file, 'r', encoding='utf-8') as f:
        incsv = csv.reader(f)
        next(incsv)

        data = {}

        for line in incsv:
            title = line[0]
            clf = line[13]

            if title is None or clf is None:
                continue

            if clf in data:
                data[clf].append(title)
            else:
                data[clf] = [title]

        return data

def word_freq(data):
    stop_words = set(stopwords.words('english'))

    word_freq_dict = {}

    for clf, titles in data.items():
        word_list = []
        for title in titles:
            words = nltk.word_tokenize(title)
            words = [w.lower() for w in words if w.lower() not in stop_words]
            filtered_words = [w for w in words if re.match(r'[a-zA-Z]', w)]
            word_list.extend(filtered_words)
        freq = Counter(word_list)
        word_freq_dict[clf] = dict(freq)

    return word_freq_dict

def tf_idf_calculator(data):
    doc_num = len(data)
    doc_freq = {}
    result = {}

    for words in data.values():
        for word in words.keys():
            if word in doc_freq:
                doc_freq[word] += 1
            else:
                doc_freq[word] = 1

    for key, value in data.items():
        tf_idf = {}

        for word, freq in value.items():
            tf = math.log(freq + 1)
            idf = math.log(doc_num / doc_freq[word]) + 1
            tf_idf[word] = tf * idf

        # tf_idf = sorted(tf_idf.items(), key=lambda x: x[1], reverse=True)
        result[key] = tf_idf

    return result

if __name__ == '__main__':
    data = load_data('../data/Artworks.csv')
    dic = word_freq(data)
    tf_idf = tf_idf_calculator(dic)
    f = open('../data/tf_idf.json', 'w', encoding='utf-8')
    json.dump(tf_idf, f)

