from dataclasses import dataclass, field
from typing import List, Literal

# Define custom types for ENUM fields to enforce data integrity
Rarity = Literal["Legendary", "Epic", "Elite"]
Faction = Literal["League of Order", "Springwardens", "Wilderburg"]
UnitType = Literal["Infantry", "Cavalry", "Marksman", "Magic", "Overall"]

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