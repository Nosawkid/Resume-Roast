import pdfplumber

def extract_text_from_resume(uploaded_file):
    """
    Args:
        uploaded_file: The file object returned by st.file_uploader()
    """
    try:
        # Check the type of the file object
        if uploaded_file.type == "application/pdf":
            with pdfplumber.open(uploaded_file) as pdf:
                text = ""
                for page in pdf.pages:
                    # Extracts text, adds a newline for separation, defaults to empty string if None
                    text += (page.extract_text() or "") + "\n"
                return text
        
        # Simple text files (unlikely for resumes, but good to have)
        elif uploaded_file.type == "text/plain":
            # We must decode the bytes into a string
            return uploaded_file.getvalue().decode("utf-8")
            
        else:
            return "Error: Unsupported file format. Please upload a PDF."

    except Exception as e:
        return f"Error processing file: {e}"