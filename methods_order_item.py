import re
from tkinter import filedialog, Button, Toplevel, Text, BOTH, END, Label, Entry
from datatier import Datatier
from model import Order_items


data_tier = Datatier()

def show_orders_items():
    result_window = Toplevel()
    result_window.title("Orders items")
    result_window.geometry("1200x600")
    result_window.configure(bg='gray10')

    orders = data_tier.get_order_item()
    result_text = Text(result_window, bg='gray10', fg="white", font=("Helvetica", 12))
    result_text.pack(fill=BOTH, expand=True)

    result_text.insert(END,
                       "\n{:<5} {:<30} {:<20} {:<20}\n".format("No.", "order_id", "name", "quantity",))
    result_text.insert(END, "-" * 225 + "\n")

    cislo = 0
    for order in orders:
        cislo += 1
        result_text.insert(END, "{:<5} {:<35} {:<25} {:<20}\n\n".format(str(cislo), str(order['order_id']),
                                                                               order['name'],
                                                                               str(order['quantity'])))

    result_label = Label(result_window, text="Orders final price are shown.", bg='gray10', fg="white", font=("Helvetica", 14))
    result_label.pack(pady=(10, 0))

