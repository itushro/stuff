import pandas as pd
import matplotlib.pyplot as plt
from wordcloud import WordCloud

for place in places:
    df_tweets = pd.read_pickle("../data/derived/tweets_terms_{}.pd".format(place))
    df_instas = pd.read_pickle("../data/derived/instas_terms_{}.pd".format(place))

    df = pd.concat([df_tweets,df_instas])
    term_freq = dict(zip(df["term"],df["count"]))

    for key in term_freq.keys():
        if len(key) < 2:
            term_freq[key] = 0

    print("Now {}.".format(place))

    wc = WordCloud(background_color="white", max_words=100, mask=None,
                   stopwords=None, max_font_size=250, random_state=None,
                   width=1920, height=1080)

    wc.generate_from_frequencies(term_freq)

    plt.imshow(wc, interpolation="bilinear")
    plt.axis("off")
    plt.savefig("{}.png".format(place),dpi=1000)
#plt.show()