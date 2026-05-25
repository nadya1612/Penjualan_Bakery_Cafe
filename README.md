
# Python CRUD Application for Bakery & Coffee Shop

A terminal-based Python application for managing Bakery & Coffee Shop menu data using Create, Read, Update, and Delete (CRUD) operations.

## Business Understanding

This project was developed to help Bakery & Coffee Shop businesses manage menu data and sales transactions more efficiently. Product data such as menu name, category, price, stock, and total sales plays an important role in supporting store operations and monitoring sales performance.

## Benefits

* Simplifies bakery and coffee menu management
* Helps monitor product stock
* Makes product searching and updating easier
* Supports the purchasing transaction process
* Provides simple sales reports
* Reduces manual recording errors

## Target Users

This application is designed for:
* Cashiers
* Store staff
* Bakery/Coffee shop owners

To support activities such as:
* Menu management
* Purchase transactions
* Stock monitoring
* Sales reporting



# Features

## Create Menu
Add new menu items with information such as:
* Product ID
* Product name
* Category
* Stock
* Price
* Total products sold

## Read Menu
* Display all menu items
* Search products by menu name

## Update Menu
Update product information such as:
* Product name
* Category
* Stock
* Price
* Total products sold

## Delete Menu
Delete products based on Product ID.

## Buy Product
* Purchase products
* Add products to the shopping cart
* Automatically reduce stock
* Calculate subtotal and total payment

## Sales Report
Display:
* Total products sold
* Total revenue for each product
* Overall total revenue

---

# Installation

## Prerequisites
* Python 3.x

## Run Application

```bash
python main.py
```

---

# Usage

## Main Menu

1. View Menu List
2. Add Menu Item
3. Update Menu Item
4. Delete Menu Item
5. Buy Product
6. Sales Report
7. Exit Program

---

# Data Model

Product data is stored using Python Lists and Dictionaries.

## Product Fields

 Field              Type     Description 
 product_id         string   Unique product ID 
 product_name       string   Product name 
 product_category   string   Product category 
 product_stock      integer  Product stock quantity 
 product_price      integer  Product price 
 product_total_sold integer  Total products sold 



# Technologies Used

* Python
* List
* Dictionary
* Looping
* Conditional Statements
* Functions



# Future Improvements

* Add database integration
* Login authentication
* Export reports to Excel/CSV
* GUI interface
* Digital payment system



