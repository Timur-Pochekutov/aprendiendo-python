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

def convert(event=None):
        try:
            amount = float(entry.get())
            if direction.get() == "to_pesos":
                 pesos = usd_to_pesos(amount)
                 result.config(text=f"{pesos} pesos")
            else:
                 usd = pesos_to_usd(amount)
                 result.config(text=f"{usd} USD")
        except:
            result.config(text="Ingresa un numero valido")

window = tk.Tk()
window.title("Conversor de dolar")
window.geometry("600x400")

direction = tk.StringVar(value= "to_pesos")

label = tk.Label(window, text="Ingresa la cantidad:", font=("Arial", 16))
label.pack(pady=(40, 19))

entry = tk.Entry(window, font=("Arial", 16), width=15)
entry.pack(pady = 10)
entry.bind("<Return>", convert)

radio1 = tk.Radiobutton(window, text="Dolares → Pesos", variable=direction, value="to_pesos", font=("Arial", 12))
radio1.pack()

radio2 = tk.Radiobutton(window, text="Pesos → Dolares", variable=direction, value="to_usd", font=("Arial", 12))
radio2.pack()

button = tk.Button(window, text="Convertir", command=convert, font=("Arial", 14))
button.pack(pady=15)

result = tk.Label(window, text="")
result.pack()

window.mainloop() 