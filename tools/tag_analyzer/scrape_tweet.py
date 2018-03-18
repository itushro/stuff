import twitterscraper
import pandas as pd
import datetime as dt

def scrape(queries,limit=10000,verbose=False):
    if __name__ == '__main__':
        posts = dict()

        for query in queries:
            if verbose:
                print('Now scraping {} for "{}".'.format("Twitter",query))
            
            tweets = twitterscraper.query_tweets(query,
                                                 begindate=dt.date(2006,3,1),
                                                 enddate=dt.date.today(),
                                                 limit=limit,
                                                 poolsize=1)

            posts[query] = [tweet.text for tweet in tweets]
    return posts
    
