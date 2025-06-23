from typing import Literal

# Shared types for Heroes
Rarity = Literal["Legendary", "Epic", "Elite"]
Faction = Literal["League of Order", "Springwardens", "Wilderburg"]
UnitType = Literal["Infantry", "Cavalry", "Marksman", "Magic", "Overall"]
SkillType = Literal["Active", "Passive", "Awakened"]

# Shared types for War Pets
PetRarity = Literal["Common", "Rare", "Event-Exclusive", "Prestigious"]
PetAttribute = Literal["Strength", "Agility", "Intelligence", "Endurance", "Luck", "Spirit"]
DamageType = Literal["Physical", "Magic", "Healing", "Buff", "N/A"]