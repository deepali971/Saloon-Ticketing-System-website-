from flask import Flask, render_template, request, redirect, url_for, flash, session
import sqlite3
import pandas as pd
import random
import os

app = Flask(__name__)
app.secret_key = os.environ.get('SECRET_KEY', 'your_secret_key')  # Use environment variable for secret key

# Services and their prices
services = {
    "Hair Cut": 300,
    "Spa": 500,
    "Facial": 350
}

# Database setup
def get_db_connection():
    conn = sqlite3.connect('saloon.db')
    conn.row_factory = sqlite3.Row
    return conn

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if 'username' in session:  # Check if user is already logged in
        return render_template('customer.html')  # Stay on customer page

    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if username == "admin" and password == "password":
            session['username'] = username  # Store username in session
            print(f"User logged in: {session['username']}")  # Debug statement
            return redirect(url_for('customer'))  # Redirect to customer page
        else:
            flash('Invalid username or password')
    return render_template('login.html')

@app.route('/ticket_generation', methods=['GET', 'POST'])
def ticket_generation():
    if request.method == 'POST':
        customer_name = request.form['customer_name']
        selected_services = request.form.getlist('services')
        if not customer_name or not selected_services:
            flash('Please enter customer name and select at least one service')
            return redirect(url_for('ticket_generation'))

        ticket_id = f"TID{random.randint(1000, 9999)}"
        total_amount = sum(services[service] for service in selected_services)
        service_list = ", ".join(selected_services)

        # Insert into database
        conn = get_db_connection()
        conn.execute("INSERT INTO tickets (ticket_id, customer_name, services, total_amount) VALUES (?, ?, ?, ?)",
                     (ticket_id, customer_name, service_list, total_amount))
        conn.commit()
        conn.close()

        # Save to CSV
        ticket_data = {
            "Customer Name": customer_name,
            "Ticket ID": ticket_id,
            "Selected Services": service_list,
            "Total Amount": total_amount
        }
        df = pd.DataFrame([ticket_data])
        df.to_csv("ticket_details.csv", index=False, mode='a', header=not pd.io.common.file_exists("ticket_details.csv"))

        flash(f'Ticket generated: {ticket_id}')
        return redirect(url_for('customer'))  # Redirect to customer page

    return render_template('ticket_generation.html')

@app.route('/customer')
def customer():
    return render_template('customer.html')

@app.route('/logout', methods=['POST'])
def logout():
    session.clear()  # Clear the session
    flash('You have been logged out.')
    return redirect(url_for('index'))  # Redirect to index page

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)  # Changed port for testing
