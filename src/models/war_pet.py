from dataclasses import dataclass
from .common_types import PetRarity, PetAttribute # <-- UPDATED IMPORT

@dataclass
class WarPet:
    """
    Represents a single War Pet, based on the 'war_pets' table schema.
    """
    pet_id: int
    pet_name: str
    rarity_de_facto: PetRarity
    primary_attribute: PetAttribute
    talent_skill_id: int  # Foreign key to the pet's unique talent skill