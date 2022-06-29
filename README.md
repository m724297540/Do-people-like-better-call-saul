# Do People Like Better Call Saul?
## Data
1. [web_scraping_audience_reviews.py](https://github.com/m724297540/How-good-is-Better-Call-Saul/blob/master/web_scraping_audiance_reviews.py) 
and [web_scraping_audience_reviews.py](https://github.com/m724297540/How-good-is-Better-Call-Saul/blob/master/web_scraping_critic_reviews.py) 
collect audience reviews and critic reviews from Rotten Tomatoes using *selenium* and *Beautifulsoup*. Reviews are collected on 6/21/2022.

2. The collected reviews are saved in the following two csv files:
[Better_Call_Saul_audience_reviews.csv](https://github.com/m724297540/How-good-is-Better-Call-Saul/blob/master/Better_Call_Saul_audience_reviews.csv) and 
[Better_Call_Saul_critic_reviews.csv](https://github.com/m724297540/How-good-is-Better-Call-Saul/blob/master/Better_Call_Saul_critic_reviews.csv).

## Data preparation
1. [prepare_audience_reviews.py](https://github.com/m724297540/How-good-is-Better-Call-Saul/blob/master/prepare_audience_reviews.py) and 
[prepare_critic_reviews.py](https://github.com/m724297540/How-good-is-Better-Call-Saul/blob/master/prepare_critic_reviews.py) prepare data for later analysis.
The preparation includes following steps:
- check for missing values
- expand contractions
- remove non-English reviews
- tokenization
- covert to lower case
- remove punctuations
- remove stopwords
- lemmatization

2. The prepared reviews are saved in the following csv files:
[BCS_processed_audience_reviews.csv](https://github.com/m724297540/How-good-is-Better-Call-Saul/blob/master/BCS_processed_audience_reviews.csv) and 
[BCS_processed_critic_reviews.csv](https://github.com/m724297540/How-good-is-Better-Call-Saul/blob/master/BCS_processed_critic_reviews.csv).

## Review analysis
1. [EDA_audience_reviews.ipynb](https://github.com/m724297540/How-good-is-Better-Call-Saul/blob/master/EDA_audience_reviews.ipynb) explores the following
about the audience reviews:
- Sentiment analysis: how do people like this TV show?
- How much would people like to share?
- Term frequency analysis
- Topic modeling
- Which season do people like the most?

2. [EDA_critic_reviews.ipynb](https://github.com/m724297540/How-good-is-Better-Call-Saul/blob/master/EDA_critic_reviews.ipynb) explores the following
about the critic reviews:
- Sentiment analysis: how do critics like this TV show?
- Term frequency analysis
- Topic modeling
- Which season do critics like the most?
