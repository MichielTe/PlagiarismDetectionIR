import pickle
import matplotlib.pyplot as plt
import math

def getData():
    with open('obj/similarity.pkl', 'rb') as file:
        data = pickle.load(file)
    return data

def main():
    data=getData()
    counted_vals=[0]*10
    names=["0-10","10-20","20-30","30-40","40-50","50-60","60-70","70-80","80-90","90-100"]
    for datapoint in data:
        val=data[datapoint]
        index=math.floor(val*10)
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