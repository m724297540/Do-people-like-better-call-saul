# date: 6/21/2022
# author: Cheng Ma
# This script collects audiance reviews of Better Call Saul Season 1-6 from Rotton Tomatoes
# output: Better_Call_Saul_Season_audience_reviews.csv


import requests
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import time
import pandas as pd

def extract(html):
    soup = BeautifulSoup(html, 'html.parser')
    return soup

# collect reviews from a certain page
def transform(soup, season):
    items = soup.find_all('li', class_ = 'audience-reviews__item')
    for item in items:
        user_name = item.find('a')['href']
        rating_stars = len(item.find_all('span', class_ = 'star-display__filled')) + 0.5 * len(item.find_all('span', class_ = 'star-display__half'))
        review_text = item.find('p', class_ = 'audience-reviews__review--mobile js-review-text clamp clamp-4 js-clamp').text.strip()
        date_published = item.find('span', class_ = 'audience-reviews__duration').text.strip()
        review = {
            'user_name' : user_name,
            'rating_stars' : rating_stars,
            'review_text' : review_text,
            'date_published' : date_published,
            'season' : season
        }
        reviews.append(review)
    return

# collect reviews from all the pages
def get_audience_reviews(season):
    url = f'https://www.rottentomatoes.com/tv/better_call_saul/s0{season}/reviews?type=user'
    driver = webdriver.Chrome()
    driver.get(url)
    time.sleep(5)
    
    while True:
        html = driver.page_source
        soup = extract(html)
        transform(soup, season)
        try:
            driver.find_element(by=By.XPATH, value='//*[@id="content"]/div/div/nav[3]/button[2]').click()
            time.sleep(5)
        except:
            break
    driver.close()
    return

# collect reviews of Better Call Saul Season 1 - 6
reviews = []

for season in range(1,7):
    get_audience_reviews(season)

df = pd.DataFrame(reviews)
df.to_csv('Better_Call_Saul_audience_reviews.csv', index = False)