import streamlit as st

# Set page configuration
st.set_page_config(page_title="JnanMudra - ISL App", layout="wide")

# CSS styles
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

header {
    background: var(--primary-color);
    color: var(--light-color);
    padding: 1rem 0;
}

#about .container{
    max-width: 45%;
    float: left;
    margin-left: 80px;
    margin-right: 50px;
}

.container {
    width: 80%;
    margin: 0 auto;
}

nav ul {
    list-style: none;
    display: flex;
    justify-content: flex-end;
}

nav ul li {
    margin-left: 2rem;
}

nav ul li a {
    color: var(--light-color);
    text-decoration: none;
    font-weight: bold;
    padding: 0.5rem 1rem;
}

nav ul li a:hover {
    background: var(--accent-color);
    color: var(--light-color);
    border-radius: 5px;
}

.hero {
    background: var(--secondary-color);
    color: var(--dark-color);
    text-align: center;
    padding: 4rem 1rem;
}

.hero h2 {
    font-size: 2.5rem;
    margin-bottom: 1rem;
}

.hero p {
    font-size: 1.2rem;
    margin-bottom: 1.5rem;
}

.btn {
    background-color: #FF6B6B;
    color: #FFFFFF;
    padding: 0.8rem 2rem;
    border: none;
    border-radius: 5px;
    font-size: 1rem;
    cursor: pointer;
    text-decoration: none;
}

section {
    padding: 3rem 0;
}

#about p, #learn p {
    margin-top: 15px;
    margin-bottom: 20px;
    font-size: 1.1rem;
    line-height: 1.8;
}

#features .features-grid {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
    gap: 2rem;
}

#features h1{
    font-size: 30px;
    text-align: center;
    margin: 10px;
}

.feature {
    background: var(--light-color);
    padding: 1rem;
    margin: 10px;
    text-align: center;
    border-radius: 8px;
    box-shadow: 0 2px 5px rgba(0, 0, 0, 0.1);
}

.feature:hover {
    animation: popUp 1s ease-in;
    transform-origin: center;
}

.feature h3 {
    margin-bottom: 1rem;
    color: var(--primary-color);
}

#learn ul {
    margin-top: 2rem;
    list-style-type: none;
}

#learn ul li {
    margin-bottom: 1rem;
}

#learn ul li a {
    color: var(--primary-color);
    text-decoration: none;
    font-size: 1.1rem;
}

#learn ul li a:hover {
    text-decoration: underline;
}

form {
    background: var(--light-color);
    padding: 2rem;
    border-radius: 5px;
    box-shadow: 0 2px 5px rgba(0, 0, 0, 0.1);
}

form label {
    display: block;
    margin: 1rem 0 0.5rem;
    font-weight: bold;
}

form input, form textarea {
    width: 100%;
    padding: 0.8rem;
    border: 1px solid var(--primary-color);
    border-radius: 5px;
    margin-bottom: 1.5rem;
}

form button {
    background: var(--primary-color);
    color: var(--light-color);
    padding: 0.8rem 2rem;
    border: none;
    border-radius: 5px;
    font-size: 1rem;
    cursor: pointer;
}

form button:hover {
    background: var(--accent-color);
}

footer {
    background: var(--primary-color);
    color: var(--light-color);
    text-align: center;
    padding: 15px;
    margin-bottom: 0px;
}

@keyframes popUp {
    0% {
        transform: scale(1);
    }
    50% {
        transform: scale(1.1);
    }
    100% {
        transform: scale(1);
    }
}

</style>
""", unsafe_allow_html=True)

# Header Section
st.markdown("<header><div class='container'><h1>JnanMudra</h1><nav><ul><li><a href='#home'>Home</a></li><li><a href='#about'>About</a></li><li><a href='#learn'>Learn</a></li><li><a href='#contact'>Contact</a></li></ul></nav></div></header>", unsafe_allow_html=True)

# Home Section
st.markdown("<section id='home'><div class='hero'><h2>Empowering Communication Through Sign Language</h2><p>Your companion to understanding Indian Sign Language.</p><a href='#features' class='btn'>Explore Features</a></div></section>", unsafe_allow_html=True)

# About Us Section
st.markdown("<section id='about'><div class='container'><h2>About Us</h2><p>JnanMudra is dedicated to empowering the Indian deaf community by providing accessible and innovative tools for communication using Indian Sign Language (ISL). Our mission is to bridge the communication gap between the deaf and hearing communities through AI-powered technology, enabling real-time translation from speech to sign language and vice-versa. We aim to make ISL easily learnable and usable for everyone, creating a more inclusive world where no one is left out of conversations due to hearing disabilities.</p></div><div class='about-img'><img src='./Screenshot 2024-09-29 172357.png' alt='signing animation' height='400px' width='600px'></div></section>", unsafe_allow_html=True)

st.markdown("<hr>", unsafe_allow_html=True)

# Features Section
st.markdown("""
<section id='features'>
    <div class='container'>
        <h1>Features</h1>
        <div class='features-grid'>
        <a href="#" onclick="window.location.href = '?page=Real-time ISL Conversion';">
            <div class='feature'>
                <h3>Real-time ISL Conversion</h3>
                <p>Convert spoken words into Indian Sign Language gestures.</p>
            </div>
        </a>
        <a href="#" onclick="window.location.href = '?page=Speech to Gesture';">
            <div class='feature'>
                <h3>Speech to Gesture</h3>
                <p>Use our AI-driven technology to interpret and generate gestures.</p>
            </div>
        </a>
        </div>
    </div>
</section>
""", unsafe_allow_html=True)

#st.markdown("</div></div></section>", unsafe_allow_html=True)

#st.markdown("<hr>", unsafe_allow_html=True)

# Learn Section (Tutorials and Articles)
st.markdown("<section id='learn'><div class='container'><h1>Learn ISL</h1><p>Explore a collection of tutorials and articles to master Indian Sign Language.</p>", unsafe_allow_html=True)

youtube_links = [
    "https://www.youtube.com/embed/videoseries?list=PLFjydPMg4DaoHAtKlvy4I1aL1ksHY0l28",
    "https://www.youtube.com/embed/videoseries?list=PLFjydPMg4DarukFKKVn9bop7fWDg8TGhG",
    "https://www.youtube.com/embed/videoseries?list=PLxYMaKXKMMcMgg4f47WkG7AM0bb3AyjTi",
    "https://www.youtube.com/embed/videoseries?list=PLxYMaKXKMMcNfbb0sOfg5sGJCWCLyKe_K"
]
for link in youtube_links:
    st.markdown(f"<iframe width='560' height='315' src='{link}' frameborder='0' allow='accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share' allowfullscreen></iframe>", unsafe_allow_html=True)

st.markdown("<ul class='tutorial-list'>", unsafe_allow_html=True)
tutorials = [
    ("Beginner's Guide to Indian Sign Language", "https://indiansignlanguage.org/"),
    ("Common ISL Gestures and Their Meanings", "https://www.researchgate.net/figure/Different-Signs-of-Indian-Sign-language_fig1_360403465"),
    ("How to Communicate Effectively Using ISL", "https://www.ndcs.org.uk/information-and-support/professionals/activities/resources/communication/"),
    ("Advanced ISL Grammar and Syntax", "https://www.nios.ac.in/media/documents/230-ISL/Indian-Sign-Language-230.pdf")
]
for title, url in tutorials:
    st.markdown(f"<li><a href='{url}' target='_blank'>{title}</a></li>", unsafe_allow_html=True)
st.markdown("</ul></div></section>", unsafe_allow_html=True)

st.markdown("<hr>", unsafe_allow_html=True)

# Contact Us Section
st.markdown("<section id='contact'><div class='container'><h2>Contact Us</h2>", unsafe_allow_html=True)
with st.form(key='contact_form'):
    name = st.text_input("Your Name:", "")
    email = st.text_input("Your Email:", "")
    phone = st.text_input("Your Phone Number:", "")
    message = st.text_area("Your Message:", "")
    submit_button = st.form_submit_button(label='Submit')

    if submit_button:
        st.success("Thank you for your message! We will get back to you soon.")

st.markdown("</div></section>", unsafe_allow_html=True)

# Footer
st.markdown("<footer><div class='container'><p>&copy; 2024 JnanMudra. All Rights Reserved.</p></div></footer>", unsafe_allow_html=True)

