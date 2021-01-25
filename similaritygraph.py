import pickle

def getData():
    with open('obj/documents.pkl', 'rb') as file:
        data = pickle.load(file)
    return data

def main():
    data = getData()
    return 0

if __name__ == "__main__":
    main()