import praw as p
hashmap = {'clientId': '9EMA9bZJNOr-3jDNFPR8Ug', 'clientSecret': 'DjcpA3XYXiO3O0eH0sEwrrF_xkzx8w',
           'userAgent': 'web:placetimely532:1(by u/PlaceTimely532)',
           'username': 'PlaceTimely532', 'password': 'zxh4NG4vAd7PDcp'}

rd = p.Reddit(client_id=hashmap['clientId'], client_secret=hashmap['clientSecret'],
              user_agent=hashmap['userAgent'],
              username=hashmap['username'], password=hashmap['password'])

readOnly = p.Reddit(client_id=hashmap['clientId'], client_secret=hashmap['clientSecret'],
                    user_agent=hashmap['userAgent'])

for idx, post in enumerate(readOnly.subreddit('boxing').hot(limit=5), 1):
    print(idx, post.title)


title = 'Wilder is amazing'
body = 'Wilder is not the best boxer. Yet, he remains an remarkable individual given his upbringing.'
# rd.subreddit('boxing').submit(title=title, selftext=body)

# print(rd.read_only)

# for post in rd.subreddit('boxing').hot(limit=3):
#     print(post.title)
