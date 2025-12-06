from google import genai
import os
from dotenv import load_dotenv

load_dotenv()

# Initialize the client once (Global scope is fine for this scale)
try:
    api_key = os.getenv("GOOGLE_API_KEY")
    if not api_key:
        # If .env failed (cloud), try Streamlit secrets
        api_key = st.secrets["GOOGLE_API_KEY"]
except Exception as e:
    api_key = None
client = genai.Client(api_key=os.getenv(api_key))

def roast_resume(resume_text):
    """
    Sends the resume text to Gemini with strict instructions to roast it.
    """
    
    # This is the "Personality". We prepend it to the user's text.
    system_instruction = """
    You are a cynical, hard-to-please HR Manager who has seen too many bad resumes.
    Your task is to read the following resume and 'roast' it.
    
    Rules:
    1. Quote specific lines from the text and mock them.
    2. Make fun of generic skills (e.g., "Microsoft Word", "Team Player").
    3. Be sarcastic but funny.
    4. Keep the response at least a minimum of 400 words.
    5. Give it a brutal "Score" out of 10 at the end.
    6. Don't quote the text from the resume again just pure roast only
    7. Roast in Malayalam
    
    Here is the resume content:
    """
    
    try:
        # Combine the instructions with the actual resume data
        full_prompt = f"{system_instruction}\n\n{resume_text}"
        
        response = client.models.generate_content(
            model="gemini-2.0-flash",
            contents=full_prompt,
        )
        return response.text
        
    except Exception as e:
        return f"Gemini is taking a coffee break. Error: {e}"