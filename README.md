# Voice Auction App

A simple live auction platform with a Flask backend and a Streamlit dashboard.

## Features

- **Flask API** for managing products, bids, and auction stats.
- **Streamlit dashboard** for real-time auction monitoring.
- **SQLite database** for persistent storage.
- **Omnidimension web widget** integration (for chat/support).

## Setup Instructions

### 1. Install Dependencies

```bash
pip install -r requirements.txt
```

### 2. Initialize the Database

```bash
python init_db.py
```

### 3. Run the Flask Backend

```bash
python app.py
```

The backend will start at `http://127.0.0.1:5000/`.

### 4. Run the Streamlit Dashboard

```bash
streamlit run streamlit_app.py
```

The dashboard will open in your browser.

## File Structure

- `app.py` — Flask backend API for products, bids, and stats.
- `init_db.py` — Initializes the SQLite database with schema and sample data.
- `schema.sql` — SQL schema for products and bids tables.
- `streamlit_app.py` — Streamlit dashboard for live auction stats.
- `requirements.txt` — Python dependencies.

## API Endpoints

- `GET /products` — List all products.
- `GET /product/<product_id>` — Get details of a product.
- `POST /bid` — Place a bid (JSON: `product_id`, `amount`, `user`).
- `GET /stats` — Get auction stats for all products.

## Notes

- The Omnidimension widget is embedded in the Streamlit dashboard.
- Make sure both the backend and dashboard are running for full functionality. 