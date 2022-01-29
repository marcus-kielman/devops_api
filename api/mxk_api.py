# Module: mxk_api
# File Type: Main Module
# Author: Marcus X. Kielman
# Description: Flask Interface for Database Models
from flask import Flask, jsonify, request
import mariadb

from model.tables import Tables, TableSchema
from model.payments import Payments, PaymentSchema
from model.offices import Offices, OfficeSchema
from model.customers import Customers, CustomerSchema

app = Flask(__name__)


# ========================================================================
# Description: Connects Flask API to MariaDB classicmodels database
#                at http://mariadb:3306
#       Input: Null
#      Output: Connect Object to MariaDB on Success and False on Failure
def connect_db():
    try:
        conn = mariadb.connect(
            user="root",
            password="root",
            host="mariadb",
            port=3306,
            database="classicmodels"
        )
        conn.autocommit = True
    except mariadb.Error as e:
        print(f"Error connecting to MariaDB Platform: {e}")
        return False
    else:
        print("successfully connected")

    cur = conn.cursor()
    return cur


# ========================================================================
# Description: Sends GET Request for database tables at
#                http://localhost:8081/get_database_table
#       Input: Null
#      Output: "Database Inaccessible" message on Failure
#              JSON file of database tables on Success
@app.route('/get_database_table')
def get_database_table():
    cur = connect_db() if connect_db() is not False else None
    if cur is None:
        return "Database Inaccessible\n"
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


# ========================================================================
# Description: Sends GET Request for payments table at
#                http://localhost:8081/get_database_table/payments
#       Input: Null
#      Output: "Database Inaccessible" message on Failure
#              JSON file of payments table on Success
@app.route('/get_database_table/payments')
def get_payments():
    cur = connect_db() if connect_db() is not False else None
    if cur is None:
        return "Database Inaccessible\n"
    else:
        cur.execute(
            "SELECT * FROM payments;"
        )

        # Map to Schema format
        table = []
        for i in cur:
            table.append(Payments(i[0], i[1], i[2], i[3]))
        schema = PaymentSchema(many=True)
        payments = schema.dump(table)
        return jsonify(payments)


# ========================================================================
# Description: Sends POST Request for payments table at
#                http://localhost:8081/get_database_table/payments
#       Input: Null
#      Output: "Database Inaccessible" message on Failure
#              204 "Payment Added to Database" message on Success
@app.route('/get_database_table/payments', methods=['POST'])
def add_payments():
    # Map JSON in POST Request to Payment Schema
    payments = PaymentSchema().load(request.get_json())
    cur = connect_db() if connect_db() is not False else None
    if cur is None:
        return "Database Inaccessible\n"
    else:
        # Send JSON POST to Database
        cur.execute(
            "INSERT INTO payments (\
            customerNumber, checkNumber, paymentDate, amount)\
            VALUES (?,?,?,?)",
            (
                payments.customerNumber,
                payments.checkNumber,
                payments.paymentDate,
                payments.amount
            )
        )
        return "Payment Added to Database\n", 204


# ========================================================================
# Description: Sends GET Request for offices table at
#                http://localhost:8081/get_database_table/offices
#       Input: Null
#      Output: "Database Inaccessible" message on Failure
#              JSON file of offices table on Success
@app.route('/get_database_table/offices')
def get_offices():
    cur = connect_db() if connect_db() is not False else None
    if cur is None:
        return "Database Inaccessible\n"
    else:
        cur.execute(
            "SELECT * FROM offices;"
        )

        # Map to Schema for JSON format
        table = []
        for i in cur:
            table.append(Offices(
                                i[0], i[1], i[2], i[3], i[4],
                                i[5], i[6], i[7], i[8]
                        ))
        schema = OfficeSchema(many=True)
        offices = schema.dump(table)
        return jsonify(offices)


# ========================================================================
# Description: Sends GET Request for customers table at
#                http://localhost:8081/get_database_table/customers
#       Input: Null
#      Output: "Database Inaccessible" message on Failure
#              JSON file of customers table on Success
@app.route('/get_database_table/customers')
def get_customers():
    cur = connect_db() if connect_db() is not False else None
    if cur is None:
        return "Database Inaccessible\n"
    else:
        cur.execute(
            "SELECT * FROM customers;"
        )

        # Map to Schema for JSON format
        table = []
        for i in cur:
            table.append(Customers(
                                i[0], i[1], i[2], i[3], i[4], i[5], i[6],
                                i[7], i[8], i[9], i[10], i[11], i[12]
                        ))
        schema = CustomerSchema(many=True)
        customers = schema.dump(table)
        return jsonify(customers)


# ========================================================================
# Description: Sends POST Request for customers table at
#                http://localhost:8081/get_database_table/customers
#       Input: Null
#      Output: "Database Inaccessible" message on Failure
#              204 "Payment Added to Database" message on Success
@app.route('/get_database_table/customers', methods=['POST'])
def add_customer():
    # Map JSON in POST Request to Customer Schema
    customer = CustomerSchema().load(request.get_json())
    cur = connect_db() if connect_db() is not False else None

    if cur is None:
        return "Database Inaccessible\n"
    else:
        # Send JSON POST to Database
        cur.execute(
            "INSERT INTO customers (\
            customerNumber, customerName, contactLastName,\
            contactFirstName, phone, addressLine1, addressLine2,\
            city, state, postalCode, country, salesRepEmployeeNumber,\
            creditLimit)\
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)",

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
        return "Customer Successfully Added\n", 204


# ========================================================================
# Description: Sends GET Request for main API page at
#                http://localhost:8081
#       Input: Null
#      Output: "Hello Welcome To My API" Message
@app.route('/')
def hello():
    return "Hello Welcome To My API\n"


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8081, debug=True)
