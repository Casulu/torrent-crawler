import requests
from bs4 import BeautifulSoup


# titleLinks = True returnerar ändast länkar med titelattribut. Returnerar även titeln med länken
def getLinks(url, titlelinks=False):
    linkpairs = {}                                          # Dict med titel på länken och länken
    response = requests.get(url)                            # HTML data
    soup = BeautifulSoup(response.text, 'html.parser')      # Parsad data
    if titlelinks:
        for currTag in soup.findAll('a', recursive=True):   # Loopar igenom alla a-taggar på sidan
            if 'title' in currTag.attrs:                    # Om a-taggen har en titel-attribut
                linkpairs[currTag['title']] = currTag['href']

    else:
        i = 0
        for currTag in soup.findAll('a', recursive=True):
            linkpairs[i] = currTag['href']
            i = i + 1

    return linkpairs
