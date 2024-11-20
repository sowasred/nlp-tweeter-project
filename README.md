# Tweet Analysis with TextBlob and Tweepy

This Python script uses the TextBlob library for sentiment analysis of tweets retrieved using the Tweepy library. The script calculates the percentage of positive, negative, and neutral tweets based on user input keywords or hashtags.

## Prerequisites

- Install Python 3.x
- Create a Twitter Developer Account to get API keys (consumerKey, consumerSecret, accessToken, accessTokenSecret)
- Install the required libraries: textblob and tweepy

## Installation

1. Install Python 3.x on your system if it's not already installed. You can download it from [python.org](https://www.python.org/downloads/).

2. Create a Twitter Developer Account to obtain API keys (consumerKey, consumerSecret, accessToken, accessTokenSecret) by following the instructions on [developer.twitter.com](https://developer.twitter.com/en/apps).

3. Install the required libraries: textblob and tweepy using pip:

```shell
pip install textblob tweepy matplotlib
```

## Usage

1. Replace the API keys in the script with your own Twitter Developer Account credentials.
2. Run the Python script using your preferred method (Python IDE, terminal, etc.).
3. Enter the keyword or hashtag to search about and the number of tweets to analyze when prompted.
4. The script will display a pie chart showing the percentage of positive, negative, and neutral tweets based on the analysis.

## Customization

- You can customize the script by modifying the sentiment analysis logic and adjusting the visualization options.
