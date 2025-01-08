from flask import Flask, render_template
import random
from datetime import datetime, timedelta

app = Flask(__name__)

# Stock Data
STOCK_DATA = {
    "RELIANCE": {
        "company_name": "Reliance Industries",
        "price": 2500,
        "market_cap": 1700000,
        "logo": "https://upload.wikimedia.org/wikipedia/en/thumb/4/4e/Reliance_Industries_Logo.svg/512px-Reliance_Industries_Logo.svg.png",
    },
    "TCS": {
        "company_name": "Tata Consultancy Services",
        "price": 3500,
        "market_cap": 1300000,
        "logo": "https://upload.wikimedia.org/wikipedia/commons/thumb/2/2f/Tata_Consultancy_Services_Logo.svg/512px-Tata_Consultancy_Services_Logo.svg.png",
    },
    "INFY": {
        "company_name": "Infosys",
        "price": 1500,
        "market_cap": 800000,
        "logo": "https://upload.wikimedia.org/wikipedia/commons/thumb/d/d2/Infosys_logo.svg/512px-Infosys_logo.svg.png",
    },
    "HDFCBANK": {
        "company_name": "HDFC Bank",
        "price": 1200,
        "market_cap": 1000000,
        "logo": "https://upload.wikimedia.org/wikipedia/commons/thumb/6/61/HDFC_Bank_Logo.svg/512px-HDFC_Bank_Logo.svg.png",
    },
    "ICICIBANK": {
        "company_name": "ICICI Bank",
        "price": 1000,
        "market_cap": 950000,
        "logo": "https://upload.wikimedia.org/wikipedia/commons/thumb/1/10/ICICI_Bank_Logo.svg/512px-ICICI_Bank_Logo.svg.png",
    },
    "SBIN": {
        "company_name": "State Bank of India",
        "price": 600,
        "market_cap": 600000,
        "logo": "https://upload.wikimedia.org/wikipedia/commons/thumb/5/5e/State_Bank_of_India_logo.svg/512px-State_Bank_of_India_logo.svg.png",
    },
    "MARUTI": {
        "company_name": "Maruti Suzuki",
        "price": 8000,
        "market_cap": 250000,
        "logo": "https://upload.wikimedia.org/wikipedia/commons/thumb/8/8e/Maruti_Suzuki_Logo.svg/512px-Maruti_Suzuki_Logo.svg.png",
    },
    "WIPRO": {
        "company_name": "Wipro",
        "price": 450,
        "market_cap": 500000,
        "logo": "https://upload.wikimedia.org/wikipedia/commons/thumb/f/fa/Wipro_Primary_Logo_Color.svg/512px-Wipro_Primary_Logo_Color.svg.png",
    },
    "ITC": {
        "company_name": "ITC",
        "price": 350,
        "market_cap": 300000,
        "logo": "https://upload.wikimedia.org/wikipedia/commons/thumb/9/93/ITC_Limited_logo.svg/512px-ITC_Limited_logo.svg.png",
    },
    "HCLTECH": {
        "company_name": "HCL Technologies",
        "price": 1100,
        "market_cap": 650000,
        "logo": "https://upload.wikimedia.org/wikipedia/commons/thumb/e/e4/HCLTech_Logo.svg/512px-HCLTech_Logo.svg.png",
    },
    "ADANIENT": {
        "company_name": "Adani Enterprises",
        "price": 1500,
        "market_cap": 1800000,
        "logo": "https://upload.wikimedia.org/wikipedia/en/thumb/5/52/Adani_Enterprises_logo.svg/512px-Adani_Enterprises_logo.svg.png",
    },
    "BAJAJFINSV": {
        "company_name": "Bajaj Finserv",
        "price": 1700,
        "market_cap": 1400000,
        "logo": "https://upload.wikimedia.org/wikipedia/commons/thumb/2/2f/Bajaj_Finserv_logo.svg/512px-Bajaj_Finserv_logo.svg.png",
    },
    "TITAN": {
        "company_name": "Titan Company",
        "price": 2500,
        "market_cap": 500000,
        "logo": "https://upload.wikimedia.org/wikipedia/commons/thumb/1/16/Titan_Company_Logo.svg/512px-Titan_Company_Logo.svg.png",
    },
    "ONGC": {
        "company_name": "Oil and Natural Gas Corporation",
        "price": 160,
        "market_cap": 900000,
        "logo": "https://upload.wikimedia.org/wikipedia/en/thumb/9/95/ONGC_Logo.svg/512px-ONGC_Logo.svg.png",
    },
    "COALINDIA": {
        "company_name": "Coal India",
        "price": 200,
        "market_cap": 150000,
        "logo": "https://upload.wikimedia.org/wikipedia/commons/thumb/6/6d/Coal_India_Logo.svg/512px-Coal_India_Logo.svg.png",
    },
    "NTPC": {
        "company_name": "NTPC Limited",
        "price": 180,
        "market_cap": 750000,
        "logo": "https://upload.wikimedia.org/wikipedia/commons/thumb/f/f2/NTPC_Logo.svg/512px-NTPC_Logo.svg.png",
    },
    "POWERGRID": {
        "company_name": "Power Grid Corporation",
        "price": 250,
        "market_cap": 350000,
        "logo": "https://upload.wikimedia.org/wikipedia/commons/thumb/4/49/Power_Grid_Corporation_logo.svg/512px-Power_Grid_Corporation_logo.svg.png",
    },
    "BPCL": {
        "company_name": "Bharat Petroleum Corporation",
        "price": 350,
        "market_cap": 300000,
        "logo": "https://upload.wikimedia.org/wikipedia/commons/thumb/9/92/Bharat_Petroleum_logo.svg/512px-Bharat_Petroleum_logo.svg.png",
    },
    "ASIANPAINT": {
        "company_name": "Asian Paints",
        "price": 3200,
        "market_cap": 220000,
        "logo": "https://upload.wikimedia.org/wikipedia/commons/thumb/5/51/Asian_Paints_logo.svg/512px-Asian_Paints_logo.svg.png",
    },
}

# Simulated News Data
NEWS_DATA = {
    "RELIANCE": [
        {"title": "Reliance leads renewable energy investments", "description": "Reliance Industries is now a leader in renewable energy.", "url": "#", "published_at": "2025-01-07"},
        {"title": "Record profits reported this quarter", "description": "Reliance Industries has exceeded market expectations.", "url": "#", "published_at": "2025-01-06"},
    ],
}

# Generate simulated stock history
def generate_stock_history(price):
    return [
        {"date": (datetime.now() - timedelta(days=i)).strftime("%Y-%m-%d"), "price": round(price * (0.95 + random.uniform(0, 0.1)), 2)}
        for i in range(7)
    ]

@app.route("/")
def index():
    return render_template("index.html", companies=STOCK_DATA)

@app.route("/stock/<symbol>")
def stock_detail(symbol):
    stock = STOCK_DATA.get(symbol.upper())
    if not stock:
        return "Stock not found", 404

    history = generate_stock_history(stock["price"])
    dates = [entry["date"] for entry in history]
    prices = [entry["price"] for entry in history]
    news = NEWS_DATA.get(symbol.upper(), [])
    return render_template("stock_detail.html", stock=stock, dates=dates, prices=prices, news=news)

if __name__ == "__main__":
    app.run(debug=True)
