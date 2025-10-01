import streamlit as st

# Set page title
st.set_page_config(page_title="JnanMudra - ISL App")

# Navbar
def navbar():
    st.markdown("""
    <style>
        .navbar {
            background-color: #2b6777;
            color: white;
            padding: 1rem;
        }
        .navbar a {
            color: white;
            padding: 0.5rem 1rem;
            text-decoration: none;
            font-weight: bold;
        }
        .navbar a:hover {
            background-color: #ff6b6b;
            border-radius: 5px;
        }
    </style>
    <div class="navbar">
        <h1 style="display:inline;">JnanMudra</h1>
        <nav style="float:right;">
            <a href="#home">Home</a>
            <a href="#about">About</a>
            <a href="#learn">Learn</a>
            <a href="#contact">Contact</a>
        </nav>
    </div>
    """, unsafe_allow_html=True)

navbar()

# Home Section
st.markdown("""
### Empowering Communication Through Sign Language
Your companion to understanding Indian Sign Language.
""")
st.button("Explore Features", key="explore_features")

# About Us Section
st.markdown("## About Us")
st.markdown("""
JnanMudra is dedicated to empowering the Indian deaf community by providing accessible and innovative tools for communication using Indian Sign Language (ISL). 
Our mission is to bridge the communication gap between the deaf and hearing communities through AI-powered technology, enabling real-time translation from speech to sign language and vice-versa. 
We aim to make ISL easily learnable and usable for everyone, creating a more inclusive world where no one is left out of conversations due to hearing disabilities.
""")
st.image("Screenshot 2024-09-29 172357.png", caption="Signing Animation", use_column_width=True)

# Features Section
st.markdown("## Features")
features = {
    "Real-time ISL Conversion": "Convert spoken words into Indian Sign Language gestures.",
    "Speech to Gesture": "Use our AI-driven technology to interpret and generate gestures.",
    "ISL Learning Tools": "Interactive tutorials to help you learn ISL step-by-step.",
    "User-Friendly Interface": "Simple, intuitive design for easy navigation."
}

for feature, description in features.items():
    st.markdown(f"**{feature}**: {description}")

# Learn Section (Tutorials and Articles)
st.markdown("## Learn ISL")
st.markdown("Explore collection of tutorials and articles to master Indian Sign Language.")

# YouTube Playlist
st.markdown("### YouTube Tutorials")
youtube_links = [
    "https://www.youtube.com/embed/videoseries?list=PLFjydPMg4DaoHAtKlvy4I1aL1ksHY0l28",
    "https://www.youtube.com/embed/videoseries?list=PLFjydPMg4DarukFKKVn9bop7fWDg8TGhG",
    "https://www.youtube.com/embed/videoseries?list=PLxYMaKXKMMcMgg4f47WkG7AM0bb3AyjTi",
    "https://www.youtube.com/embed/videoseries?list=PLxYMaKXKMMcNfbb0sOfg5sGJCWCLyKe_K"
]

for link in youtube_links:
    st.markdown(f'<iframe width="560" height="315" src="{link}" frameborder="0" allowfullscreen></iframe>', unsafe_allow_html=True)

# Tutorials Links
st.markdown("### Useful Links")
tutorial_links = [
    ("Beginner's Guide to Indian Sign Language", "https://indiansignlanguage.org/"),
    ("Common ISL Gestures and Their Meanings", "https://www.researchgate.net/figure/Different-Signs-of-Indian-Sign-language_fig1_360403465"),
    ("How to Communicate Effectively Using ISL", "https://www.ndcs.org.uk/information-and-support/professionals/activities/resources/communication/"),
    ("Advanced ISL Grammar and Syntax", "https://www.nios.ac.in/media/documents/230-ISL/Indian-Sign-Language-230.pdf")
]

for title, url in tutorial_links:
    st.markdown(f"- [{title}]({url})")

# Contact Us Section
st.markdown("## Contact Us")
with st.form(key='contact_form'):
    name = st.text_input("Your Name:")
    email = st.text_input("Your Email:")
    phone = st.text_input("Your Phone Number:")
    message = st.text_area("Your Message:")
    submit_button = st.form_submit_button(label='Submit')

if submit_button:
    st.success("Your message has been submitted!")

# Footer
st.markdown("<footer style='text-align:center; padding:15px; background-color:#2b6777; color:white;'> &copy; 2024 JnanMudra. All Rights Reserved.</footer>", unsafe_allow_html=True)
