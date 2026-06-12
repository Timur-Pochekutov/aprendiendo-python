import requests
import tkinter as tk

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

def convert_to_pesos(event=None):
        try:
            amount = float(entry.get())
            pesos = usd_to_pesos(amount)
            result.config(text=f"{pesos} pesos")
        except:
            result.config(text="Ingresa un numero valido")

def convert_to_usd(event=None):
     try:
          amount = float(entry.get())
          usd = pesos_to_usd(amount)
          result.config(text=f"{usd} USD")
    
     except:
          result.config(text="Ingresa un numero valido")

window = tk.Tk()
window.title("Conversor de dolar")
window.geometry("600x400")

label = tk.Label(window, text="Cantidad en dolares:")
label.pack()

entry = tk.Entry(window)
entry.pack()
entry.bind("<Return>", convert_to_pesos)

button_pesos = tk.Button(window, text="Dolares → Pesos", command=convert_to_pesos)
button_pesos.pack()

button_usd = tk.Button(window, text="Pesos → Dolares", command=convert_to_usd)
button_usd.pack()

result = tk.Label(window, text="")
result.pack()

window.mainloop() 