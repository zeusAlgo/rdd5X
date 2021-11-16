import praw as p

map = {'clientId': '9EMA9bZJNOr-3jDNFPR8Ug', 'clientSecret': 'DjcpA3XYXiO3O0eH0sEwrrF_xkzx8w',
       'userAgent': 'web:placetimely532:1(by u/PlaceTimely532)',
       'username': 'PlaceTimely532', 'password': 'zxh4NG4vAd7PDcp'}

rd = p.Reddit(client_id=map['clientId'], client_secret=map['clientSecret'],
              user_agent=map['userAgent'], username=map['username'], password=map['password'])

readOnly = p.Reddit(client_id=map['clientId'], client_secret=map['clientSecret'], user_agent=map['userAgent'])

for idx, post in enumerate(readOnly.subreddit('boxing').hot(limit=5), 1):
    print(idx, post.title)

sub = rd.subreddit('boxing')
comments = sub.stream.comments()

for comment in comments:
    text, author = comment.body, comment.author
    if 'wilder' in text.lower():
        reply = 'Fascinating'
    comment.reply(reply)

title = 'Wilder is amazing'
body = 'Wilder is not the best boxer. Yet, he remains an remarkable individual given his upbringing.'
# rd.subreddit('boxing').submit(title=title, selftext=body)
