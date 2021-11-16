import praw as p

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
