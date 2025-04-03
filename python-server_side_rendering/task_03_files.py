from flask import Flask, render_template, request
import json
import csv

app = Flask(__name__)

# Function to load JSON data
def load_json():
    try:
        with open("products.json", "r") as file:
            return json.load(file)
    except Exception as e:
        return {"error": str(e)}

# Function to load CSV data
def load_csv():
    try:
        products = []
        with open("products.csv", "r") as file:
            reader = csv.DictReader(file)
            for row in reader:
                row["id"] = int(row["id"])
                row["price"] = float(row["price"])
                products.append(row)
        return products
    except Exception as e:
        return {"error": str(e)}

@app.route('/products')
def products():
    """Route to display product data from JSON or CSV."""
    source = request.args.get('source')
    product_id = request.args.get('id', type=int)

    if source == "json":
        data = load_json()
    elif source == "csv":
        data = load_csv()
    else:
        return render_template("product_display.html", error="Wrong source. Use 'json' or 'csv'.")

    if isinstance(data, dict) and "error" in data:
        return render_template("product_display.html", error=data["error"])

    if product_id:
        filtered_data = [item for item in data if item["id"] == product_id]
        if not filtered_data:
            return render_template("product_display.html", error="Product not found.")
        data = filtered_data

    return render_template("product_display.html", products=data)

if __name__ == "__main__":
    app.run(debug=True)
