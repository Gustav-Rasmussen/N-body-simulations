import requests
import pandas as pd


def get_data(file):
    usr = "https://raw.githubusercontent.com/Gustav-Rasmussen/"
    repo = "N-Body-Simulations/master/"
    datafiles = "textfiles/StableStructures/"
    URL = usr + repo + datafiles + file
    r = requests.get(URL)
    if r.status_code == 200:
        list_of_strings = [i.split(" ") for i in r.text.split("\n")[:-1]]
        array = pd.DataFrame(list_of_strings).astype(float).values
        return array
    return None


if __name__ == '__main__':
    file = "A/AHQ10000G1.0_0_000.txt"
    array = get_data(file)
    print(array)
    # print(array[0])  # 1.st row
    # print(array[:, 3])  # 4.th column
