import requests

url = "https://www.reddit.com/r/funny/.json"
headers = {"User-Agent": "Mozilla/5.0"}

response = requests.get(url, headers=headers)

if response.status_code == 200:
    data = response.json()
    posts = data['data']['children']
    
    for post in posts:
        title = post['data']['title']
        link = post['data']['url']
        print(f"Title: {title}")
        print(f"Link: {link}")
        print()
else:
    print(f"Failed to fetch: {response.status_code}")
