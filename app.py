import streamlit as st
import pdfplumber
from roaster import roast_resume 
st.set_page_config(page_title="Resume Roast 🔥")
st.title("🔥 AI Resume Roaster")
st.write("Upload your resume. Prepare to cry.")

uploaded_file = st.file_uploader("Upload PDF", type="pdf")

if uploaded_file is not None:
    
    with st.spinner("Reading file..."):
        text = ""
        with pdfplumber.open(uploaded_file) as pdf:
            for page in pdf.pages:
                text += (page.extract_text() or "") + "\n"
                
    st.success("Resume read successfully!")
    
    if st.button("Roast Me! 🔥"):
        
        with st.spinner("Generating insults..."):
            roast_output = roast_resume(text)
            
        st.markdown("### The Verdict:")
        st.write(roast_output)