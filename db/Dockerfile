#!/bin/bash
FROM memgraph/memgraph-platform:latest

COPY import/ import/
COPY load.sh /load.sh

RUN chmod +x /load.sh
RUN echo "DONE"

# run load.sh in the background after waiting for memgraph to start
ENTRYPOINT ["/bin/bash", "-c", "sleep 10 && /load.sh & /usr/bin/supervisord"]
