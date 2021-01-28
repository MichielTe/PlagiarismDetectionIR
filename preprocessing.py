import csv
import pickle
import re

# Regex expression to remove all non alphabet/numbers characters
removeNonAlphabet=re.compile('[\W_]+', re.UNICODE)

def getData(file):
    data = list()
    with open(file, newline='\n', encoding="utf8") as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            data.append(sanitiseData(row["article"]))
    # save pre-processed documents to file for usages in the shingling file
    with open('obj/documents.pkl', 'wb') as file:
        pickle.dump(data, file)
    return data

def sanitiseData(data):
    """
    Sanitise data, here we will only put all letter to lowercase, and remove non alphabetic characters
    So only lowercase letters will remain
    :param data: The inital data set
    :return: the sanitised data set
    """
    splitted = data.split(" ")
    removedStopWord = [removeNonAlphabet.sub('', word).lower()
                       for word in splitted if word != ""  and not any(i.isdigit() for i in word)]

    return removedStopWord


def main():
    data = getData("data/news_articles_small.csv")

if __name__ == "__main__":
    main()
