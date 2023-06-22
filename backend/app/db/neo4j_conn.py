from typing import Any, Dict, Iterator

from gqlalchemy import Memgraph


class GraphConnClass(Memgraph):

    """
    Class for connecting to the graph database

    Parameters
    ----------
    host : str
        Hostname of the graph database

    port : int
        Port of the graph database

    username : str
        Username of the graph database

    password : str
        Password of the graph database

    Returns
    -------
    None
    """

    def __init__(self, host, port, username, password):
        super().__init__(host, port, username, password)

        print("Connecting to graph database...")

    def _select_all_nodes(self) -> Iterator[Dict[str, Any]]:
        """
        Selects the whole graph

        Parameters
        ----------
        None

        Yields
        -------
        Iterator[Dict[str, Any]]
            Iterator all nodes in the graph
        """

        query = """
        MATCH (n)
        RETURN n
        """
        return self.execute_and_fetch(query)

    def _select_all_relationships(self) -> Iterator[Dict[str, Any]]:
        """
        Selects the whole graph

        Parameters
        ----------
        None

        Yields
        -------
        Iterator[Dict[str, Any]]
            Iterator all relationships in the graph
        """

        query = """
        MATCH ()-[r]->()
        RETURN distinct(r) as r
        """
        return self.execute_and_fetch(query)

    def _select_whole_graph(self):
        """
        Select the whole graph from the database

        Parameters
        ----------
        None

        Returns
        -------
        Dict[str, Any]
            Dictionary of the whole graph
        """

        query = """
        MATCH (n)-[r]->(m)
        RETURN n, r, m
        """
        return self.execute_and_fetch(query)

    def get_whole_graph(self) -> Dict[str, Any]:

        """
        Get the whole graph from the database

        Parameters
        ----------
        None

        Returns
        -------
        Dict[str, Any]
            Dictionary of the whole graph
        """

        nodes = []
        relationships = []

        for node in self._select_all_nodes():
            nodes.append({"id": node["n"]._id, "name": node["n"].name, "label": list(node["n"]._labels)[0]})

        for relationship in self._select_all_relationships():
            relationships.append({"source": relationship["r"]._start_node_id, "target": relationship["r"]._end_node_id})

        return {"nodes": nodes, "links": relationships}

    @property
    def number_of_nodes(self) -> int:
        """
        Get the number of nodes in the graph

        Parameters
        ----------
        None

        Returns
        -------
        int
            Number of nodes in the graph
        """

        query = """
        MATCH (n)
        RETURN count(distinct(n)) as count
        """
        return next(self.execute_and_fetch(query))["count"]

    @property
    def number_of_relationships(self) -> int:
        """
        Get the number of relationships in the graph

        Parameters
        ----------
        None

        Returns
        -------
        int
            Number of relationships in the graph
        """

        query = """
        MATCH ()-[r]->()
        RETURN count(distinct(r)) as count
        """
        return next(self.execute_and_fetch(query))["count"]
