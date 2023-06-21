#!/bin/bash

echo "Running load.sh"

# Check if CSV files actor exists
if [ ! -f "import/people_nodes.csv" ]; then
  echo "CSV file not found in directory."
  exit 1
fi

echo "Importing CSV files into memgraph."

LOAD CSV FROM "import/people_nodes.csv" WITH HEADER AS row CREATE (p:Person {id: row.id, name: row.name});
CREATE INDEX ON :Person(id);
LOAD CSV FROM "import/people_relationships.csv" WITH HEADER AS row MATCH (p1:Person {id: row.id_from}), (p2:Person {id: row.id_to}) CREATE (p1)-[:IS_FRIENDS_WITH]->(p2);
