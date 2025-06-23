from dataclasses import dataclass, field
from typing import List
from .common_types import Rarity, Faction, UnitType # <-- UPDATED IMPORT

@dataclass
class Hero:
    """
    Represents a single hero, based on the 'heroes' table schema.
    """
    hero_id: int
    hero_name: str
    rarity: Rarity
    faction: Faction
    unit_type: UnitType
    roles: List[str] = field(default_factory=list)
    acquisition_methods: List[str] = field(default_factory=list)
    
    # Links to the talent trees this hero can access
    talent_tree_ids: List[int] = field(default_factory=list)