from dataclasses import dataclass

@dataclass
class TalentTree:
    """
    Represents a single talent tree, based on the 'talent_trees' table schema.
    This serves as a master record for a given tree (e.g., 'Magic', 'Tank').
    """
    tree_id: int
    tree_name: str
    description: str