#!/bin/bash
curl http://localhost:5000/get_database_table
curl http://localhost:5000/get_database_table/payments
curl http://localhost:5000/get_database_table/customers
curl http://localhost:5000/get_database_table/offices

curl -X POST -H "Content-Type: application/json" -d '{
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
    "salesRepEmployeeNumber": 1002,
    "creditLimit": "26000.44"
}' http://localhost:5000/get_database_table/customers

curl -X POST -H "Content-Type: application/json" -d '{
    "customerNumber": 103,
    "checkNumber": "HR141523",
    "paymentDate": "2020-01-23",
    "amount": 1234.56
}' http://localhost:5000/get_database_table/payments