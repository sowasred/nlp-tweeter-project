# textblob and tweepy were installed globally(not sure globally but with pip for sure)
# if you have multiple version of python in your pc, specify as following which module are you gonna install
# python -m pip install tweepy matplotlib textblob

from textblob import TextBlob
import sys, tweepy
import matplotlib.pyplot as plt


def percentage(part, whole):
    return 100 * float(part)/float(whole)


consumerKey = '100juqMSRXMi0RL35Barcyk3r'
consumerSecret = 'a5H4h3vVJulI02Ege4AE6gVxAud2LQysHsNTn7eudwC1ZrkfbA'
accessToken = '507832449-tMlg6VZderSdDT3fbn1BIbvSGxQbHv9c69sNUO6R'
accessTokenSecret = 'wcKaAIFeNGtfhuGZj1gYU6E8kg5bwzwCh3NKZZaOm3wwz'


auth = tweepy.OAuthHandler(consumerKey, consumerSecret)
auth.set_access_token(accessToken, accessTokenSecret)
api = tweepy.API(auth)


searchTerm = input('Enter keyword/hashtag to search about: ')
noOfSearchTerms = int(input('Enter how many tweets to analyze:'))                      
                      
                      
tweets = tweepy.Cursor(api.search, q=searchTerm, lang = "en").items(noOfSearchTerms)

positive = 0
negative = 0
neutral = 0
polarity = 0

for tweet in tweets:
                     #print(tweet.text)
                     analysis = TextBlob(tweet.text)
                     polarity += analysis.sentiment.polarity
                     if(analysis.sentiment.polarity == 0):
                          neutral += 1
                     elif(analysis.sentiment.polarity < 0):
                          negative += 1
                     elif(analysis.sentiment.polarity > 0):
                          positive += 1

positive = percentage(positive, noOfSearchTerms)
neutral = percentage(neutral, noOfSearchTerms)
negative = percentage(negative, noOfSearchTerms)
polarity = percentage(polarity, noOfSearchTerms)

positive = format(positive, '.2f')
neutral = format(neutral, '.2f')
negative = format(negative, '.2f')


print('How people are reacting on ' + searchTerm + ' by analyzing ' + str(noOfSearchTerms) + ' Tweets.')

if(polarity == 0):
    print('Neutral')
elif(polarity < 0.00):
    print('Negative')
elif(polarity > 0.00):
    print('Positive')

labels = ['Positive[' + str(positive) +'%]','Neutral[' + str(neutral) +'%]', 'Negative[' + str(negative) +'%]']
sizes = [positive, neutral, negative]
colors = ['green','gold','red']
patches, texts = plt.pie(sizes, colors=colors, startangle=90)
plt.legend(patches, labels, loc="best")
plt.title('How people are reacting on ' + searchTerm + ' by analyzing ' + str(noOfSearchTerms) + ' Tweets.')
plt.axis('equal')
plt.tight_layout()
plt.show()

                      
                      




                      
                      
