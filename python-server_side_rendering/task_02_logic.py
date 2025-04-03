import json
from flask import Flask, render_template

app = Flask(__name__)

def load_items():
    """Load items from the JSON file."""
    with open("items.json", "r") as file:
        data = json.load(file)
    return data.get("items", [])  # Default to an empty list if 'items' is missing

@app.route('/items')
def items():
    """Render the items page with dynamic content."""
    item_list = load_items()
    return render_template('items.html', items=item_list)

if __name__ == '__main__':
    app.run(debug=True, port=5000)
