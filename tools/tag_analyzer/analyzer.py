import scrape_insta
import scrape_tweet
import cloud

class Analyzer:
    def scrape(self,queries,solver="twitter",limit=10000,wordcloud=True,verbose=False):
        if solver == "instagram":
            posts = scrape_insta.scrape(queries,limit,verbose)
        elif solver == "twitter":
            posts = scrape_tweet.scrape(queries,limit,verbose)
        return posts


s = Analyzer().scrape(["juletræ"],solver="instagram",limit=500,verbose=True)
print(s)