import requests


def get_data(file):
    github_usr = "https://github.com/Gustav-Rasmussen/"
    repo = "N-Body-Simulations/tree/master/"
    datafiles = "textfiles/StableStructures/"

    URL = github_usr + repo + datafiles + file

    r = requests.get(URL)
    if r.status_code == 200:
        return r.json()
    return None


if __name__ == '__main__':
    file = "A/AHQ10000G1.0_0_000.txt"
    get_data(file)
