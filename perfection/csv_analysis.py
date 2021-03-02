import os

def lunch_analysis(data_file):
    directory = os.path.dirname(__file__)
    path_to_file = os.path.join(directory, "data", data_file)
    with open(path_to_file, 'r') as file:
        preview = file.readline()
    print("lire le ficier csv. Voici la ligne preview {}".format(preview))

def main():
    lunch_analysis('google_stock_data.csv')

if __name__ =="__main__":
    main()