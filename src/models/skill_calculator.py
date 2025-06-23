from src.models.common_types import Rarity

# Data for token costs per skill level.
# NOTE: These are placeholder values. We will need to populate this with
# verified data from in-game for Legendary, Epic, and Elite heroes.
TOKEN_COSTS = {
    "Legendary": {1: 10, 2: 10, 3: 15, 4: 15},
    "Epic": {1: 10, 2: 10, 3: 10, 4: 10},
    "Elite": {1: 5, 2: 5, 3: 5, 4: 5},
}

def calculate_tokens_needed(current_level: int, rarity: Rarity) -> int:
    """
    Calculates the total number of hero tokens required to max a skill
    from its current level. A skill is maxed at level 5.

    Args:
        current_level: The current level of the skill (1-4).
        rarity: The rarity of the hero, which determines token cost.

    Returns:
        The total number of tokens needed to get from current_level to level 5.
    """
    if current_level >= 5:
        return 0

    total_tokens = 0
    # The loop starts from the current level and goes up to level 4,
    # as these are the levels that require tokens to advance.
    for level in range(current_level, 5):
        total_tokens += TOKEN_COSTS[rarity].get(level, 0)
    
    return total_tokens