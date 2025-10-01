import streamlit as st
import json
import random

# Page 1: Hindi Voice Chatbot
def hindi_voice_chatbot():
    st.markdown("<h1 style='text-align: center; color: white;'>हिंदी वॉयस चैटबॉट</h1>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: center; color: white;'>माइक दबाएं और बात करें</p>", unsafe_allow_html=True)
    
    if st.button("माइक से बोलें"):
        # Simulate a speech recognition response for the demo
        commands = ["कैसा मौसम है?", "समय क्या हुआ है?", "तुम्हारा नाम क्या है?", "मुझे खबर सुनाओ"]
        selected_command = random.choice(commands)
        
        st.write(f"आदेश: {selected_command}")
        st.write("सुन रहा हूँ...")

        # Simulating chatbot response
        response = {
            "कैसा मौसम है?": "मौसम अच्छा है।",
            "समय क्या हुआ है?": "अभी 5 बजे हैं।",
            "तुम्हारा नाम क्या है?": "मेरा नाम स्ट्रीमलिट है।",
            "मुझे खबर सुनाओ": "आज की खबर यह है कि तकनीक तेजी से बढ़ रही है!"
        }
        st.write(f"प्रतिक्रिया: {response[selected_command]}")
    
    # Link to the next page
    st.markdown("<a href='/page2' style='font-size:18px; color:#00ffcc;'>अगले पेज पर जाएं</a>", unsafe_allow_html=True)

# Page 2: Are You Deaf?
def are_you_deaf():
    st.markdown("<h1 style='text-align: center; color: white;'>क्या आप बहरे हैं?</h1>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: center; color: white;'>इस प्रश्न का उत्तर देने के लिए कृपया एक बटन दबाएँ:</p>", unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    
    with col1:
        if st.button("हाँ"):
            st.write("आपने 'हाँ' का उत्तर दिया।")
    
    with col2:
        if st.button("नहीं"):
            st.write("आपने 'नहीं' का उत्तर दिया।")
    
    st.markdown("<br><a href='/' style='font-size:18px; color:#00ffcc;'>वापस जाएं</a>", unsafe_allow_html=True)

# Main logic to switch between pages
def main():
    st.set_page_config(page_title="JnanMudra - ISL App", layout="wide")
    
    pages = {
        "Hindi Voice Chatbot": hindi_voice_chatbot,
        "Are You Deaf?": are_you_deaf
    }
    
    page = st.sidebar.selectbox("Select a page:", list(pages.keys()))
    
    # Render the selected page
    pages[page]()

if __name__ == "__main__":
    main()
