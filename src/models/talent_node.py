from dataclasses import dataclass, field
from typing import List

@dataclass
class TalentNode:
    """
    Represents a single talent node within a talent tree, based on the
    'talent_nodes' table schema.
    """
    node_id: int
    tree_id: int  # Foreign key to the TalentTree
    node_name: str
    max_points: int
    description: str
    
    # A list of node_ids that must be unlocked before this one
    dependencies: List[int] = field(default_factory=list)