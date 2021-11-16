import praw as p
import requests
import requests.auth
from urllib.parse import quote_plus

map = {'clientId': '9EMA9bZJNOr-3jDNFPR8Ug', 'clientSecret': 'DjcpA3XYXiO3O0eH0sEwrrF_xkzx8w',
       'userAgent': 'web:placetimely532:1(by u/PlaceTimely532)',
       'username': 'PlaceTimely532', 'password': 'zxh4NG4vAd7PDcp'}

client_auth = requests.auth.HTTPBasicAuth('9EMA9bZJNOr-3jDNFPR8Ug', 'DjcpA3XYXiO3O0eH0sEwrrF_xkzx8w')
post_data = {"grant_type": "password", "username": "PlaceTimely532", "password": "zxh4NG4vAd7PDcp"}
headers = {"User-Agent": "web:placetimely532:1(by u/PlaceTimely532)"}
response = requests.post("https://www.reddit.com/api/v1/access_token", auth=client_auth, data=post_data,
                         headers=headers)
response.json()

rd = p.Reddit(client_id=map['clientId'], client_secret=map['clientSecret'],
              user_agent=map['userAgent'], username=map['username'], password=map['password'])

readOnly = p.Reddit(client_id=map['clientId'], client_secret=map['clientSecret'], user_agent=map['userAgent'])

for idx, post in enumerate(readOnly.subreddit('boxing').hot(limit=5), 1):
    print(idx, post.title)

sub = rd.subreddit('boxing')

rd1 = p.Reddit(client_id=map['clientId'], client_secret=map['clientSecret'], password=map['password'],
               user_agent=map['userAgent'], username=map['username'])

# rd2 = p.Reddit(user_agent=map['userAgent'], client_id=map['clientId'], client_secret=map['clientSecret'],
#                username=map['username'], password=map['password'])
#
# for post in rd2.subreddit('boxing').stream.submissions():
#     post.reply('Fascinating')
#     print('x')

for comment in readOnly.subreddit('boxing').comments(limit=10):
    print(comment.body)

print(sub.display_name)
comments = sub.stream.comments()
print(rd.read_only)

# for comment in comments:
#     text, author = comment.body, comment.author
#     if 'wilder' in text.lower():
#         reply = 'Fascinating'
#     comment.reply(reply)

title = 'Wilder is amazing'
body = 'Wilder is not the best boxer. Yet, he remains an remarkable individual given his upbringing.'
# rd.subreddit('boxing').submit(title=title, selftext=body)
