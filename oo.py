import praw as p
import requests.auth

"""""
client_auth = requests.auth.HTTPBasicAuth('9EMA9bZJNOr-3jDNFPR8Ug', 'DjcpA3XYXiO3O0eH0sEwrrF_xkzx8w')
post_data = {"grant_type": "password", "username": "PlaceTimely532", "password": "zZEKHwSTzDgCCq9"}
headers = {"User-Agent": "web:placetimely532:1(by u/PlaceTimely532)"}
response = requests.post("https://www.reddit.com/api/v1/access_token", auth=client_auth, data=post_data,
                         headers=headers)
response.json()
print(response.json())
headers = {"Authorization": "bearer 1293885880213-w0vPtPUl0yNL8xFu0cbO4FAx8uxCZw",
           "User-Agent": "web:placetimely532:1(by u/PlaceTimely532)"}
response1 = requests.get("https://oauth.reddit.com/api/v1/me", headers=headers)
response1.json()
"""""
map = {'clientId': '9EMA9bZJNOr-3jDNFPR8Ug', 'clientSecret': 'DjcpA3XYXiO3O0eH0sEwrrF_xkzx8w',
       'userAgent': 'web:placetimely532:1(by u/PlaceTimely532)',
       'username': 'PlaceTimely532', 'password': 'zZEKHwSTzDgCCq9'}

rd = p.Reddit(client_id=map['clientId'], client_secret=map['clientSecret'],
              user_agent=map['userAgent'], username=map['username'], password=map['password'])
sub = rd.subreddit('boxing')

readOnly = p.Reddit(client_id=map['clientId'], client_secret=map['clientSecret'], user_agent=map['userAgent'])

for idx, post in enumerate(readOnly.subreddit('boxing').hot(limit=5), 1):
    print(idx, post.title)

for comment in sub.comments(limit=10):
    print(comment.body)

for post in rd.subreddit('boxing').stream.submissions():
    post.reply('Intriguing perspective')
