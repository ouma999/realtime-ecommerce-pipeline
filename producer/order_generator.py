import json
import time
import random
from datetime import datetime
from faker import Faker
from kafka import KafkaProducer

fake = Faker()

# Products list
PRODUCTS = [
    {"name": "Laptop", "category": "Electronics", "price": 999.99},
    {"name": "Phone", "category": "Electronics", "price": 699.99},
    {"name": "Headphones", "category": "Electronics", "price": 199.99},
    {"name": "T-Shirt", "category": "Clothing", "price": 29.99},
    {"name": "Jeans", "category": "Clothing", "price": 59.99},
    {"name": "Sneakers", "category": "Footwear", "price": 89.99},
    {"name": "Watch", "category": "Accessories", "price": 249.99},
    {"name": "Backpack", "category": "Accessories", "price": 79.99},
]

def generate_order():
    product = random.choice(PRODUCTS)
    quantity = random.randint(1, 5)
    return {
        "order_id": str(fake.uuid4()),
        "customer_name": fake.name(),
        "product": product["name"],
        "category": product["category"],
        "price": product["price"],
        "quantity": quantity,
        "total": round(product["price"] * quantity, 2),
        "status": random.choice(["pending", "confirmed", "shipped"]),
        "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }

def main():
    producer = KafkaProducer(
        bootstrap_servers=['localhost:9092'],
        value_serializer=lambda x: json.dumps(x).encode('utf-8')
    )

    print("🚀 Starting Order Generator...")
    print("Generating orders every 2 seconds. Press CTRL+C to stop.\n")

    while True:
        order = generate_order()
        producer.send('orders', value=order)
        print(f"✅ Order sent: {order['order_id']} | {order['customer_name']} | {order['product']} | ${order['total']}")
        time.sleep(2)

if __name__ == "__main__":
    main()