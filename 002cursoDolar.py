import requests

def get_rate():
    url = "https://dolarapi.com/v1/dolares/oficial"
    response = requests.get(url)
    data = response.json()
    return data["venta"]

def usd_to_pesos(usd):
    rate = get_rate()
    return usd * rate

def pesos_to_usd(pesos):
    rate = get_rate()
    return pesos / rate

print(usd_to_pesos(100))
print(pesos_to_usd(150000))