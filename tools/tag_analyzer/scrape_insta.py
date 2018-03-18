import instaloader
import pandas as pd
import numpy as np

def scrape(queries,limit=10000,verbose=False):
    scrape = instaloader.Instaloader()

    posts = dict()

    for query in queries:
        if verbose:
            print('Now scraping {} for "{}".'.format("Instagram",query))

        posts[query] = list()

        i = 0
        for post in scrape.get_hashtag_posts(query):
            posts[query].append(str(post.caption))

            if verbose:
                i += 1
                if i % 1000 == 0:
                    print("{} posts have been scraped so far.".format(i))
            
            if limit and i == limit:
                return posts
    return posts


