from gqlalchemy import Memgraph, Node, Relationship

"""
This file contains the models for the graph database. Not used in the current version of the project.
"""

db = Memgraph()


class Person(Node):
    id: int
    name: str


class knows(Relationship, type="KNOWS"):
    pass
