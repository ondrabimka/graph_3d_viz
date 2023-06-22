from typing import Optional

from gqlalchemy import Memgraph, Node, Relationship

db = Memgraph()


class Officer(Node):
    name: Optional[str]
    source: Optional[str]
    country: Optional[str]
    country_codes: Optional[str]
    icij_note: Optional[str]
    icij_id: Optional[str]


class Country(Node):
    name: Optional[str]
    iso_2_code: Optional[str]
    iso_3_code: Optional[str]
    region: Optional[str]
    sub_region: Optional[str]


class Entity(Node):
    name: Optional[str]
    source: Optional[str]
    status: Optional[str]
    status_updated_at: Optional[str]
    registered_at: Optional[str]
    provider: Optional[str]
    jurisdiction_note: Optional[str]
    icij_note: Optional[str]
    icij_id: Optional[str]


class From(Relationship, type="FROM"):
    pass


class Related_to(Relationship, type="RELATED_TO"):
    pass


class Jurisdiction_in(Relationship, type="JURISDICTION_IN"):
    pass


class Officer_of(Relationship, type="OFFICER_OF"):
    pass
