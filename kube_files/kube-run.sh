#!/bin/bash

kubectl port-forward service/devops-api 9090:9090 --address "192.168.1.233" &
python3 test_files/kube_test.py
../test_files/del-test-entries.sh