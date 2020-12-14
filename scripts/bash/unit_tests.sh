#!/bin/bash

# unit_tests.sh
# Runs unit tests and prints results toa file with a datetime stamp

cd ../../tests
pytest -v
date
cd ../scripts/Bash