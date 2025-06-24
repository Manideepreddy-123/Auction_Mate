from flask import Flask, request, jsonify
import sqlite3
from datetime import datetime

app = Flask(__name__)

def db_conn():
    conn = sqlite3.connect("database.db")
    conn.row_factory = sqlite3.Row
    return conn

@app.route("/products", methods=["GET"])
def get_products():
    conn = db_conn()
    cur = conn.cursor()
    cur.execute("SELECT * FROM products")
    products = [dict(row) for row in cur.fetchall()]
    conn.close()
    return jsonify(products)

@app.route("/product/<int:product_id>", methods=["GET"])
def get_product(product_id):
    conn = db_conn()
    cur = conn.cursor()
    cur.execute("SELECT * FROM products WHERE id = ?", (product_id,))
    product = cur.fetchone()
    if not product:
        return jsonify({"error": "Product not found"}), 404
    return jsonify(dict(product))

@app.route("/bid", methods=["POST"])
def post_bid():
    data = request.json
    product_id = data["product_id"]
    bid_amount = data["amount"]
    user = data.get("user", "anonymous")

    conn = db_conn()
    cur = conn.cursor()

    cur.execute("SELECT highest_bid, end_time FROM products WHERE id = ?", (product_id,))
    product = cur.fetchone()
    if not product:
        return jsonify({"error": "Invalid product"}), 404

    if datetime.strptime(product["end_time"], "%Y-%m-%d %H:%M:%S") < datetime.now():
        return jsonify({"error": "Auction ended"}), 403

    if bid_amount <= product["highest_bid"]:
        return jsonify({"error": "Bid too low"}), 400

    cur.execute("INSERT INTO bids (product_id, user, amount) VALUES (?, ?, ?)",
                (product_id, user, bid_amount))
    cur.execute("UPDATE products SET highest_bid = ? WHERE id = ?", (bid_amount, product_id))
    conn.commit()
    conn.close()

    return jsonify({"message": "Bid accepted", "amount": bid_amount})

@app.route("/stats", methods=["GET"])
def get_stats():
    conn = db_conn()
    cur = conn.cursor()
    cur.execute("""
        SELECT 
            products.name,
            COUNT(bids.id) AS total_bids,
            MAX(bids.amount) AS highest_bid
        FROM products
        LEFT JOIN bids ON products.id = bids.product_id
        GROUP BY products.id
    """)
    stats = [dict(row) for row in cur.fetchall()]
    conn.close()
    return jsonify(stats)

if __name__ == "__main__":
    app.run(debug=True)
