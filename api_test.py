import unittest
import requests
import mariadb

class GetTestCases(unittest.TestCase):
    def test_get_database_tables(self):
        r = requests.get('http://172.18.0.3:8081/get_database_table')
        self.assertNotEqual(r.json(), "Database Inaccessible")
        self.assertEqual(r.status_code, 200)

    def test_get_payments(self):
        r = requests.get('http://172.18.0.3:8081/get_database_table/payments')
        self.assertNotEqual(r.json(), "Database Inaccessible")
        self.assertEqual(r.status_code, 200)

    def test_get_customers(self):
        r = requests.get('http://172.18.0.3:8081/get_database_table/customers')
        self.assertNotEqual(r.json(), "Database Inaccessible")
        self.assertEqual(r.status_code, 200)

    def test_get_offices(self):
        r = requests.get('http://172.18.0.3:8081/get_database_table/offices')
        self.assertNotEqual(r.json(), "Database Inaccessible")
        self.assertEqual(r.status_code, 200)

class InPostTestCases(unittest.TestCase):
    def test_in_add_customer(self):
        header = {"Content-Type: application/json",}
        data = {
                "customerNumber": 100,
                "customerName": "Fitz",
                "contactLastName": "Mulligan",
                "contactFirstName": "Patrick",
                "phone": "4125264562",
                "addressLine1": "520 Willford Lane",
                "addressLine2": "1444 University Park",
                "city": "State College",
                "state": "PA",
                "postalCode": 16802,
                "country": "US",
                "salesRepEmployeeNumber": 1000,
                "creditLimit": "26000.44"
        }
        r = requests.post('http://172.18.0.3:8081/get_database_table/customers', json=data)
        self.assertEqual(r.status_code, 500)

        data = {
                "customerNumber": 100,
                "customerName": "Fitz",
                "contactLastName": "Mulligan",
                "contactFirstName": "Patrick",
                "phone": "4125264562",
                "addressLine1": "520 Willford Lane",
                "addressLine2": "1444 University Park",
                "city": "State College",
                "state": "PA",
                "postalCode": 16802,
                "country": "US",
                "creditLimit": "26000.44"
        }
        r = requests.post('http://172.18.0.3:8081/get_database_table/customers', json=data)
        self.assertEqual(r.status_code, 500)

    def test_in_add_payment(self):
        header = {"Content-Type: application/json",}
        data = {
                "customerNumber": 100,
                "checkNumber": "HR141523",
                "paymentDate": "2020-01-23",
                "amount": 1234.56
        }
        r = requests.post('http://172.18.0.3:8081/get_database_table/payments', json=data)
        self.assertEqual(r.status_code, 500)

        data = {
                "customerNumber": 103,
                "checkNumber": "HR141523",
                "amount": 1234.56
        }
        r = requests.post('http://172.18.0.3:8081/get_database_table/payments', json=data)
        self.assertEqual(r.status_code, 500)

class PostTestCases(unittest.TestCase):
    def test_add_customer(self):
        cur = connect_db() if connect_db() is not False else None
        if cur is not None:
            header = {"Content-Type: application/json",}
            data = {
                    "customerNumber": 103,
                    "checkNumber": "HR141523",
                    "paymentDate": "2020-01-23",
                    "amount": 1234.56
            }
            r = requests.post('http://172.18.0.3:8081/get_database_table/payments', json=data)
            self.assertEqual(r.status_code, 204)
            cur.execute(
                "DELETE FROM payments WHERE checkNumber='HR141523';"
            )
        
    def test_add_payment(self):
        cur = connect_db() if connect_db() is not False else None
        if cur is not None:
            header = {"Content-Type: application/json",}
            data = {
                    "customerNumber": 100,
                    "customerName": "Fitz",
                    "contactLastName": "Mulligan",
                    "contactFirstName": "Patrick",
                    "phone": "4125264562",
                    "addressLine1": "520 Willford Lane",
                    "addressLine2": "1444 University Park",
                    "city": "State College",
                    "state": "PA",
                    "postalCode": "16802",
                    "country": "US",
                    "salesRepEmployeeNumber": 1002,
                    "creditLimit": "26000.44"
            }
            r = requests.post('http://172.18.0.3:8081/get_database_table/customers', json=data)
            print(r.text)
            self.assertEqual(r.status_code, 204)
            cur.execute(
                "DELETE FROM customers WHERE customerNumber=100;"
            )

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

unittest.main()