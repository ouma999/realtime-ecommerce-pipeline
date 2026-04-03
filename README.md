# ⚡ Real-Time E-Commerce Streaming Pipeline

A real-time data streaming pipeline that generates e-commerce orders every 2 seconds, streams them through Apache Kafka, stores them in PostgreSQL, and visualizes them in a live Metabase dashboard.

---

## 🏗️ Architecture
```
Fake Order Generator → Kafka Topic → Python Consumer → PostgreSQL → Metabase Dashboard
     (Producer)          (Stream)      (Consumer)       (Storage)    (Visualization)
```

---

## 🛠️ Tech Stack
| Tool | Purpose |
|------|---------|
| Apache Kafka | Real-time data streaming |
| Zookeeper | Kafka cluster management |
| Python | Order generation & consumption |
| PostgreSQL | Data storage |
| Metabase | Real-time dashboard & visualization |
| Docker | Containerization |

---

## 📁 Project Structure
```
realtime-ecommerce/
├── producer/
│   └── order_generator.py  # Generates fake orders every 2 seconds
├── consumer/
│   └── order_consumer.py   # Consumes orders from Kafka & saves to PostgreSQL
├── database/
│   └── db_setup.py         # Creates PostgreSQL tables
└── docker-compose.yml      # Docker configuration
```

---

## 🚀 How to Run

### Prerequisites
- Docker Desktop installed
- Python 3.x installed

### Steps

1. Clone the repository:
```bash
git clone https://github.com/ouma999/realtime-ecommerce-pipeline.git
cd realtime-ecommerce-pipeline
```

2. Create virtual environment:
```bash
python3 -m venv .venv
source .venv/bin/activate
```

3. Install dependencies:
```bash
pip install kafka-python faker psycopg2-binary
```

4. Start Docker containers:
```bash
docker-compose up -d
```

5. Set up the database:
```bash
python3 database/db_setup.py
```

6. Start the Consumer (Terminal 1):
```bash
python3 consumer/order_consumer.py
```

7. Start the Producer (Terminal 2):
```bash
python3 producer/order_generator.py
```

---

## 📊 Metabase Dashboard

Open **http://localhost:3000** and connect to PostgreSQL:
```
Host:     <postgres-container-ip>
Port:     5432
Database: ecommerce_realtime
Username: kafka
Password: kafka123
```

### Dashboard Charts
- 📊 Orders by Category
- 🥧 Revenue by Category
- 📈 Orders Over Time
- 🏆 Top Selling Products
- 🔄 Orders by Status
- 💰 Total Revenue
- 📦 Average Order Value

---

## 📦 Sample Data
```json
{
  "order_id": "abc-123",
  "customer_name": "John Doe",
  "product": "Laptop",
  "category": "Electronics",
  "price": 999.99,
  "quantity": 1,
  "total": 999.99,
  "status": "confirmed",
  "timestamp": "2024-01-01 12:00:00"
}
```

---

## 📚 What I Learned
- Real-time data streaming with Apache Kafka
- Building Kafka Producers & Consumers in Python
- Database management with PostgreSQL
- Data visualization with Metabase
- Containerization with Docker

---

## 🔜 Next Steps
- Add Apache Spark for large-scale processing
- Deploy to AWS or GCP
- Connect real e-commerce APIs (Shopify, WooCommerce)
- Add data quality checks
