from flask import Flask, jsonify, request
import mariadb

from model.tables import Tables, TableSchema
from model.payments import Payments, PaymentSchema
from model.offices import Offices, OfficeSchema
from model.customers import Customers, CustomerSchema

app = Flask(__name__)

def connect_db():
    try:
        conn = mariadb.connect(
            user="root",
            password="root",
            host="172.18.0.2",
            port=3306,
            database="classicmodels"

        )
        conn.autocommit = True
    except mariadb.Error as e:
        print(f"Error connecting to MariaDB Platform: {e}")
        return False
    else:
        print("successfully connected")
    
    #select column_name from information_schema.columns where table_name='customers'; (use to get column names)
    cur = conn.cursor()
    return cur

@app.route('/get_database_table')
def get_database_table():
    cur = connect_db() if connect_db() is not False else None
    if cur is None:
        return "Database Inaccessible"
    else:
        cur.execute(
            "show tables;"
        )
        table = []
        for i, value in enumerate(cur):
            table.append(Tables(value[0]))

        schema = TableSchema(many=True)
        db = schema.dump(table)
        return jsonify(db)

@app.route('/get_database_table/payments')
def get_payments():
    cur = connect_db() if connect_db() is not False else None
    if cur is None:
        return "Database Inaccessible"
    else:
        cur.execute(
            "SELECT * FROM payments;"
        )
        table = []
        for i in cur:
            table.append(Payments(i[0], i[1], i[2], i[3]))
        schema = PaymentSchema(many=True)
        payments = schema.dump(table)
        return jsonify(payments)

@app.route('/get_database_table/payments', methods=['POST'])
def add_payments():
    payments = PaymentSchema().load(request.get_json())
    cur = connect_db() if connect_db() is not False else None
    if cur is None:
        return "Database Inaccessible"
    else:
        cur.execute(
            "INSERT INTO payments (customerNumber, checkNumber, paymentDate, amount) VALUES (?,?,?,?)",
            (   
                payments.customerNumber,
                payments.checkNumber,
                payments.paymentDate,
                payments.amount
            )
        )
        return "Payment Added to Database", 204

@app.route('/get_database_table/offices')
def get_offices():
    cur = connect_db() if connect_db() is not False else None
    if cur is None:
        return "Database Inaccessible"
    else:
        cur.execute(
            "SELECT * FROM offices;"
        )
        table = []
        for i in cur:
            table.append(Offices(i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[8]))
        schema = OfficeSchema(many=True)
        offices = schema.dump(table)
        return jsonify(offices)

@app.route('/get_database_table/customers')
def get_customers():
    cur = connect_db() if connect_db() is not False else None
    if cur is None:
        return "Database Inaccessible"
    else:
        cur.execute(
            "SELECT * FROM customers;"
        )
        table = []
        for i in cur:
            table.append(Customers(i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[8], i[9], i[10], i[11], i[12]))
        schema = CustomerSchema(many=True)
        customers = schema.dump(table)
        return jsonify(customers)
    
@app.route('/get_database_table/customers', methods=['POST'])
def add_customer():
    customer = CustomerSchema().load(request.get_json())
    cur = connect_db() if connect_db() is not False else None
    if cur is None:
        return "Database Inaccessible"
    else:
        cur.execute(
            "INSERT INTO customers (customerNumber, customerName, contactLastName, contactFirstName, phone, addressLine1, addressLine2, city, state, postalCode, country, salesRepEmployeeNumber, creditLimit) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)",
            (
                customer.customerNumber,
                customer.customerName,
                customer.contactLastName,
                customer.contactFirstName,
                customer.phone,
                customer.addressLine1,
                customer.addressLine2,
                customer.city,
                customer.state,
                customer.postalCode,
                customer.country,
                customer.salesRepEmployeeNumber,
                customer.creditLimit
            )
        )
        return "Customer Successfully Added", 204

@app.route('/')
def hello():
    return "Hello Welcome To My API"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080, debug=True)
