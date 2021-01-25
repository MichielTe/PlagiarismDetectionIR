import csv
import pickle
import re

# Regex expression to remove all non alphabet/numbers characters
removeNonAlphabet=re.compile('[\W_]+', re.UNICODE)

def sanitiseData(data):
    splitted = data.split(" ")
    removedStopWord = [removeNonAlphabet.sub('', word).lower()
                       for word in splitted if word != ""  and not any(i.isdigit() for i in word)]

    return removedStopWord

def getData():
    data = list()
    with open('data/news_articles_small.csv', newline='\n', encoding="utf8") as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            data.append(sanitiseData(row["article"]))
    return data


def main():
    data = getData()
    # save pre-processed documents to file
    with open('obj/documents.pkl', 'wb') as file:
        pickle.dump(data, file)
    return 0


if __name__ == "__main__":
    main()
