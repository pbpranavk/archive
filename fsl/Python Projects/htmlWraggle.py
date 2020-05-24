from bs4 import BeautifulSoup
raw_html = open('simple.html').read()

html = BeautifulSoup(raw_html, 'html.parser')

for p in html.select('p'):
    if p['id'] == 'pyth':
        print(p.text)
