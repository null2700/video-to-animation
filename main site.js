import streamlit as st

# Custom CSS
st.markdown("""
    <style>
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
            font-family: 'Arial', sans-serif;
        }

        body {
            line-height: 1.6;
            background-color: #f4f4f9;
        }

        /* Color Palette */
        :root {
            --primary-color: #2b6777;
            --secondary-color: #c8d8e4;
            --accent-color: #ff6b6b;
            --light-color: #ffffff;
            --dark-color: #1f3a52;
        }

        .header {
            background: var(--primary-color);
            color: var(--light-color);
            padding: 1rem 0;
            text-align: center;
        }

        .hero {
            background: var(--secondary-color);
            color: var(--dark-color);
            text-align: center;
            padding: 4rem 1rem;
        }

        .btn {
            background-color: var(--accent-color);
            color: var(--light-color);
            padding: 0.8rem 2rem;
            border: none;
            border-radius: 5px;
            font-size: 1rem;
            cursor: pointer;
            text-decoration: none;
        }

        .container {
            width: 80%;
            margin: 0 auto;
        }

        .feature {
            background: var(--light-color);
            padding: 1rem;
            margin: 10px;
            text-align: center;
            border-radius: 8px;
            box-shadow: 0 2px 5px rgba(0, 0, 0, 0.1);
        }

        footer {
            background: var(--primary-color);
            color: var(--light-color);
            text-align: center;
            padding: 15px;
        }
    </style>
""", unsafe_allow_html=True)

# Header
st.markdown('<h1 class="header">JnanMudra</h1>', unsafe_allow_html=True)

# Navbar
st.sidebar.title("Navigation")
nav_options = ["Home", "About", "Learn", "Contact"]
selection = st.sidebar.radio("Go to", nav_options)

# Home Section
if selection == "Home":
    st.markdown("""
        <div class="hero">
            <h2>Empowering Communication Through Sign Language</h2>
            <p>Your companion to understanding Indian Sign Language.</p>
            <a href="#features" class="btn">Explore Features</a>
        </div>
    """, unsafe_allow_html=True)

# About Us Section
elif selection == "About":
    st.title("About Us")
    st.write("""
        JnanMudra is dedicated to empowering the Indian deaf community by providing accessible and innovative tools for communication using Indian Sign Language (ISL).
        Our mission is to bridge the communication gap between the deaf and hearing communities through AI-powered technology, enabling real-time translation from speech to sign language and vice-versa.
        We aim to make ISL easily learnable and usable for everyone, creating a more inclusive world where no one is left out of conversations due to hearing disabilities.
    """)
    st.image("./Screenshot 2024-09-29 172357.png", caption="Signing Animation", use_column_width=True)

# Features Section
elif selection == "Learn":
    st.title("Learn ISL")
    st.write("Explore a collection of tutorials and articles to master Indian Sign Language.")
    tutorial_links = [
        ("Beginner's Guide to Indian Sign Language", "https://indiansignlanguage.org/"),
        ("Common ISL Gestures and Their Meanings", "https://www.researchgate.net/figure/Different-Signs-of-Indian-Sign-language_fig1_360403465"),
        ("How to Communicate Effectively Using ISL", "https://www.ndcs.org.uk/information-and-support/professionals/activities/resources/communication/"),
        ("Advanced ISL Grammar and Syntax", "https://www.nios.ac.in/media/documents/230-ISL/Indian-Sign-Language-230.pdf"),
    ]
    
    for title, link in tutorial_links:
        st.markdown(f"- [{title}]({link})")
    
    # YouTube Playlists
    st.subheader("YouTube Playlists")
    youtube_playlists = [
        "https://www.youtube.com/embed/videoseries?si=k4BeBIa_4omr5ziu&list=PLFjydPMg4DaoHAtKlvy4I1aL1ksHY0l28",
        "https://www.youtube.com/embed/videoseries?si=E4ddmwwSTUlQBbqc&list=PLFjydPMg4DarukFKKVn9bop7fWDg8TGhG",
        "https://www.youtube.com/embed/videoseries?si=hO8ptBjnbE9h6i_j&list=PLxYMaKXKMMcMgg4f47WkG7AM0bb3AyjTi",
        "https://www.youtube.com/embed/videoseries?si=GA1FQ9DpdZv0-V2t&list=PLxYMaKXKMMcNfbb0sOfg5sGJCWCLyKe_K"
    ]
    
    for playlist in youtube_playlists:
        st.markdown(f'<iframe width="560" height="315" src="{playlist}" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>', unsafe_allow_html=True)

# Contact Us Section
elif selection == "Contact":
    st.title("Contact Us")
    with st.form("contact_form"):
        name = st.text_input("Your Name:")
        email = st.text_input("Your Email:")
        phone = st.text_input("Your Phone Number:")
        message = st.text_area("Your Message:")
        
        submitted = st.form_submit_button("Submit")
        if submitted:
            st.success("Your message has been sent!")

# Footer
st.markdown('<footer><p>&copy; 2024 JnanMudra. All Rights Reserved.</p></footer>', unsafe_allow_html=True)
