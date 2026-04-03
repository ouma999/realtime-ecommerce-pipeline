import psycopg2

def create_table():
    conn = psycopg2.connect(
        host="localhost",
        port="5433",
        database="ecommerce_realtime",
        user="kafka",
        password="kafka"
    )
    cursor = conn.cursor()
    
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS orders (
            order_id VARCHAR(50) PRIMARY KEY,
            customer_name VARCHAR(100),
            product VARCHAR(100),
            category VARCHAR(50),
            price DECIMAL(10,2),
            quantity INTEGER,
            total DECIMAL(10,2),
            status VARCHAR(20),
            timestamp TIMESTAMP
        )
    ''')
    
    conn.commit()
    cursor.close()
    conn.close()
    print("✅ Orders table created successfully!")

if __name__ == "__main__":
    create_table()