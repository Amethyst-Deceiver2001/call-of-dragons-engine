from dataclasses import dataclass, field
from typing import List, Dict, Any, Literal

# Define a custom type for the skill's category
SkillType = Literal["Active", "Passive", "Awakened"]

@dataclass
class HeroSkill:
    """
    Represents a single hero skill, based on the 'hero_skills' table schema.
    This structure is vital for querying specific skill effects. 
    """
    skill_id: int
    hero_id: int # Foreign key to the Hero
    skill_name: str
    skill_type: SkillType
    skill_order: int # The order the skill unlocks, from 1 to 5 
    description: str
    
    # Represents the JSON object for scaling values (e.g., damage_factor) 
    scaling_values: Dict[str, Any] = field(default_factory=dict)
    
    # Machine-readable tags for buffs, debuffs, or triggers 
    effects: List[str] = field(default_factory=list)