import praw as p

rd = p.Reddit(user_agent='web:placetimely532:1', client_id='9EMA9bZJNOr-3jDNFPR8Ug',
              client_secret='DjcpA3XYXiO3O0eH0sEwrrF_xkzx8w', username='PlaceTimely532', password='zxh4NG4vAd7PDcp')

title = 'Wilder is amazing'
body = 'Wilder is not the best boxer. Yet, he remains an remarkable individual given his upbringing.'
rd.subreddit('boxing').submit(title=title, selftext=body)