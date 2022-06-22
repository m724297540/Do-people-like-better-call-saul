# date: 6/21/2022
# author: Cheng Ma
# This script collects critic reviews of Better Call Saul Season 1-6 from Rotton Tomatoes
# output: Better_Call_Saul_Season_critic_reviews.csv


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
    items = soup.find_all('div', class_ = 'row review_table_row')
    for item in items:
        critic_name = item.find('a', class_ = 'unstyled bold articleLink critic__name').text.strip()
        critic_publication = item.find('a', class_ = 'critic__publication').text.strip()

        try:
            top_critic = item.find('rt-icon-top-critic', class_ = 'small') != None
        except:
            top_critic = False
        
        review_icon = item.find('div', class_ = 'col-xs-16 review_container').find_all('div')[0]['class'][3]

        review_quote = item.find('div', class_ = 'critic__review-quote').text.strip()
        review_link = item.find('div', class_ = 'small subtle').find('a')['href']
        date_published = item.find('div', class_ = 'critic__review-date subtle small').text.strip()

        review = {
            'critic_name' : critic_name,
            'top_critic' :  top_critic,
            'critic_publication' : critic_publication,
            'review_icon' : review_icon,
            'review_quote' : review_quote,
            'review_link' : review_link,
            'date_published' : date_published,
            'season' : season
        }
        reviews.append(review)
    return

# collect reviews from all the pages
def get_audience_reviews(season):
    url = f'https://www.rottentomatoes.com/tv/better_call_saul/s0{season}/reviews'
    driver = webdriver.Chrome()
    driver.get(url)
    time.sleep(5)
    
    while True:
        html = driver.page_source
        soup = extract(html)
        transform(soup, season)
        try:
            driver.find_element(by=By.XPATH, value='//*[@id="content"]/div/div/div/nav[1]/button[2]').click()
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
df.to_csv('Better_Call_Saul_Season_critic_reviews.csv', index = False)