import tkinter as tk
from tkinter import ttk, messagebox
import mysql.connector
\
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Pass",
    database="grocery_management_db"
)
cursor = conn.cursor()

def fetch_products():
    cursor.execute("SELECT * FROM product")
    rows = cursor.fetchall()
    product_list.delete(*product_list.get_children())
    for row in rows:
        product_list.insert("", tk.END, values=row)

def add_product():
    name, category, price, stock, expiry = entry_name.get(), entry_category.get(), entry_price.get(), entry_stock.get(), entry_expiry.get()
    if name and price and stock:
        try:
            cursor.execute("INSERT INTO product (name, category, price, stock_quantity, expiry_date) VALUES (%s, %s, %s, %s, %s)",
                           (name, category, price, stock, expiry))
            conn.commit()
            fetch_products()
            messagebox.showinfo("Success", "Product Added")
        except mysql.connector.Error as e:
            messagebox.showerror("Database Error", f"Error: {e}")
    else:
        messagebox.showwarning("Error", "Please fill all fields")

def fetch_customers():
    cursor.execute("SELECT * FROM customer")
    rows = cursor.fetchall()
    customer_list.delete(*customer_list.get_children())
    for row in rows:
        customer_list.insert("", tk.END, values=row)

def add_customer():
    name, phone, email = entry_cust_name.get(), entry_phone.get(), entry_email.get()
    if name and phone:
        try:
            cursor.execute("INSERT INTO customer (name, phone, email) VALUES (%s, %s, %s)", (name, phone, email))
            conn.commit()
            fetch_customers()
            messagebox.showinfo("Success", "Customer Added")
        except mysql.connector.Error as e:
            messagebox.showerror("Database Error", f"Error: {e}")
    else:
        messagebox.showwarning("Error", "Please enter name and phone")

#GUI

root = tk.Tk()
root.title("Grocery Store Management")
root.geometry("900x600")

tk.Label(root, text="Product Name").grid(row=0, column=0)
entry_name = tk.Entry(root)
entry_name.grid(row=0, column=1)

tk.Label(root, text="Category").grid(row=1, column=0)
entry_category = tk.Entry(root)
entry_category.grid(row=1, column=1)

tk.Label(root, text="Price").grid(row=2, column=0)
entry_price = tk.Entry(root)
entry_price.grid(row=2, column=1)

tk.Label(root, text="Stock").grid(row=3, column=0)
entry_stock = tk.Entry(root)
entry_stock.grid(row=3, column=1)

tk.Label(root, text="Expiry Date").grid(row=4, column=0)
entry_expiry = tk.Entry(root)
entry_expiry.grid(row=4, column=1)

btn_add = tk.Button(root, text="Add Product", command=add_product)
btn_add.grid(row=5, column=0, pady=10)

columns = ("ID", "Name", "Category", "Price", "Stock", "Expiry")
product_list = ttk.Treeview(root, columns=columns, show="headings")
for col in columns:
    product_list.heading(col, text=col)
product_list.grid(row=6, column=0, columnspan=2, padx=10, pady=10)


tk.Label(root, text="Customer Name").grid(row=0, column=3)
entry_cust_name = tk.Entry(root)
entry_cust_name.grid(row=0, column=4)

tk.Label(root, text="Phone").grid(row=1, column=3)
entry_phone = tk.Entry(root)
entry_phone.grid(row=1, column=4)

tk.Label(root, text="Email").grid(row=2, column=3)
entry_email = tk.Entry(root)
entry_email.grid(row=2, column=4)

btn_add_cust = tk.Button(root, text="Add Customer", command=add_customer)
btn_add_cust.grid(row=3, column=3, pady=10)

cust_columns = ("ID", "Name", "Phone", "Email")
customer_list = ttk.Treeview(root, columns=cust_columns, show="headings")
for col in cust_columns:
    customer_list.heading(col, text=col)
customer_list.grid(row=6, column=3, columnspan=2, padx=10, pady=10)

fetch_products()
fetch_customers()

root.mainloop()
