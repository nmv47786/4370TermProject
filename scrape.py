import requests
from bs4 import BeautifulSoup
import re
import pandas as pd
import numpy as np
from PIL import Image
from fake_useragent import UserAgent

ua = UserAgent()
print(ua.chrome)
header = {'User-Agent':str(ua.chrome)}
#print(header)

URL = "https://www.imdb.com/title/tt3783958/"
#URL + "tt3783958"
page = requests.get(URL, headers=header)
soup = BeautifulSoup(page.content, "html.parser")
results = soup.find("class"=="ipc-page-content-container ipc-page-content-container--full sc-5c7dd5e4-0 iRUEko")
#print(results.prettify())
#movie = soup.find("a"=="ipc-lockup-overlay ipc-focusable")
#print(movie.prettify())

movie_elements = results.find_all("div", class_="sc-9497c711-2 boaMFA")
#ipc-poster ipc-poster--baseAlt ipc-poster--dynamic-width sc-d383958-0 gvOdLN celwidget ipc-sub-grid-item ipc-sub-grid-item--span-2
#ipc-media ipc-media--poster-27x40 ipc-image-media-ratio--poster-27x40 ipc-media--baseAlt ipc-media--poster-l ipc-poster__poster-image ipc-media__img
#ipc-media ipc-media--poster-27x40 ipc-image-media-ratio--poster-27x40 ipc-media--baseAlt ipc-media--poster-l ipc-poster__poster-image ipc-media__img
for movie_element in movie_elements:
    description_element = movie_element.find("span", class_="sc-16ede01-0 fMPjMP")
    #description_element = movie_element.find("div", class_="ipc-html-content-inner-div")
    img_element = movie_element.find("a", class_="ipc-lockup-overlay ipc-focusable")
    video_element = movie_element.find("video", class_="jw-video jw-reset")
    rating_element = movie_element.find("span", class_="sc-7ab21ed2-1 jGRxWM")
    genre_element = movie_element.find("ul", class_="ipc-inline-list ipc-inline-list--show-dividers ipc-inline-list--inline ipc-metadata-list-item__list-content base")

    #k = img_element.indexOf("href")
    print(description_element)
    print(img_element)
    print(video_element)
    print(rating_element)

    print(genre_element)
    print()

#
#link = 'https://www.imdb.com/title/'
#for i in image_url_arr[link + 'tt0088172']:
#    r = requests.get(i)
#    soup = BeautifulSoup(r.content, "html.parser")
#    try:
#      image_url = page_html.find('div', class_='poster').img['src']
#    except:
#      image_url = np.nan
#    images.append(image_url)
#
#im = Image.open(r'images[0]')
#im.show()
