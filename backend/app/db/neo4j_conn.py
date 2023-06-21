import logging

from py2neo import Graph


class Neo4jConnClass(Graph):

    """Class for connecting to Neo4j database

    Parameters
    ----------
    Graph : py2neo.Graph
        Graph object from py2neo library

    Returns
    -------
    Neo4jConnClass
        Neo4jConnClass object

    Examples
    --------
    >>> from neo4j_con import Neo4jConnClass
    >>> neo4j_conn = Neo4jConnClass()
    >>> neo4j_conn
    """

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        logging.info(f"Connected to Neo4j database: {self.name}")
