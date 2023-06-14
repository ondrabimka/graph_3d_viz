#!/bin/bash

echo "Running load.sh"

if [ ! -f "import/customers.csv" ]; then
  echo "CSV file not found in directory."
  exit 1
fi

echo "Loading data"
neo4j-admin database import full neo4j --nodes=import/customers.csv --delimiter="," --overwrite-destination=true
