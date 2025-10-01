import streamlit as st

# Title and Header
st.set_page_config(page_title="JnanMudra - ISL App", layout="wide")
st.title("JnanMudra")
st.markdown("""
    ### Empowering Communication Through Sign Language
    Your companion to understanding Indian Sign Language.
""")

# Navigation
nav_options = ["Home", "About", "Learn", "Contact"]
selected_nav = st.sidebar.selectbox("Navigate", nav_options)

# Home Section
if selected_nav == "Home":
    st.header("Welcome to JnanMudra")
    st.button("Explore Features")

# About Section
elif selected_nav == "About":
    st.header("About Us")
    st.write("""
        JnanMudra is dedicated to empowering the Indian deaf community by providing accessible and innovative tools for communication using Indian Sign Language (ISL). 
        Our mission is to bridge the communication gap between the deaf and hearing communities through AI-powered technology, enabling real-time translation from speech to sign language and vice-versa. 
        We aim to make ISL easily learnable and usable for everyone, creating a more inclusive world where no one is left out of conversations due to hearing disabilities.
    """)
    st.image("Screenshot 2024-09-29 172357.png", caption="Signing Animation", width=600)

# Features Section
elif selected_nav == "Learn":
    st.header("Features")
    features = {
        "Real-time ISL Conversion": "Convert spoken words into Indian Sign Language gestures.",
        "Speech to Gesture": "Use our AI-driven technology to interpret and generate gestures.",
        "ISL Learning Tools": "Interactive tutorials to help you learn ISL step-by-step.",
        "User-Friendly Interface": "Simple, intuitive design for easy navigation."
    }
    
    for feature, description in features.items():
        st.subheader(feature)
        st.write(description)

    st.header("Learn ISL")
    st.write("Explore a collection of tutorials and articles to master Indian Sign Language.")

    # YouTube Playlists
    st.video("https://www.youtube.com/embed/videoseries?si=k4BeBIa_4omr5ziu&list=PLFjydPMg4DaoHAtKlvy4I1aL1ksHY0l28")
    st.video("https://www.youtube.com/embed/videoseries?si=E4ddmwwSTUlQBbqc&list=PLFjydPMg4DarukFKKVn9bop7fWDg8TGhG")
    st.video("https://www.youtube.com/embed/videoseries?si=hO8ptBjnbE9h6i_j&list=PLxYMaKXKMMcMgg4f47WkG7AM0bb3AyjTi")
    st.video("https://www.youtube.com/embed/videoseries?si=GA1FQ9DpdZv0-V2t&list=PLxYMaKXKMMcNfbb0sOfg5sGJCWCLyKe_K")

    # Tutorial Links
    tutorials = [
        ("Beginner's Guide to Indian Sign Language", "https://indiansignlanguage.org/"),
        ("Common ISL Gestures and Their Meanings", "https://www.researchgate.net/figure/Different-Signs-of-Indian-Sign-language_fig1_360403465"),
        ("How to Communicate Effectively Using ISL", "https://www.ndcs.org.uk/information-and-support/professionals/activities/resources/communication/"),
        ("Advanced ISL Grammar and Syntax", "https://www.nios.ac.in/media/documents/230-ISL/Indian-Sign-Language-230.pdf"),
    ]

    st.write("### Tutorials and Articles:")
    for title, link in tutorials:
        st.markdown(f"- [{title}]({link})")

# Contact Section
elif selected_nav == "Contact":
    st.header("Contact Us")
    contact_form = st.form(key='contact_form')
    name = contact_form.text_input("Your Name:")
    email = contact_form.text_input("Your Email:")
    phone = contact_form.text_input("Your Phone Number:")
    message = contact_form.text_area("Your Message:", height=150)
    submit_button = contact_form.form_submit_button(label='Submit')

    if submit_button:
        st.success("Message submitted successfully!")

# Footer
st.markdown("---")
st.write("© 2024 JnanMudra. All Rights Reserved.")
