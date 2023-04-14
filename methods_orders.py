import re
from tkinter import filedialog, Button, Toplevel, Text, BOTH, END, Label, Entry
from datatier import Datatier
from model import Order


data_tier = Datatier()


def show_orders_name():
    result_window = Toplevel()
    result_window.title("Customers")
    result_window.geometry("1200x600")

    orders = data_tier.get_orders_name()
    result_text = Text(result_window)
    result_text.pack(fill=BOTH, expand=True)

    result_text.insert(END, "Customers name:\n")
    cislo = 0
    for order in orders:
        cislo += 1
        result_text.insert(END, str(cislo) + ". Customer_name: {}\n".format(
            order['Customer_name']))


def show_orders():
    result_window = Toplevel()
    result_window.title("Orders")
    result_window.geometry("1200x600")
    result_window.configure(bg='gray10')

    orders = data_tier.get_orders()
    result_text = Text(result_window, bg='gray10', fg="white", font=("Helvetica", 12))
    result_text.pack(fill=BOTH, expand=True)

    result_text.insert(END,
                       "\n{:<5} {:<30} {:<20} {:<20} {:<20}\n".format("No.", "Customer name", "Order date", "Status",
                                                                      "Total price"))
    result_text.insert(END, "-" * 225 + "\n")

    cislo = 0
    for order in orders:
        cislo += 1
        order_date = order['Order_date'].strftime('%Y-%m-%d')
        result_text.insert(END, "{:<5} {:<30} {:<20} {:<20} {:<20}\n\n".format(str(cislo), order['Customer_name'],
                                                                               order_date, order['Status'],
                                                                               str(order['Total_price']) + " Kč"))

    result_label = Label(result_window, text="Orders are shown.", bg='gray10', fg="white", font=("Helvetica", 14))
    result_label.pack(pady=(10, 0))


def show_orders_price():
    result_window = Toplevel()
    result_window.title("Orders Price")
    result_window.geometry("1200x600")
    result_window.configure(bg='gray10')

    orders = data_tier.get_order_final_price()
    result_text = Text(result_window, bg='gray10', fg="white", font=("Helvetica", 12))
    result_text.pack(fill=BOTH, expand=True)

    result_text.insert(END,
                       "\n{:<5} {:<30} {:<20} {:<20}\n".format("No.", "Product name", "Final price", "quantity",))
    result_text.insert(END, "-" * 225 + "\n")

    cislo = 0
    for order in orders:
        cislo += 1
        result_text.insert(END, "{:<5} {:<30} {:<20} {:<20}\n\n".format(str(cislo), order['Products_name'],
                                                                               str(order['Final_price'])+ " Kč",
                                                                               str(order['Order_items_quantity']) ))

    result_label = Label(result_window, text="Orders final price are shown.", bg='gray10', fg="white", font=("Helvetica", 14))
    result_label.pack(pady=(10, 0))


def add_order():
    add_window = Toplevel()
    add_window.title("Add Order")
    add_window.geometry("1200x800")

    # Create a text widget to display customers
    customers = Text(add_window)
    customers.pack()

    # Get a list of customers from the data tier
    customers_list = data_tier.get_customers_name()

    # Loop through the list and display each customer's name
    for i, customer in enumerate(customers_list):
        customers.insert(END, f"{i + 1}. name: {customer['name']}\n")

    # Create labels and entry widgets for the order information
    customer_id_label = Label(add_window, text="Customer ID:")
    customer_id_entry = Entry(add_window)
    customer_id_label.pack()
    customer_id_entry.pack()

    status_label = Label(add_window, text="Status:")
    status_entry = Entry(add_window)
    status_label.pack()
    status_entry.pack()

    total_price_label = Label(add_window, text="Total Price:")
    total_price_entry = Entry(add_window)
    total_price_label.pack()
    total_price_entry.pack()

    # Create a function to submit the order
    def submit_order():
        # Get the order information from the entry widgets
        customer_id = customer_id_entry.get()
        status = status_entry.get()
        total_price = total_price_entry.get()

        # Check if the status is valid
        if status not in ['Pending', 'Shipped', 'Delivered']:
            output_text.insert(END, "You have to add Pending, Shipped or Delivered\n")
            return

        # Check if the total price is valid
        if not re.match(r'^[1-9]\d*(\.\d+)?$', total_price):
            output_text.insert(END, "Invalid Total Price\n")
            return

        # Create an Order object and add it to the data tier
        order = Order(customer_id, status, total_price)
        data_tier.add_order(order)

        output_text.insert(END, "Order added successfully.\n")

    # Create a button to submit the order
    submit_button = Button(add_window, text="Submit", command=submit_order)
    submit_button.pack()

    # Create a text widget to display output messages
    output_text = Text(add_window)
    output_text.pack()


def delete_order_window():
    # Vytvoření nového okna pro zadání jména zákazníka
    delete_window = Toplevel()
    delete_window.title("Delete Order")
    delete_window.geometry("1200x600")

    orders = Text(delete_window)
    orders.pack()

    orderss = data_tier.get_orders()
    cislo = 0
    for order in orderss:
        cislo += 1
        orders.insert(END, (
                str(cislo) + ". \ncustomer_name: {}\norder_date: {}\nstatus: {}\ntotal_price: {}\n".format(
            order['Customer_name'], order['Order_date'], order['Status'], order['Total_price'])))

    # Vytvoření popisku a vstupního pole pro zadání jména zákazníka
    name_label = Label(delete_window, text="Customer Name:")
    name_label.pack()
    name_entry = Entry(delete_window)
    name_entry.pack()

    def delete_order_from_controller():
        # Get the customer name from the entry field
        name = name_entry.get()

        # Delete the order from the controller
        data_tier.delete_order(name)

        # Show a message indicating that the order was deleted
        result_label.config(text="Order deleted successfully.")

    # Create a button to delete the order
    delete_button = Button(delete_window, text="Delete Order", command=delete_order_from_controller)
    delete_button.pack()

    # Create a label to display the result of deleting the order
    result_label = Label(delete_window)
    result_label.pack()


def update_order():
    update_window = Toplevel()
    update_window.title("Update Order")
    update_window.geometry("400x300")

    customers = Text(update_window)
    customers.pack()

    orderss = data_tier.get_orders()
    cislo = 0
    for order in orderss:
        cislo += 1
        customers.insert(END, (
                str(cislo) + ". \ncustomer_name: {}\norder_date: {}\nstatus: {}\ntotal_price: {}\n".format(
            order['Customer_name'], order['Order_date'], order['Status'], order['Total_price'])))

    customer_id_label = Label(update_window, text="Customer id:")
    customer_id_label.pack()
    customer_id_entry = Entry(update_window)
    customer_id_entry.pack()

    status_label = Label(update_window, text="Status:")
    status_label.pack()
    status_entry = Entry(update_window)
    status_entry.pack()

    total_price_label = Label(update_window, text="Total Price:")
    total_price_label.pack()
    total_price_entry = Entry(update_window)
    total_price_entry.pack()

    def update_order_in_database():
        customer_id = customer_id_entry.get()
        new_status = status_entry.get()
        new_total_price = total_price_entry.get()

        if new_status == 'Pending' or new_status == 'Shipped' or new_status == 'Delivered':
            data_tier.update_order(new_status, new_total_price, customer_id)
            result_label.config(text="Order has been updated.")
        else:
            result_label.config(text="Invalid status.")

    update_button = Button(update_window, text="Update Order", command=update_order_in_database)
    update_button.pack()

    result_label = Label(update_window)
    result_label.pack()

def update_order_price():
    update_window = Toplevel()
    update_window.title("Update Order Price")
    update_window.geometry("400x300")

    customers = Text(update_window)
    customers.pack()

    orders = data_tier.get_orders()
    cislo = 0
    for order in orders:
        cislo += 1
        customers.insert(END, (
                str(cislo) + ". \ncustomer_name: {}\norder_date: {}\nstatus: {}\ntotal_price: {}\n".format(
            order['Customer_name'], order['Order_date'], order['Status'], order['Total_price'])))

    customer_id_label = Label(update_window, text="Customer id:")
    customer_id_label.pack()
    customer_id_entry = Entry(update_window)
    customer_id_entry.pack()

    total_price_label = Label(update_window, text="Total Price:")
    total_price_label.pack()
    total_price_entry = Entry(update_window)
    total_price_entry.pack()

    def update_order_in_database():
        customer_id = customer_id_entry.get()
        new_total_price = total_price_entry.get()

        if not re.match(r'^[1-9]\d*(\.\d+)?$', new_total_price):
            output_text.insert(END, "Invalid Total Price\n")
            return

        # Create an Order object and add it to the data tier
        data_tier.update_order_price(new_total_price, customer_id)

        output_text.insert(END, "Order price updated successfully.\n")

    update_button = Button(update_window, text="Update Order price", command=update_order_in_database)
    update_button.pack()

    output_text = Text(update_window)
    output_text.pack()




def update_order_status():
    update_window = Toplevel()
    update_window.title("Update Order Status")
    update_window.geometry("400x300")

    customers = Text(update_window)
    customers.pack()

    orderss = data_tier.get_orders()
    cislo = 0
    for order in orderss:
        cislo += 1
        customers.insert(END, (
                str(cislo) + ". \ncustomer_name: {}\norder_date: {}\nstatus: {}\ntotal_price: {}\n".format(
            order['Customer_name'], order['Order_date'], order['Status'], order['Total_price'])))

    customer_id_label = Label(update_window, text="Customer id:")
    customer_id_label.pack()
    customer_id_entry = Entry(update_window)
    customer_id_entry.pack()

    status_label = Label(update_window, text="Status:")
    status_label.pack()
    status_entry = Entry(update_window)
    status_entry.pack()

    def update_order_in_database():
        customer_id = customer_id_entry.get()
        new_status = status_entry.get()


        if new_status == 'Pending' or new_status == 'Shipped' or new_status == 'Delivered':
            data_tier.update_order_status(new_status, customer_id)
            result_label.config(text="Order  status has been updated.")
        else:
            result_label.config(text="Invalid status.")

    update_button = Button(update_window, text="Update Order status", command=update_order_in_database)
    update_button.pack()

    result_label = Label(update_window)
    result_label.pack()

def show_order_data():
    result_window = Toplevel()
    result_window.title("Order Data")
    result_window.geometry("1200x600")
    result_window.configure(bg='gray10')

    orders = data_tier.get_order_data()
    result_text = Text(result_window, bg='gray10', fg="white", font=("Helvetica", 12))
    result_text.pack(fill=BOTH, expand=True)

    result_text.insert(END, "\n{:<5} {:<15} {:<15} {:<15} {:<10}\n".format("No.", "Order", "Customer Name","Product name","Amount"))
    result_text.insert(END,
                       "--------------------------------------------------------------------------------------\n\n")

    cislo = 0
    for order in orders:
        cislo += 1
        result_text.insert(END,
                           "{:<5} {:<20} {:<25} {:<25} {:<10}\n\n".format(str(cislo), order['order'], order['customer_name'],order['product_name'],
                                                                   order['product_amount']))
        result_text.insert(END,
                           "--------------------------------------------------------------------------------------\n\n")

    result_label = Label(result_window, text="Order Data is shown.", bg='gray10', fg="white", font=("Helvetica", 14))
    result_label.pack(pady=(10, 0))


def import_orders():
    filetypes = [('CSV files', '*.csv'), ('All files', '*.*')]
    filepath = filedialog.askopenfilename(filetypes=filetypes)
    if filepath:
        data_tier.import_order_from_csv(filepath)
