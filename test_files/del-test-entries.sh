# Script: del-test-entries.sh
# File Type: DB Cleanup
# Author: Marcus X. Kielman
# Description: Deletes Test Entries from Kubernetes Container
export POD_NAME=$(kubectl get pods -o name | grep mariadb)
echo "DELETE FROM payments WHERE checkNumber='HR141523'; DELETE FROM customers WHERE customerNumber=100;" | kubectl exec -i $POD_NAME -- mysql -uroot -proot classicmodels
