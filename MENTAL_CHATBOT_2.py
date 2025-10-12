import streamlit as st
import google.generativeai as genai

# CONFIGURATION
st.set_page_config(page_title="AI Mental Health Companion", page_icon="🧘‍♀️")
#genai.configure(api_key="AIzaSyDqr468UxePktdsorrRZHjrY7G6GFebybI")  
GOOGLE_API_KEY ="AIzaSyDqr468UxePktdsorrRZHjrY7G6GFebybI"
genai.configure(api_key=st.secrets["GOOGLE_API_KEY"])

# Initialize model
model = genai.GenerativeModel("gemini-2.5-flash")

# FUNCTION: Analyze and Respond
def get_emotional_response(user_input):
    prompt = f"""
    You are a kind, empathetic AI mental health companion for students.
    Analyze the user’s message for emotional tone and stress level.
    Respond with short, comforting, and caring advice (max 80 words).
    If the user sounds extremely distressed, gently suggest professional help or campus counselor contact.

    User message: "{user_input}"
    """
    response = model.generate_content(prompt)
    return response.text.strip()

# STREAMLIT FRONTEND
st.title("🧠 AI-Driven Mental Health Companion Chatbot")
st.write("Your private, 24/7 AI chat friend for emotional support ❤️")

# Chat history
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

# User input
user_message = st.text_area("How are you feeling today?", placeholder="Type your thoughts here...")

if st.button("Send"):
    if user_message.strip():
        bot_reply = get_emotional_response(user_message)

        st.session_state.chat_history.append(("You", user_message))
        st.session_state.chat_history.append(("Companion", bot_reply))
        st.rerun()

# Display chat history
for sender, msg in st.session_state.chat_history:
    if sender == "You":
        st.markdown(f"**👤 You:** {msg}")
    else:
        st.markdown(f"**🤖 Companion:** {msg}")

st.markdown("---")
st.info("If you're ever in crisis, please reach out to your college counselor or call a trusted helpline immediately 💛")

