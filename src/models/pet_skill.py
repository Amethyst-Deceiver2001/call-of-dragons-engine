from dataclasses import dataclass, field
from typing import List, Optional
from .common_types import PetAttribute, DamageType # <-- UPDATED IMPORT

@dataclass
class PetSkill:
    """
    Represents a single War Pet skill, based on the 'pet_skills' table schema.
    Captures the complex attributes needed for the Pet Optimizer.
    """
    pet_skill_id: int
    skill_name: str
    effect_description: str
    damage_type: DamageType
    primary_attribute: PetAttribute
    
    # A skill may or may not be unique to a specific pet
    associated_pet_id: Optional[int] = None 
    
    damage_healing_factor: str = "" # Stored as string to handle complex values
    
    category: List[str] = field(default_factory=list)
    linked_skills: List[str] = field(default_factory=list)
    acquisition_method: List[str] = field(default_factory=list)