# Module: kube_test
# File Type: Test Module
# Author: Marcus X. Kielman
# Description: Unit Testing for Flask API and Database in Kubernetes
import unittest
import requests


# ========================================================================
# Description: Tests GET Requests to Database:
#                http://localhost:9090/get_database_table
#                http://localhost:9090/get_database_table/payments
#                http://localhost:9090/get_database_table/customers
#                http://localhost:9090/get_database_table/offices
#       Input: Null
#      Output: Pass on 200 Code and Failure/Error on Inaccessible Database
class GetTestCases(unittest.TestCase):
    def test_get_database_tables(self):
        r = requests.get(
                'http://192.168.1.233:9090/get_database_table'
            )
        self.assertNotEqual(r.json(), "Database Inaccessible")
        self.assertEqual(r.status_code, 200)

    def test_get_payments(self):
        r = requests.get(
                'http://192.168.1.233:9090/get_database_table/payments'
            )
        self.assertNotEqual(r.json(), "Database Inaccessible")
        self.assertEqual(r.status_code, 200)

    def test_get_customers(self):
        r = requests.get(
                'http://192.168.1.233:9090/get_database_table/customers'
            )
        self.assertNotEqual(r.json(), "Database Inaccessible")
        self.assertEqual(r.status_code, 200)

    def test_get_offices(self):
        r = requests.get(
                'http://192.168.1.233:9090/get_database_table/offices'
            )
        self.assertNotEqual(r.json(), "Database Inaccessible")
        self.assertEqual(r.status_code, 200)


# ========================================================================
# Description: Tests Incorrect POST Requests to Database:
#                http://localhost:9090/get_database_table/payments
#                http://localhost:9090/get_database_table/customers
#       Input: Null
#      Output: Pass on 500 Code Failure/Error on Inaccessible Database
class InPostTestCases(unittest.TestCase):
    def test_in_add_customer(self):
        # Test POST Requests with Unknown Database Entries
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
        r = requests.post(
                'http://192.168.1.233:9090/get_database_table/customers',
                json=data
            )
        self.assertEqual(r.status_code, 500)

        # Test POST Requests with Missing Database Entries
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
        r = requests.post(
                'http://192.168.1.233:9090/get_database_table/customers',
                json=data
            )
        self.assertEqual(r.status_code, 500)

    def test_in_add_payment(self):
        # Tests POST Requests with Unknown Database Entries
        data = {
                "customerNumber": 100,
                "checkNumber": "HR141523",
                "paymentDate": "2020-01-23",
                "amount": 1234.56
        }
        r = requests.post(
                'http://192.168.1.233:9090/get_database_table/payments',
                json=data
            )
        self.assertEqual(r.status_code, 500)

        # Test POST Request With Missing Entries
        data = {
                "customerNumber": 103,
                "checkNumber": "HR141523",
                "amount": 1234.56
        }
        r = requests.post(
                'http://192.168.1.233:9090/get_database_table/payments',
                json=data
            )
        self.assertEqual(r.status_code, 500)


# ========================================================================
# Description: Tests Incorrect POST Requests to Database:
#                http://localhost:9090/get_database_table/payments
#                http://localhost:9090/get_database_table/customers
#       Input: Null
#      Output: Pass on 204 Code Failure/Error on Inaccessible Database
class PostTestCases(unittest.TestCase):
    def test_add_customer(self):
        data = {
                "customerNumber": 103,
                "checkNumber": "HR141523",
                "paymentDate": "2020-01-23",
                "amount": 1234.56
        }
        r = requests.post(
                'http://192.168.1.233:9090/get_database_table/payments',
                json=data
            )
        self.assertEqual(r.status_code, 204)

    def test_add_payment(self):
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
        r = requests.post(
                'http://192.168.1.233:9090/get_database_table/customers',
                json=data
            )
        print(r.text)
        self.assertEqual(r.status_code, 204)


unittest.main()
