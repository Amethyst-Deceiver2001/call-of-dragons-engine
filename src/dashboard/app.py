import streamlit as st

st.title("Call of Dragons Strategic Analysis Dashboard (Blue Team)")

st.write(
    "Welcome to the Call of Dragons Strategic Analysis Dashboard. "
    "This is the Blue Team's initial MVP, designed to provide "
    "data-driven insights for optimal gameplay."
)

st.header("Current Status")
st.info("Dashboard under active development. Stay tuned for more features!")

if st.button("Click me!"):
    st.success("Button clicked! The app is interactive.")

# --- New Section: Skill XP Calculator ---
st.header("Skill XP Calculator")
st.write("Optimize your hero's skill progression using the '5-1-1-1' strategy.")

# Input fields for hero information
hero_rarity = st.selectbox(
    "Select Hero Rarity:",
    options=["Legendary", "Epic", "Elite"]
)

current_star_level = st.number_input(
    "Current Star Level (1-5):",
    min_value=1,
    max_value=5,
    value=1,
    step=1
)

current_skill_1_level = st.number_input(
    "Current Level of Skill 1 (1-4):",
    min_value=1,
    max_value=4, # Max 4, as 5 is maxed and handled by logic
    value=1,
    step=1
)

available_hero_tokens = st.number_input(
    "Number of Hero Tokens Available:",
    min_value=0,
    value=0,
    step=10
)

# Button to trigger calculation
if st.button("Calculate Optimal Progression"):
    # Basic calculation logic for '5-1-1-1' strategy
    if current_skill_1_level < 5:
        if current_star_level > 1:
            st.warning(
                "**Warning: You are not on the optimal '5-1-1-1' path!**\n\n"
                "Your first skill is not yet maxed (Level 5), but your hero's star level "
                "is greater than 1. This means other skills are unlocked, and your "
                "Hero Tokens will be randomly distributed among all unlocked skills, "
                "diluting your investment in the crucial first skill. "
                "It is highly recommended to max Skill 1 to Level 5 *before* increasing "
                "star levels beyond 1 to ensure 100% token efficiency for Skill 1. [1, 2]"
            )
        else: # current_star_level == 1
            st.success(
                "**Optimal Path Confirmed!**\n\n"
                "Your hero is at 1-star and Skill 1 is not yet maxed. "
                "This is the optimal 'skill locking' strategy. All Hero Tokens "
                "you invest will go directly into Skill 1 until it reaches Level 5. "
                "Keep investing tokens until Skill 1 is maxed before increasing star levels. [1, 2]"
            )
    else: # current_skill_1_level == 5
        st.info(
            "Skill 1 is already maxed (Level 5). You can now safely increase your "
            "hero's star level to unlock and progress other skills. [1, 2]"
        )

# --- End of New Section ---