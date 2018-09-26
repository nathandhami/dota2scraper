from dota2scrape import scraper
from dota2scrape.constants import HERO_NAMES
import os

IMAGES_FOLDER = "images"
 
def downloadAllHeroImages(directory=None):
    for hero in HERO_NAMES:
         scraper.downloadHeroImage(hero, directory)

def createDirectory(directory):
    try:
        if not os.path.exists(directory):
            os.makedirs(directory)
    except OSError:
        print ('Error creating directory ' + directory)

if __name__ == "__main__":
    createDirectory(IMAGES_FOLDER)
    downloadAllHeroImages(IMAGES_FOLDER)