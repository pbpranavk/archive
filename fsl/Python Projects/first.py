from requests import get
from requests.exceptions import RequestException
from contextlib import closing
from bs4 import BeautifulSoup


def getHtmlXml(url):
    try:
        with closing(get(url,stream = True)) as resp:
            if is_good_response(resp):
                return resp.content
            else:
                return None
    except RequestException as e:
        print("Error is " + str(e));

def is_good_response(resp):
    content_type = resp.headers['Content-Type'].lower()
    return(resp.status_code == 200
            and content_type is not None
            and content_type.find('html') > -1
            )

if __name__ == "__main__" :
    print("Enter the url which you want to scrape")
    url = input()
    print(getHtmlXml(url))
