import streamlit as st

# --- Core Imports from our new modular structure ---
# Import the calculator function to handle our business logic.
from src.calculators.skill_calculator import calculate_tokens_needed

# Import the data models and the populated hero data.
from src.models.hero import Hero
from src.data.heroes_data import ALL_HEROES


# --- Main Application UI ---

st.set_page_config(page_title="Call of Dragons: Engine", layout="wide")

st.title("🐉 Call of Dragons: Strategic Engine")
st.markdown("This engine provides analytical tools based on verified game mechanics to help optimize progression.")

# Create a dictionary for easy hero lookup by name. This is more efficient.
heroes_dict = {hero.hero_name: hero for hero in ALL_HEROES}
hero_names = list(heroes_dict.keys())

st.sidebar.header("Hero Selection")
selected_hero_name = st.sidebar.selectbox(
    "Select a Hero to analyze:",
    options=hero_names,
    index=0 # Default to the first hero in the list
)

# --- Main Calculator Panel ---
# This section will only render if a hero has been selected.
if selected_hero_name:
    selected_hero = heroes_dict[selected_hero_name]

    st.header(f"Analysis for: {selected_hero.hero_name}")
    st.subheader("Skill 1 '5-1-1-1' Progression Calculator")
    st.markdown(
        "This tool helps you follow the optimal 'skill locking' strategy for a hero's first skill. "
        "It calculates the tokens needed to max Skill 1 and warns you if you are on a sub-optimal path."
    )

    col1, col2 = st.columns(2)

    with col1:
        st.info(
            f"""
            - **Rarity**: {selected_hero.rarity}
            - **Unit Type**: {selected_hero.unit_type}
            - **Roles**: {', '.join(selected_hero.roles)}
            """
        )

        # --- User Input Widgets ---
        current_star_level = st.number_input(
            "Current Star Level (1-6):",
            min_value=1,
            max_value=6,  # Corrected to reflect S2 mechanics
            value=1,
            step=1,
            help="Enter the hero's current star level, up to a maximum of 6 for Season 2+."
        )

        current_skill_1_level = st.number_input(
            "Current Level of Skill 1 (1-5):",
            min_value=1,
            max_value=5,  # Corrected to allow input up to level 5
            value=1,
            step=1,
            help="Enter the current level of the first skill. A skill is maxed at level 5."
        )

        available_hero_tokens = st.number_input(
            "Number of Hero Tokens Available:",
            min_value=0,
            value=0,
            step=10,
            help="Enter the number of hero-specific tokens you currently have."
        )

    with col2:
        # --- Calculation and Recommendation Logic ---
        if st.button("Calculate Optimal Progression"):
            if current_skill_1_level == 5:
                st.success(
                    "**Skill 1 is already maxed (Level 5)!**\n\n"
                    "You can now safely increase your hero's star level to unlock "
                    "and progress other skills. Congratulations!"
                )
            elif current_star_level > 1:
                st.warning(
                    "**Warning: You are not on the optimal '5-1-1-1' path!**\n\n"
                    "Your first skill is not yet maxed, but your hero's star level "
                    "is greater than 1. This means other skills are unlocked, and your "
                    "Hero Tokens will be randomly distributed among them, "
                    "which is highly inefficient. It is recommended to max Skill 1 "
                    "*before* increasing star levels beyond 1."
                )
            else:  # This is the optimal path: star_level is 1 and skill_1 is not maxed.
                st.success(
                    "**Optimal Path Confirmed!**\n\n"
                    "Your hero is at 1-star while Skill 1 is not yet maxed. "
                    "This is the correct 'skill locking' strategy. All tokens "
                    "you invest will go directly into Skill 1."
                )

                # Use the dedicated calculator function from our new module
                tokens_to_max = calculate_tokens_needed(current_skill_1_level, selected_hero.rarity)

                st.info(f"You need **{tokens_to_max}** more tokens to max out Skill 1.")

                if available_hero_tokens >= tokens_to_max:
                    st.balloons()
                    st.success(f"Great news! You have enough tokens to max Skill 1 right now.")
                else:
                    tokens_still_needed = tokens_to_max - available_hero_tokens
                    st.warning(f"You are on the right track, but you still need **{tokens_still_needed}** more tokens.")

