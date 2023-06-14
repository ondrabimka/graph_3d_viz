#!/bin/bash
FROM neo4j:5.8.0-community

COPY import/ import/
COPY load.sh import/load.sh

RUN chmod +x import/load.sh
RUN /bin/bash -c "import/load.sh"
