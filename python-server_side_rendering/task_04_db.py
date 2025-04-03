from flask import Flask, request, render_template, jsonify
import json
import csv
import sqlite3

app = Flask(__name__)

# Function to read data from JSON file
def read_json():
    try:
        with open('products.json', 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return None

# Function to read data from CSV file
def read_csv():
    try:
        with open('products.csv', 'r') as file:
            reader = csv.DictReader(file)
            return [row for row in reader]
    except FileNotFoundError:
        return None

# Function to read data from SQLite
def read_sql():
    try:
        conn = sqlite3.connect('products.db')
        cursor = conn.cursor()
        cursor.execute("SELECT id, name, category, price FROM Products")
        rows = cursor.fetchall()
        conn.close()

        products = [{"id": row[0], "name": row[1], "category": row[2], "price": row[3]} for row in rows]
        return products
    except sqlite3.Error as e:
        return None

@app.route('/products')
def get_products():
    source = request.args.get('source', '').lower()
    product_id = request.args.get('id')

    if source == "json":
        products = read_json()
    elif source == "csv":
        products = read_csv()
    elif source == "sql":
        products = read_sql()
    else:
        return render_template('product_display.html', error="Wrong source")

    if products is None:
        return render_template('product_display.html', error="Error reading data")

    # Filter by ID if provided
    if product_id:
        products = [p for p in products if str(p["id"]) == product_id]
        if not products:
            return render_template('product_display.html', error="Product not found")

    return render_template('product_display.html', products=products)

if __name__ == '__main__':
    app.run(debug=True)
