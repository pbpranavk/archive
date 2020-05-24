def fetch(url):
    return requests.get(url)

def fetch_all(url):
    with multiprocessing.Pool() as pool:
        results = pool.map(fetch, urls)