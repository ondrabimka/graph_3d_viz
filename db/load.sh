#!/bin/bash

echo "Running load.sh"

# Check if CSV file people_nodes.csv and people_relationships exists in the import directory.
if [ -f /import/people_nodes.csv ] && [ -f /import/people_relationships.csv ]; then
    # Import CSV files into memgraph.
    echo "Importing CSV files into memgraph."
    echo "LOAD CSV FROM '/import/people_nodes.csv' NO HEADER AS row CREATE (p:Person {person_id: row[0], name: row[1]});" | mgconsole
    echo "LOAD CSV FROM '/import/people_relationships.csv' NO HEADER AS row MATCH (p1:Person {person_id: row[0]}), (p2:Person {person_id: row[1]}) CREATE (p1)-[:KNOWS]->(p2);" | mgconsole
    echo "Finished importing CSV files into memgraph."
else
    echo "CSV files not found in the import directory."
fi
