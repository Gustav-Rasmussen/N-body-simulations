import requests
import pandas as pd


def get_data(file):
    github_usr = "https://raw.githubusercontent.com/Gustav-Rasmussen/"
    repo = "N-Body-Simulations/master/"
    datafiles = "textfiles/StableStructures/"
    URL = github_usr + repo + datafiles + file
    r = requests.get(URL)
    if r.status_code == 200:
        rr = r.text
        ff = [i.split(" ") for i in rr.split("\n")[:-1]]
        df = pd.DataFrame(ff).astype(float).values
        return df
    return None


if __name__ == '__main__':
    file = "A/AHQ10000G1.0_0_000.txt"
    df = get_data(file)
    print(df)
