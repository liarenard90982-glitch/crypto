import tkinter as tk


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

window.mainloop()
