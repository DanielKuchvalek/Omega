from tkinter import Toplevel, Button
from tkinter import Frame, Button, Toplevel, Label, Entry
from datatier import Datatier
import methods_customer
import methods_orders
import methods_products
import methods_category
import methods_order_item
import methods_reviews
import methods_address
import sys

class Widgets:

    def __init__(self, master, role):
        self.master = master
        self.role = role

    def menu_widgets(self):
        button_frame = Toplevel(self.master)
        button_frame.title("Menu")
        button_frame.configure(bg="gray10")
        button_frame.geometry("170x550")

        customers_button = Button(button_frame, text="Customers",
                                  command=lambda: [button_frame.destroy(), self.customers_widgets()],
                                  bg="#4a4a4a",
                                  fg="white", width=20, height=2)
        customers_button.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")

        orders_button = Button(button_frame, text="Orders",
                               command=lambda: [button_frame.destroy(), self.order_widgets()],
                               bg="#4a4a4a",
                               fg="white")
        orders_button.grid(row=1, column=0, padx=10, pady=10, sticky="nsew")

        product_button = Button(button_frame, text="Products",
                                command=lambda: [button_frame.destroy(), self.product_widgets()],
                                bg="#4a4a4a",
                                fg="white", width=20, height=2)
        product_button.grid(row=2, column=0, padx=10, pady=10, sticky="nsew")

        category_button = Button(button_frame, text="Category",
                                 command=lambda: [button_frame.destroy(), self.category_widgets()],
                                 bg="#4a4a4a",
                                 fg="white", width=20, height=2)
        category_button.grid(row=3, column=0, padx=10, pady=10, sticky="nsew")

        order_item_button = Button(button_frame, text="Order item",
                                   command=lambda: [button_frame.destroy(), self.order_item_widgets()],
                                   bg="#4a4a4a",
                                   fg="white", width=20, height=2)
        order_item_button.grid(row=4, column=0, padx=10, pady=10, sticky="nsew")

        review_button = Button(button_frame, text="Review",
                               command=lambda: [button_frame.destroy(), self.review_widgets()],
                               bg="#4a4a4a",
                               fg="white", width=20, height=2)
        review_button.grid(row=5, column=0, padx=10, pady=10, sticky="nsew")

        address_button = Button(button_frame, text="Adreess",
                                command=lambda: [button_frame.destroy(), self.address_widgets()],
                                bg="#4a4a4a",
                                fg="white", width=20, height=2)
        address_button.grid(row=6, column=0, padx=10, pady=10, sticky="nsew")

        quit_button = Button(button_frame, text="Quit",
                             command=self.quit_app,
                             bg="#4a4a4a",
                             fg="white")
        quit_button.grid(row=7, column=0, padx=10, pady=10, sticky="nsew")

    def customers_widgets(self):
        customers_window = Toplevel(self.master)
        customers_window.title("Customers")
        customers_window.geometry("170x400")
        customers_window.config(bg='gray10')

        # Show Customers button
        customers_button = Button(customers_window, text="Show Customers", command=methods_customer.show_customers,
                                  bg="#4a4a4a",
                                  fg="white")
        customers_button.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")

        if self.role == "admin":
            # Add Customers button
            add_customer_button = Button(customers_window, text="Add Customers", command=methods_customer.add_customer,
                                         bg="#4a4a4a", fg="white", width=20, height=2)
            add_customer_button.grid(row=1, column=0, padx=10, pady=10, sticky="nsew")

            # Update Customers button
            update_customer_button = Button(customers_window, text="Update Customers",
                                            command=lambda: [customers_window.destroy(),
                                                             self.update_customer_widgets()],
                                            bg="#4a4a4a", fg="white")
            update_customer_button.grid(row=2, column=0, padx=10, pady=10, sticky="nsew")

            # Delete Customers button
            delete_customer_button = Button(customers_window, text="Delete Customers",
                                            command=methods_customer.delete_customer_window, bg="#4a4a4a", fg="white",
                                            width=20,
                                            height=2)
            delete_customer_button.grid(row=3, column=0, padx=10, pady=10, sticky="nsew")

            # Import Customers button
            import_customer_button = Button(customers_window, text="Import Customers",
                                            command=methods_customer.import_customers,
                                            bg="#4a4a4a", fg="white")
            import_customer_button.grid(row=4, column=0, padx=10, pady=10, sticky="nsew")

        # Back button
        back_button = Button(customers_window, text="Back",
                             command=lambda: [customers_window.destroy(), self.menu_widgets()], bg="#4a4a4a",
                             fg="white", width=20, height=2)
        back_button.grid(row=5, column=0, padx=10, pady=10, sticky="nsew")

    def update_customer_widgets(self):
        update_customer_window = Toplevel(self.master)
        update_customer_window.title("Update Customer")
        update_customer_window.geometry("170x400")
        update_customer_window.config(bg='gray10')

        update_customer_button = Button(update_customer_window, text="Update Email and Password",
                                        command=methods_customer.update_customers,
                                        bg="#4a4a4a",
                                        fg="white")
        update_customer_button.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")

        update_customer_email = Button(update_customer_window, text="Update Email",
                                       command=methods_customer.update_customers_email,
                                       bg="#4a4a4a",
                                       fg="white", width=20, height=2)
        update_customer_email.grid(row=1, column=0, padx=10, pady=10, sticky="nsew")

        update_customer_password = Button(update_customer_window, text="Update Password",
                                          command=methods_customer.update_customers_password,
                                          bg="#4a4a4a",
                                          fg="white")
        update_customer_password.grid(row=2, column=0, padx=10, pady=10, sticky="nsew")

        back_button = Button(update_customer_window, text="Back",
                             command=lambda: [update_customer_window.destroy(), self.customers_widgets()],
                             bg="#4a4a4a", fg="white", width=20, height=2)
        back_button.grid(row=3, column=0, padx=10, pady=10, sticky="nsew")


    def order_widgets(self):
        order_window = Toplevel(self.master)
        order_window.title("Orders")
        order_window.geometry("170x500")
        order_window.config(bg='gray10')

        select_order_button = Button(order_window, text="Show Order", command=methods_orders.show_orders, bg="#4a4a4a",
                                     fg="white")
        select_order_button.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")

        select_order_data = Button(order_window, text="Show Order Data", command=methods_orders.show_order_data,
                                   bg="#4a4a4a",
                                   fg="white", width=20, height=2)
        select_order_data.grid(row=1, column=0, padx=10, pady=10, sticky="nsew")

        select_order_price_data = Button(order_window, text="Show Order Price",
                                         command=methods_orders.show_orders_price,
                                         bg="#4a4a4a",
                                         fg="white", width=20, height=2)
        select_order_price_data.grid(row=2, column=0, padx=10, pady=10, sticky="nsew")

        if self.role == "admin":
            # Add Customers button
            add_order_button = Button(order_window, text="Add Order", command=methods_orders.add_order, bg="#4a4a4a",
                                      fg="white")
            add_order_button.grid(row=3, column=0, padx=10, pady=10, sticky="nsew")
            # Delete Customers button
            delete_order_button = Button(order_window, text="Delete Order", command=methods_orders.delete_order_window,
                                         bg="#4a4a4a", fg="white", width=20, height=2)
            delete_order_button.grid(row=4, column=0, padx=10, pady=10, sticky="nsew")
            # Update Customers button
            update_order_button = Button(order_window, text="Update Order",
                                         command=lambda: [order_window.destroy(), self.update_order_widgets()],
                                         bg="#4a4a4a",
                                         fg="white")
            update_order_button.grid(row=5, column=0, padx=10, pady=10, sticky="nsew")
            # Import Orders button
            import_orders_button = Button(order_window, text="Import Orders", command=methods_orders.import_orders,
                                          bg="#4a4a4a",
                                          fg="white", width=20, height=2)
            import_orders_button.grid(row=6, column=0, padx=10, pady=10, sticky="nsew")

        # Back button
        back_button = Button(order_window, text="Back", command=lambda: [order_window.destroy(), self.menu_widgets()],
                             bg="#4a4a4a", fg="white")
        back_button.grid(row=7, column=0, padx=10, pady=10, sticky="nsew")
    def update_order_widgets(self):
        update_order_window = Toplevel(self.master)
        update_order_window.title("Update Order")
        update_order_window.geometry("240x400")
        update_order_window.config(bg='gray10')

        update_customer_button = Button(update_order_window, text="Update Customer , Status, Price in Order",
                                        command=methods_orders.update_order,
                                        bg="#4a4a4a",
                                        fg="white")
        update_customer_button.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")

        update_customer_email = Button(update_order_window, text="Update Status",
                                       command=methods_orders.update_order_status,
                                       bg="#4a4a4a",
                                       fg="white", width=20, height=2)
        update_customer_email.grid(row=1, column=0, padx=10, pady=10, sticky="nsew")

        update_customer_password = Button(update_order_window, text="Update total price",
                                          command=methods_orders.update_order_price,
                                          bg="#4a4a4a",
                                          fg="white")
        update_customer_password.grid(row=2, column=0, padx=10, pady=10, sticky="nsew")

        back_button = Button(update_order_window, text="Back",
                             command=lambda: [update_order_window.destroy(), self.order_widgets()],
                             bg="#4a4a4a", fg="white", width=20, height=2)
        back_button.grid(row=3, column=0, padx=10, pady=10, sticky="nsew")

    def product_widgets(self):
        product_window = Toplevel(self.master)
        product_window.title("Products")
        product_window.geometry("170x400")
        product_window.config(bg='gray10')

        select_product_button = Button(product_window, text="Show Product", command=methods_products.show_products,
                                       bg="#4a4a4a",
                                       fg="white", width=20, height=2)
        select_product_button.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")
        if self.role == "admin":
            add_product_button = Button(product_window, text="Add Product", command=methods_products.add_product,
                                        bg="#4a4a4a",
                                        fg="white")
            add_product_button.grid(row=1, column=0, padx=10, pady=10, sticky="nsew")

            update_product_button = Button(product_window, text="Update Product",
                                           command=lambda: [product_window.destroy(), self.update_product_widgets()],
                                           bg="#4a4a4a",
                                           fg="white", width=20, height=2)
            update_product_button.grid(row=2, column=0, padx=10, pady=10, sticky="nsew")

            delete_product_button = Button(product_window, text="Delete Product",
                                           command=methods_products.delete_product_window,
                                           bg="#4a4a4a", fg="white")
            delete_product_button.grid(row=3, column=0, padx=10, pady=10, sticky="nsew")

            import_product_button = Button(product_window, text="Import Products",
                                           command=methods_products.import_products,
                                           bg="#4a4a4a",
                                           fg="white", width=20, height=2)
            import_product_button.grid(row=4, column=0, padx=10, pady=10, sticky="nsew")
        # Back button
        back_button = Button(product_window, text="Back",
                             command=lambda: [product_window.destroy(), self.menu_widgets()],
                             bg="#4a4a4a", fg="white")
        back_button.grid(row=5, column=0, padx=10, pady=10, sticky="nsew")

    def update_product_widgets(self):
        update_product_window = Toplevel(self.master)
        update_product_window.title("Update Product")
        update_product_window.geometry("170x400")
        update_product_window.config(bg='gray10')

        update_product_all = Button(update_product_window, text="Update product",
                                    command=methods_products.update_product,
                                    bg="#4a4a4a",
                                    fg="white")
        update_product_all.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")

        update_product_description = Button(update_product_window, text="Update description",
                                            command=methods_products.update_product_description,
                                            bg="#4a4a4a",
                                            fg="white", width=20, height=2)
        update_product_description.grid(row=1, column=0, padx=10, pady=10, sticky="nsew")

        update_product_price = Button(update_product_window, text="Update price",
                                      command=methods_products.update_product_price,
                                      bg="#4a4a4a",
                                      fg="white")
        update_product_price.grid(row=2, column=0, padx=10, pady=10, sticky="nsew")

        update_product_stock = Button(update_product_window, text="Update in_stock",
                                      command=methods_customer.update_customers_password,
                                      bg="#4a4a4a",
                                      fg="white", width=20, height=2)
        update_product_stock.grid(row=3, column=0, padx=10, pady=10, sticky="nsew")

        update_product_category = Button(update_product_window, text="Update Category",
                                         command=methods_customer.update_customers_password,
                                         bg="#4a4a4a",
                                         fg="white")
        update_product_category.grid(row=4, column=0, padx=10, pady=10, sticky="nsew")

        back_button = Button(update_product_window, text="Back",
                             command=lambda: [update_product_window.destroy(), self.product_widgets()],
                             bg="#4a4a4a", fg="white", width=20, height=2)
        back_button.grid(row=5, column=0, padx=10, pady=10, sticky="nsew")
    def category_widgets(self):
        category_window = Toplevel(self.master)
        category_window.title("Categories")
        category_window.geometry("170x400")
        category_window.config(bg='gray10')

        # Show Customers button
        category_button = Button(category_window, text="Show Category", command=methods_category.show_category,
                                 bg="#4a4a4a",
                                 fg="white")
        category_button.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")

        if self.role == "admin":
            # Add Category button
            add_category_button = Button(category_window, text="Add Category",
                                         command=methods_category.add_category,
                                         bg="#4a4a4a", fg="white", width=20, height=2)
            add_category_button.grid(row=1, column=0, padx=10, pady=10, sticky="nsew")

            # Update Category button
            update_category_button = Button(category_window, text="Update Category",
                                            command=methods_category.update_category,
                                            bg="#4a4a4a", fg="white")
            update_category_button.grid(row=2, column=0, padx=10, pady=10, sticky="nsew")

            # Delete Category button
            delete_category_button = Button(category_window, text="Delete Category",
                                            command=methods_category.delete_category_window, bg="#4a4a4a",
                                            fg="white",
                                            width=20,
                                            height=2)
            delete_category_button.grid(row=3, column=0, padx=10, pady=10, sticky="nsew")

            # Import Category button
            import_category_button = Button(category_window, text="Import Category",
                                            command=methods_category.import_category,
                                            bg="#4a4a4a", fg="white")
            import_category_button.grid(row=4, column=0, padx=10, pady=10, sticky="nsew")

        # Back button
        back_button = Button(category_window, text="Back",
                             command=lambda: [category_window.destroy(), self.menu_widgets()], bg="#4a4a4a",
                             fg="white", width=20, height=2)
        back_button.grid(row=5, column=0, padx=10, pady=10, sticky="nsew")

    def order_item_widgets(self):
        order_item_window = Toplevel(self.master)
        order_item_window.title("Order Item")
        order_item_window.geometry("170x400")
        order_item_window.config(bg='gray10')

        # Show Customers button
        order_item_button = Button(order_item_window, text="Show Order items",
                                   command=methods_order_item.show_orders_items,
                                   bg="#4a4a4a",
                                   fg="white")
        order_item_button.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")

        # Back button
        back_button = Button(order_item_window, text="Back",
                             command=lambda: [order_item_window.destroy(), self.menu_widgets()], bg="#4a4a4a",
                             fg="white", width=20, height=2)
        back_button.grid(row=5, column=0, padx=10, pady=10, sticky="nsew")

    def review_widgets(self):
        review_window = Toplevel(self.master)
        review_window.title("Review")
        review_window.geometry("170x400")
        review_window.config(bg='gray10')

        select_review_button = Button(review_window, text="Show Reviews", command=methods_reviews.show_review,
                                      bg="#4a4a4a",
                                      fg="white")
        select_review_button.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")

        add_category_button = Button(review_window, text="Add Review",
                                     command=methods_reviews.add_review,
                                     bg="#4a4a4a", fg="white", width=20, height=2)
        add_category_button.grid(row=1, column=0, padx=10, pady=10, sticky="nsew")

        update_review_button = Button(review_window, text="Update Review",
                                      command=methods_reviews.update_review,
                                      bg="#4a4a4a", fg="white")
        update_review_button.grid(row=2, column=0, padx=10, pady=10, sticky="nsew")

        delete_review_button = Button(review_window, text="Delete Reviews",
                                      command=methods_reviews.delete_review_window, bg="#4a4a4a",
                                      fg="white",
                                      width=20,
                                      height=2)
        delete_review_button.grid(row=3, column=0, padx=10, pady=10, sticky="nsew")

        # Back button
        back_button = Button(review_window, text="Back",
                             command=lambda: [review_window.destroy(), self.menu_widgets()],
                             bg="#4a4a4a", fg="white")
        back_button.grid(row=4, column=0, padx=10, pady=10, sticky="nsew")

    def address_widgets(self):
        address_window = Toplevel(self.master)
        address_window.title("Order Item")
        address_window.geometry("170x400")
        address_window.config(bg='gray10')

        # Show Customers button
        order_item_button = Button(address_window, text="Show Address",
                                   command=methods_address.show_address,
                                   bg="#4a4a4a",
                                   fg="white")
        order_item_button.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")
        if self.role == "admin":
            add_category_button = Button(address_window, text="Add Address",
                                         command=methods_address.add_address,
                                         bg="#4a4a4a", fg="white", width=20, height=2)
            add_category_button.grid(row=1, column=0, padx=10, pady=10, sticky="nsew")

            update_review_button = Button(address_window, text="Update Address",
                                          command=methods_address.update_address,
                                          bg="#4a4a4a", fg="white")
            update_review_button.grid(row=2, column=0, padx=10, pady=10, sticky="nsew")

            delete_customer_button = Button(address_window, text="Delete Address",
                                            command=methods_address.delete_address_window, bg="#4a4a4a", fg="white",
                                            width=20,
                                            height=2)
            delete_customer_button.grid(row=3, column=0, padx=10, pady=10, sticky="nsew")

        # Back button
        back_button = Button(address_window, text="Back",
                             command=lambda: [address_window.destroy(), self.menu_widgets()], bg="#4a4a4a",
                             fg="white", width=20, height=2)
        back_button.grid(row=4, column=0, padx=10, pady=10, sticky="nsew")

    def quit_app(self):
        if sys.stdin.isatty():  # Check if running as a standalone process
            self.master.destroy()
            sys.exit()  # Exit the process
        else:
            self.master.destroy()  # Quit the app if running in an interactive shell