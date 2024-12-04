from flask import Flask, render_template, request
import mysql.connector

app = Flask(__name__)

# MySQL connection details
dbconfig = {
    'host': '127.0.0.1',
    'user': 'root',
    'password': 'zach9096',
    'database': 'SchoolEnrollmentDB'
}

@app.route('/')
def index():
    # Render the home page
    return render_template('index.html')

@app.route('/execute-query', methods=['POST'])
def execute_query():
    # Get the query from the form
    query = request.form['query']
    conn = mysql.connector.connect(**dbconfig)
    cursor = conn.cursor()
    results = None

    try:
        # Execute the query
        cursor.execute(query)

        # If the query produces results (e.g., SELECT):
        if cursor.description:
            columns = [desc[0] for desc in cursor.description]
            rows = cursor.fetchall()
            results = {'columns': columns, 'rows': rows}
        else:
            # If the query modifies data (e.g., INSERT, UPDATE, DELETE):
            conn.commit()
            results = {'message': f"Query executed successfully. {cursor.rowcount} rows affected."}
    except Exception as e:
        # Handle any errors
        results = {'message': f"Error: {str(e)}"}
    finally:
        cursor.close()
        conn.close()

    # Render the page with the results
    return render_template('index.html', results=results)

if __name__ == '__main__':
    app.run(debug=True)
