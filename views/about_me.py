import streamlit as st

from forms.contact import contact_form


@st.dialog("Contact Me")
def show_contact_form():
    contact_form()


# --- HERO SECTION ---
col1, col2 = st.columns(2, gap="small", vertical_alignment="center")
with col1:
    st.image("./assets/me.png", width=230)

with col2:
    st.title("Trixie Gail Cloma", anchor=False)
    st.write(
        "BSIT 4"
    )
    if st.button("✉️ Contact Me"):
        show_contact_form()


st.write("\n")
st.subheader("ABOUT ME", anchor=False)
st.write(
    """
    I am Trixie Gail Cloma, a BSIT 4 student and currently studying at Cebu Institute of Technology- University.
    I am a person who is positive about every aspect of life. There are many things I like to do, to see, and to experience.
    From a young age, I've always had a curiosity for the world around me. Growing up, I was drawn to technology, which eventually led me to pursue IT. My passion for photography has been a driving force in my life, pushing me to constantly learn and evolve.
    After I complete my studies in IT, I'll embarked on a journey in teaching, where I'll be able to teach younger generation about technology. 
    Outside of my student life, I enjoy doing photography and watching anime, which keep me balanced and grounded. Whether I'm doing photography, I find joy in the simple things that life has to offer.

    Throughout my life, I've been guided by values, and these have shaped the person I am today. I look forward to the future with optimism, ready to embrace new challenges and continue growing both personally and professionally.
    """
)


# Custom CSS for background color
st.markdown(
    """
    <style>
    .custom-container {
        background-color: #f0f2f6;
        padding: 2px;
        border-radius: 10px;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Creating a container with a background color
with st.container():
    st.markdown('<div class="custom-container">', unsafe_allow_html=True)
    st.header("General About Me")
    st.write("""
    - **Name**: Trixie Gail Cloma
    - **Age**: 21
    - **Location**: Talisay City, Philippines
    - **Interests outside of field of study**: photography, singing, dancing, watching anime and many more!
    - **Favorite Quote**: "The only way to do great work is to love what you do." - Steve Jobs
    - **Favorite Color**: Yellow
    """)
    st.markdown('</div>', unsafe_allow_html=True)


