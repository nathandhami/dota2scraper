from urllib.request import urlopen, urlretrieve
from bs4 import BeautifulSoup as soup
from dota2scrape.constants import HERO_IMAGE_URL

def downloadHeroImage(hero_name, dir=None):
    resource_file = str(hero_name) + "_full.png"
    url = HERO_IMAGE_URL + resource_file
    if (dir):
        resource_file = str(dir) + "\\" + resource_file
    
    urlretrieve(url, resource_file)

def getPage(url):
    with urlopen(url) as response:
        print(response.geturl())


    



