import tkinter as tk
import requests
import time

API_URL = "https://api.coingecko.com/api/v3/simple/price"


COIN_IDS = ["bitcoin", "ethereum", "solana", "dogecoin"]

COIN_NAMES = {
    "bitcoin":  "Bitcoin (BTC)",
    "ethereum": "Ethereum (ETH)",
    "solana":   "Solana (SOL)",
    "dogecoin": "Dogecoin (DOGE)",
}

window = tk.Tk()
window.title("Курсы криптовалют")
window.geometry("430x380")
window.resizable(False, False)


tk.Label(window, text="Курсы криптовалют к USD", font=("Arial", 15, "bold")).pack(pady=12)


price_labels = {}
change_labels = {}

for coin_id in COIN_IDS:
    row = tk.Frame(window)
    row.pack(pady=3, padx=25)

    tk.Label(row, text=COIN_NAMES[coin_id], width=15, anchor="w", font=("Arial", 12)).pack(side="left")

    price_labels[coin_id] = tk.Label(row, text="—.—— $", width=13, anchor="e", font=("Arial", 12, "bold"))
    price_labels[coin_id].pack(side="left")

    change_labels[coin_id] = tk.Label(row, text="", width=9, anchor="e", font=("Arial", 10))
    change_labels[coin_id].pack(side="left")

status_label = tk.Label(window, text="Нажмите кнопку 'Обновить'", fg="gray")
status_label.pack(pady=8)

update_button = tk.Button(window, text="Обновить курсы", width=22)
update_button.pack(pady=5)

def fetch_prices():

    params = {
        "ids": ",".join(COIN_IDS),
        "vs_currencies": "usd",
        "include_24hr_change": "true"
    }
    response = requests.get(API_URL, params=params, timeout=10)
    response.raise_for_status()
    return response.json()

def update():
    try:
        data = fetch_prices()

        for coin_id in COIN_IDS:
            price  = data[coin_id]["usd"]
            change = data[coin_id]["usd_24h_change"]

            price_labels[coin_id].config(
                text=f"{price:,.2f} $".replace(",", " "))

            change_labels[coin_id].config(
                text=f"{change:+.2f}%",
                fg="green" if change >= 0 else "red")

        status_label.config(
        text=f"Обновлено в {time.strftime('%H:%M:%S')}", fg="green")

    except Exception:
        status_label.config(text="Не удалось загрузить данные", fg="red")

update_button.config(command=update)

window.mainloop()
