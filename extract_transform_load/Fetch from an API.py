# In the last video, you've seen that you can extract data from an API by sending a request to the API and parsing the response which was in JSON format.
# In this exercise, you'll be doing the same by using the requests library to send a request to the Hacker News API.

# Hacker News is a social news aggregation website, specifically for articles related to computer science or the tech world in general. 
# Each post on the website has a JSON representation, which you'll see in the response of the request in the exercise.

# Instructions
# Use the requests module to get the Hacker News post's JSON object.
# Print out the response, parsed as a JSON.
# Parsing as JSON again, assign the "score" key of the post to post_score.

import requests

# Fetch the Hackernews post
resp = requests.get("https://hacker-news.firebaseio.com/v0/item/16222426.json")

# Print the response parsed as JSON
print(resp.json())

# Assign the score of the test to post_score
post_score = resp.json()["score"]
print(post_score)

{'by': 'neis', 'descendants': 0, 'id': 16222426, 'score': 17, 'time': 1516800333, 'title': 'Duolingo-Style Learning for Data Science: DataCamp for Mobile', 'type': 'story', 'url': 'https://medium.com/datacamp/duolingo-style-learning-for-data-science-datacamp-for-mobile-3861d1bc02df'}
17
