

def get_data():
    URL = "https://github.com/Gustav-Rasmussen/N-Body-Simulations/tree/master/textfiles/StableStructures"
    r = requests.get(URL)
    if r.status_code == 200:
        return r.json()
    return None


if __name__ == '__main__':
    get_data()
