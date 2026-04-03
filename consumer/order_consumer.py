import json
import psycopg2
from kafka import KafkaConsumer
from datetime import datetime

def connect_db():
    return psycopg2.connect(
        host="localhost",
        port="5433",
        database="ecommerce_realtime",
        user="kafka",
        password="kafka"
    )

def save_order(conn, order):
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO orders 
        (order_id, customer_name, product, category, price, quantity, total, status, timestamp)
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
        ON CONFLICT (order_id) DO NOTHING
    ''', (
        order['order_id'],
        order['customer_name'],
        order['product'],
        order['category'],
        order['price'],
        order['quantity'],
        order['total'],
        order['status'],
        order['timestamp']
    ))
    conn.commit()
    cursor.close()

def main():
    print("🚀 Starting Order Consumer...")
    print("Waiting for orders...\n")

    consumer = KafkaConsumer(
        'orders',
        bootstrap_servers=['localhost:9092'],
        value_deserializer=lambda x: json.loads(x.decode('utf-8')),
        auto_offset_reset='earliest',
        group_id='order-group'
    )

    conn = connect_db()

    for message in consumer:
        order = message.value
        save_order(conn, order)
        print(f"✅ Order saved: {order['order_id']} | {order['customer_name']} | {order['product']} | ${order['total']}")

if __name__ == "__main__":
    main()