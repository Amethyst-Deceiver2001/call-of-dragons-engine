from dataclasses import dataclass, field
from typing import Dict
from .common_types import PetRarity, PetAttribute

@dataclass
class WarPet:
    """
    Represents a single War Pet, merging the approved schema with an
    improved attribute model to support synergy analysis.
    """
    pet_id: int
    pet_name: str

    # Kept from our original schema to model accessibility and for reference
    rarity_de_facto: PetRarity
    primary_attribute: PetAttribute
    
    # Kept from our original schema, linking to the pet's unique skill
    talent_skill_id: int

    # Integrated from the new suggestion - This is crucial for optimization logic
    base_attributes: Dict[PetAttribute, int] = field(default_factory=dict)