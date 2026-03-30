from flask import Flask
import mysql.connector
import os

app = Flask(__name__)

def get_db_connection():
    return mysql.connector.connect(
        host=os.environ.get("DB_HOST"),
        user=os.environ.get("DB_USER"),
        password=os.environ.get("DB_PASSWORD"),
        database=os.environ.get("DB_NAME")
    )

@app.route("/")
def home():
    try:
        conn = get_db_connection()
        cursor = conn.cursor()

        # Create table
        cursor.execute("CREATE TABLE IF NOT EXISTS users (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(50))")

        # Insert data
        cursor.execute("INSERT INTO users (name) VALUES ('Pradeep')")
        conn.commit()

        # Fetch data
        cursor.execute("SELECT * FROM users")
        data = cursor.fetchall()

        return f"DB Connected ✅ Data: {data}"

    except Exception as e:
        return f"DB Connection Failed ❌ {e}"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
