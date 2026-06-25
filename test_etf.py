import requests

API_KEY = "d8ukacpr01qrt65s4dpgd8ukacpr01qrt65s4dq0"
url = f"https://finnhub.io/api/v1/quote?symbol=GLD&token={API_KEY}"

response = requests.get(url)
data = response.json()
print(data)

