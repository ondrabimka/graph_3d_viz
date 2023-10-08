#!/bin/bash

echo "Running load.sh"

if [ -f /import/atp_matches_2023.csv ]; then
    # Import CSV files into memgraph.
    echo "Importing CSV files into memgraph."
    # This cyhper query imports the data from import/file
    echo "LOAD CSV FROM '/import/atp_matches_2023.csv' NO HEADER AS row
            MERGE (p_w: PLAYER {name: row[10]})
            MERGE (p_l: PLAYER {name: row[18]})
            CREATE (p_w)-[df: DEF]->(p_l)
            SET df.score = row[23],
            df.tournament_date = row[5],
            df.duration = row[26],
            df.l_rank = row[47],
            df.w_rank = row[45];" | mgconsole
    echo "Finished importing CSV files into memgraph."
else
    echo "CSV files not found in the import directory."
fi
