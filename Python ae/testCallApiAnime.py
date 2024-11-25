import requests

resp = requests.get("https://nekos.best/api/v2/neko")
data = resp.json()
print(data["results"][0]["url"])

# https://nekos.best/api/v2/neko/0001.png
