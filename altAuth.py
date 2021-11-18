import requests.auth


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
