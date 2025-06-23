# Call of Dragons Engine

![Status](https://img.shields.io/badge/Status-Active%3A%20Data%20Population-blue)
![Python](https://img.shields.io/badge/Python-3.11-blue.svg)
![Framework](https://img.shields.io/badge/Framework-Streamlit-red)

[cite_start]This repository contains the source code for the Call of Dragons Engine, a data-driven analytical tool designed to provide deep, actionable strategic insights for the game "Call of Dragons." 

[cite_start]The project's goal is to move beyond simple tier lists and build a sophisticated engine that understands the complex, synergistic relationships between all in-game systems. 

## Core Analytical Principles

This engine is built on a set of core principles derived from an in-depth analysis of the game's mechanics:

* [cite_start]**The Legion as the Core Unit**: The fundamental unit of strategic analysis is the "Legion," a complete combat entity composed of a primary hero, secondary hero, talent build, artifact, and War Pet.  [cite_start]The engine's primary function is to find optimal Legion compositions, not just "best in slot" items. 
* [cite_start]**Synergy is Paramount**: The engine's logic is designed to programmatically identify and rank powerful synergies between hero skills, talent builds, and War Pet triggers.  [cite_start]For example, it recognizes how Madeline's shield-granting ability directly empowers a Frostbear's damage output. 
* [cite_start]**Accessibility-Adjusted Power**: The engine considers the "power-to-investment ratio" of any given hero or item.  [cite_start]It understands that a highly accessible Epic hero can be more valuable to a player than a resource-intensive Legendary hero, and its recommendations reflect this reality. 
* [cite_start]**Probabilistic Modeling**: The engine accounts for the game's random skill upgrade mechanism, with planned features designed to model the probabilities and expected resource costs associated with different upgrade paths (e.g., the "5-1-1-1" strategy). 

## Features

The Minimum Viable Product (MVP) is focused on delivering two core analytical tools:

1.  [cite_start]**Skill XP Calculator**: An advanced tool designed to model hero progression, including leveling, starring up, and talent point allocation.  [cite_start]It will help users visualize the resource trade-offs of different hero development strategies. 
2.  [cite_start]**Pet Optimizer**: A feature designed to solve the "Tri-Factor Problem" of War Pet optimization by recommending the best pet, skills, and hero pairing based on synergistic relationships and attribute scaling. 

## Technology Stack

* **Backend & Logic**: Python
* **Data Modeling**: Python `dataclasses`
* **Frontend**: Streamlit
* **Governance & Session Control**: Meta-Command Center v1.0

## Current Status

The project is currently in **Phase 5: Data Population**.

The modular application architecture is in place, and the core data models (`Hero`, `HeroSkill`, `TalentTree`, `TalentNode`, `WarPet`, `PetSkill`) have been translated from the formal schema into Python code. The current focus is on populating these models with the verified data from our "Comprehensive Ground Truth" analysis.

## Installation & Usage

*(This section will be updated once the MVP is deployed.)*

```bash
# 1. Clone the repository
git clone [https://github.com/Amethyst-Deceiver2001/call-of-dragons-engine.git](https://github.com/Amethyst-Deceiver2001/call-of-dragons-engine.git)
cd call-of-dragons-engine

# 2. Create and activate a virtual environment
python3 -m venv .venv
source .venv/bin/activate

# 3. Install dependencies
pip install -r requirements.txt

# 4. Run the Streamlit application
streamlit run app.py
