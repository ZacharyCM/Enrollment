from flask import Flask, render_template
import mysql.connector

app = Flask(__name__)

# MySQL connection details
dbconfig = {
    'host': '127.0.0.1',        # Replace with your MySQL server address
    'user': 'root',             # Replace with your MySQL username
    'password': 'zach9096',     # Replace with your MySQL password
    'database': 'SchoolEnrollmentDB'  # Replace with your MySQL database name
}

@app.route('/')
def index():
    # Connect to MySQL
    conn = mysql.connector.connect(**dbconfig)
    cursor = conn.cursor()

    # Query to show tables
    cursor.execute("SHOW TABLES")
    tables = cursor.fetchall()

    # Close the connection
    cursor.close()
    conn.close()

    return render_template('index.html', tables=tables)

if __name__ == '__main__':
    app.run(debug=True)
