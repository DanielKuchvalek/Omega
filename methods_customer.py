import re
from tkinter import filedialog, Button, Toplevel, Text, BOTH, END, Label, Entry
from datatier import Datatier
from model import Customer

data_tier = Datatier()


def show_customers():
    result_window = Toplevel()
    result_window.title("Customers")
    result_window.geometry("1200x600")
    result_window.configure(bg='gray10')

    customers = data_tier.get_customers()
    result_text = Text(result_window, bg='gray10', fg="white", font=("Helvetica", 12))
    result_text.pack(fill=BOTH, expand=True)

    result_text.insert(END, "\n{:<5} {:<30} {:<50} {:<30}\n".format("No.", "Name", "Email", "Password"))
    result_text.insert(END, "-" * 225 + "\n")

    cislo = 0
    for customer in customers:
        cislo += 1
        result_text.insert(END, "{:<5} {:<30} {:<50} {:<30}\n\n".format(str(cislo), customer['name'], customer['email'],
                                                                        customer['password']))

    result_label = Label(result_window, text="Customers are shown.", bg='gray10', fg="white", font=("Helvetica", 14))
    result_label.pack(pady=(10, 0))


def add_customer():
    # Create a new window for adding a customer
    add_window = Toplevel()
    add_window.title("Add Customer")
    add_window.geometry("400x300")

    # Create labels and entry fields for the customer information
    name_label = Label(add_window, text="Name:")
    name_label.pack()
    name_entry = Entry(add_window)
    name_entry.pack()

    email_label = Label(add_window, text="Email:")
    email_label.pack()
    email_entry = Entry(add_window)
    email_entry.pack()

    password_label = Label(add_window, text="Password:")
    password_label.pack()
    password_entry = Entry(add_window, show="*")
    password_entry.pack()

    # Create a function to add the customer to the database
    def add_customer_to_database():
        # Get the customer information from the entry fields
        name = name_entry.get()
        email = email_entry.get()
        password = password_entry.get()

        # Validate the email using a regular expression
        email_regex = r"[^@]+@[^@]+\.[^@]+"
        if not re.match(email_regex, email):
            result_label.config(text="Invalid email address.")
            return

        name_regex = r"^[A-Za-z\s]+$"
        if not re.match(name_regex, name):
            result_label.config(text="Invalid name.")
            return

        # Add the customer to the database
        customer = Customer(name, email, password)
        data_tier.add_customer(customer)

        # Show a message indicating that the customer was added
        result_label.config(text="Customer added.")

    # Create a button to add the customer to the database
    add_button = Button(add_window, text="Add Customer", command=add_customer_to_database)
    add_button.pack()

    # Create a label to display the result of adding the customer
    result_label = Label(add_window)
    result_label.pack()


def delete_customer_window():
    # Vytvoření nového okna pro zadání jména zákazníka
    delete_window = Toplevel()
    delete_window.title("Delete Order")
    delete_window.geometry("600x500")

    pole = Text(delete_window)
    pole.pack()

    customers = data_tier.get_customers_name()
    cislo = 0
    for customer in customers:
        cislo += 1
        pole.insert(END, (str(cislo) + ". customer_name: {}\n".format(customer['name'])))

    # Vytvoření popisku a vstupního pole pro zadání jména zákazníka
    name_label = Label(delete_window, text="Customer Name:")
    name_label.pack()
    name_entry = Entry(delete_window)
    name_entry.pack()

    def delete_customer_from_controller():
        # Get the customer name from the entry field
        name = name_entry.get()

        # Delete the order from the controller
        data_tier.delete_customer(name)

        # Show a message indicating that the order was deleted
        result_label.config(text="Customer deleted successfully.")

    # Create a button to delete the order
    delete_button = Button(delete_window, text="Delete Order", command=delete_customer_from_controller)
    delete_button.pack()

    # Create a label to display the result of deleting the order
    result_label = Label(delete_window)
    result_label.pack()


def update_customers():
    update_window = Toplevel()
    update_window.title("Update Customers ")
    update_window.geometry("1200x600")

    customers = data_tier.get_customers()
    update_text = Text(update_window)
    update_text.pack()

    update_text.insert(END, "Customers:\n")
    cislo = 0
    for customer in customers:
        cislo += 1
        update_text.insert(END, str(cislo) + ". \nName: {}\nEmail: {}\nPassword: {}\n".format(
            customer['name'], customer['email'], customer['password']))

    customer_name_label = Label(update_window, text="Customer name:")
    customer_name_label.pack()
    customer_name_entry = Entry(update_window)
    customer_name_entry.pack()

    email_label = Label(update_window, text="Email:")
    email_label.pack()
    email_entry = Entry(update_window)
    email_entry.pack()

    password_label = Label(update_window, text="Password:")
    password_label.pack()
    password_entry = Entry(update_window)
    password_entry.pack()

    def update_customer_in_database():
        new_email = email_entry.get()
        new_password = password_entry.get()
        customer_name = customer_name_entry.get()

        # Validate email format
        if not re.match(r"[^@]+@[^@]+\.[^@]+", new_email):
            result_label.config(text="Invalid email format.")
            return

        # Validate password format (at least one digit and one letter, minimum length 8)
        if not re.match(r"^(?=.*[A-Za-z])(?=.*\d)[A-Za-z\d]{8,}$", new_password):
            result_label.config(text="Invalid password format. At least one digit and one letter, minimum length 8")
            return

        # Validate customer name length (minimum length 2)
        if len(customer_name) < 2:
            result_label.config(text="Invalid customer name.")
            return

        data_tier.update_customers(new_email, new_password, customer_name)
        result_label.config(text="Customer has been updated.")

    update_button = Button(update_window, text="Update Customer", command=update_customer_in_database)
    update_button.pack()

    result_label = Label(update_window)
    result_label.pack()


def update_customers_email():
    update_window = Toplevel()
    update_window.title("Update Customers email")
    update_window.geometry("1200x600")

    customers = data_tier.get_customers()
    update_text = Text(update_window)
    update_text.pack()

    update_text.insert(END, "Customers:\n")
    cislo = 0
    for customer in customers:
        cislo += 1
        update_text.insert(END, str(cislo) + ". \nName: {}\nEmail: {}\nPassword: {}\n".format(
            customer['name'], customer['email'], customer['password']))

    customer_name_label = Label(update_window, text="Customer name:")
    customer_name_label.pack()
    customer_name_entry = Entry(update_window)
    customer_name_entry.pack()

    email_label = Label(update_window, text="Email:")
    email_label.pack()
    email_entry = Entry(update_window)
    email_entry.pack()

    def update_customer_in_database():
        new_email = email_entry.get()
        customer_name = customer_name_entry.get()

        # Validate email format
        if not re.match(r"[^@]+@[^@]+\.[^@]+", new_email):
            result_label.config(text="Invalid email format.")
            return

        # Validate customer name length (minimum length 2)
        if len(customer_name) < 2:
            result_label.config(text="Invalid customer name.")
            return

        data_tier.update_customers_email(new_email, customer_name)
        result_label.config(text="Customers email has been updated.")

    update_button = Button(update_window, text="Update Customers email", command=update_customer_in_database)
    update_button.pack()

    result_label = Label(update_window)
    result_label.pack()


def update_customers_password():
    update_window = Toplevel()
    update_window.title("Update Customers password")
    update_window.geometry("1200x600")

    customers = data_tier.get_customers()
    update_text = Text(update_window)
    update_text.pack()

    update_text.insert(END, "Customers:\n")
    cislo = 0
    for customer in customers:
        cislo += 1
        update_text.insert(END, str(cislo) + ". \nName: {}\nEmail: {}\nPassword: {}\n".format(
            customer['name'], customer['email'], customer['password']))

    customer_name_label = Label(update_window, text="Customer name:")
    customer_name_label.pack()
    customer_name_entry = Entry(update_window)
    customer_name_entry.pack()

    password_label = Label(update_window, text="Password:")
    password_label.pack()
    password_entry = Entry(update_window)
    password_entry.pack()

    def update_customer_in_database():

        new_password = password_entry.get()
        customer_name = customer_name_entry.get()

        # Validate password format (at least one digit and one letter, minimum length 8)
        if not re.match(r"^(?=.*[A-Za-z])(?=.*\d)[A-Za-z\d]{8,}$", new_password):
            result_label.config(text="Invalid password format. At least one digit and one letter, minimum length 8")
            return

        # Validate customer name length (minimum length 2)
        if len(customer_name) < 2:
            result_label.config(text="Invalid customer name.")
            return

        data_tier.update_customers_password(new_password, customer_name)
        result_label.config(text="Customers password has been updated.")

    update_button = Button(update_window, text="Update Customers password", command=update_customer_in_database)
    update_button.pack()

    result_label = Label(update_window)
    result_label.pack()


def import_customers():
    filetypes = [('CSV files', '*.csv'), ('All files', '*.*')]
    filepath = filedialog.askopenfilename(filetypes=filetypes)
    if filepath:
        data_tier.import_customers_from_csv(filepath)
