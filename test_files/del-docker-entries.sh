# Script: del-docker-entries.sh
# File Type: DB Cleanup
# Author: Marcus X. Kielman
# Description: Deletes Test Entries from Docker Container
echo "DELETE FROM payments WHERE checkNumber='HR141523'; DELETE FROM customers WHERE customerNumber=100;" | docker exec -i mariadb mysql -uroot -proot classicmodels