import streamlit as st
import random
import matplotlib.pyplot as plt

# Title of the app
st.title("Crush Predictor App")

# User inputs their name
name = st.text_input("What's your name?")

# Radio button for gender selection
gender = st.radio("Select your gender:", ("Male", "Female", "Other"))

# Slider to determine the user's age
age = st.slider("How old are you?", 10, 100, 25)

# Simple game that guesses the user's crush
st.subheader("Crush Guessing Game")
if 'guessed_crush' not in st.session_state:
    st.session_state.guessed_crush = None

if st.button("Guess My Crush"):
    crushes = ["Isko Moreno", "Sara Duterte", "Lean", "Desiree", "Manny Pacquiao", "Balmond", "Alucard"]
    st.session_state.guessed_crush = random.choice(crushes)
    st.write(f"Your crush might be... **{st.session_state.guessed_crush}**!")

# Graph or percentage showing the likelihood of crush reciprocation
st.subheader("Crush Reciprocation Probability")

if st.session_state.guessed_crush:
    probability = random.randint(0, 100)
    st.write(f"The probability that {st.session_state.guessed_crush} likes you back is {probability}%")

    # Displaying the probability as a pie chart
    fig, ax = plt.subplots()
    ax.pie([probability, 100-probability], labels=[f"{probability}%", f"{100-probability}%"], colors=["#FF9999", "#DDDDDD"], startangle=90, counterclock=False)
    ax.axis("equal")
    st.pyplot(fig)
else:
    st.write("Click the button above to guess your crush!")
