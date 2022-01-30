# Script: kube-run
# File Type: Run and Test
# Author: Marcus X. Kielman
# Description: Opens Port Forwarding for API in Kubernetes, and runs Tests
#!/bin/bash
kubectl port-forward service/devops-api 9090:9090 --address "192.168.1.233" &
sleep 5s
python3 kube_test.py
del-test-entries.sh       #Deletes Test Entries from Database