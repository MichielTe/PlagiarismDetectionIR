import math
import pickle

import matplotlib.pyplot as plt


def getData():
    """
    Loads data from either the similarityApproxyJaccard.py or the similairtyJaccard.py file
    :return:
    """
    with open('obj/similarityApprox.pkl', 'rb') as file:
        data = pickle.load(file)
    return data

def main():
    """
    Creates a bar graph of the data,
    x axis is the similarity percentage
    y axis will be the amount of document pairs that fall in the similarity percentage
    The y axis will be scaled logarithmically
    mathplotlib does not allow the creation of bar graphs where the x-axis labels are on the sections between graphs,
    This is why the x-axis contains ranges instead of single values

    :return:
    """
    data=getData()
    counted_vals=[0]*10
    names=["0-10","10-20","20-30","30-40","40-50","50-60","60-70","70-80","80-90","90-100"]
    for datapoint in data:
        val=data[datapoint]
        index=math.floor(val*10)
        # Edge condition when the similarity is 100%
        if index>=10:index=9
        counted_vals[index]+=1

    fig, ax = plt.subplots()
    for idx,i in enumerate(counted_vals):
        b = ax.bar(names[idx], i, 1)

    ax.set_yscale('log')
    ax.set_xlabel('similarity between documents (%)')
    ax.set_ylabel('Number of documents')
    plt.show()


if __name__ == "__main__":
    main()