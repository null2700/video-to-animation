import streamlit as st

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

# Main logic to display this page
def main():
    st.set_page_config(page_title="Are You Deaf", layout="wide")
    are_you_deaf()

if __name__ == "__main__":
    main()
