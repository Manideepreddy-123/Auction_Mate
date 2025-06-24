import streamlit as st
import requests
import streamlit.components.v1 as components

st.title("📈 Live Auction Dashboard")

try:
    response = requests.get("http://127.0.0.1:5000/stats")
    response.raise_for_status()
    stats = response.json()
    for item in stats:
        st.subheader(item["name"])
        st.write(f"Total Bids: {item['total_bids']}")
        st.write(f"Highest Bid: ₹{item['highest_bid']}")
except requests.exceptions.RequestException:
    st.error("Failed to fetch data from backend.")

# Embedding the Omnidimension web widget
components.html(
    """
    <script id="omnidimension-web-widget" async src="https://backend.omnidim.io/web_widget.js?secret_key=ef407a0608d6d2b32851df6c8c2e271d"></script>
    """,
    height=300,  # Increase height to make the widget visible
    scrolling=True,
)
