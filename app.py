import streamlit as st
import os
import datetime

# === Constants ===
RESPONSE_FILE = "response.txt"
appointment_time = "Tonight at 10:00 PM 💫"
rejection_reasons = [
    "I'm busy practicing my Oscar speech in the mirror 🏆",
    "I have a super urgent meeting with my blanket 😴",
    "Sorry, it's national ignore-your-boyfriend day 🙈",
    "Netflix > Suhail tonight, sorry not sorry 🍿",
    "My cat said no. I trust her judgment 🐱",
    "I Hate YOU!!",
    "You don't deserve to see my face."
]

# === Functions ===
def load_response():
    if os.path.exists(RESPONSE_FILE):
        with open(RESPONSE_FILE, "r") as f:
            return f.read()
    return None

def save_response(text):
    with open(RESPONSE_FILE, "w") as f:
        f.write(text)

def clear_response():
    if os.path.exists(RESPONSE_FILE):
        os.remove(RESPONSE_FILE)

# === UI Setup ===
st.set_page_config(page_title="Suhail’s Video Call Request 💖", page_icon="📞")
st.title("🌸 Video Call Request from Suhail")
st.subheader("✨ He wants to video call you...")
st.write(f"🕒 **Requested Time:** {appointment_time}")
st.markdown("---")

# === CSS for better dropdown formatting ===
st.markdown("""
    <style>
    .rejection-container .stSelectbox > div {
        width: 100% !important;
    }
    .rejection-container .stSelectbox label {
        font-weight: 500;
    }
    .rejection-container .stSelectbox .css-1cpxqw2 {
        min-height: 45px !important;
        font-size: 16px !important;
    }
    </style>
""", unsafe_allow_html=True)

# === Logic ===
previous_response = load_response()

if previous_response:
    st.markdown("### 📝 Your Response Has Been Recorded:")
    st.info(previous_response)
    if st.button("😅 Sorry, I changed my mind"):
        clear_response()
        st.success("Response cleared! You can now choose again.")
        st.stop()
    else:
        st.warning("You already responded. Thank you! 😇")
        st.stop()

# === First row: Accept button ===
st.markdown("### ✅ Accept the Call")
if st.button("✅ Accept"):
    response = f"✅ Accepted the video call at {appointment_time}."
    save_response(response)
    st.success("Response saved! Refresh to see your answer permanently.")
    st.stop()

# === Second row: Reject & Suggest Time ===
col1, col2 = st.columns(2)

with col1:
    st.markdown("### ❌ Reject:")
    with st.container():
        st.markdown('<div class="rejection-container">', unsafe_allow_html=True)
        reason = st.selectbox("Pick a reason:", rejection_reasons)
        st.markdown('</div>', unsafe_allow_html=True)
    if st.button("Submit Rejection"):
        response = f"❌ Rejected the call.\n**Reason:** {reason}"
        save_response(response)
        st.success("Rejection saved! Refresh to see it permanently.")
        st.stop()

with col2:
    st.markdown("### 🔁 Suggest Time:")
    new_time = st.time_input("Suggest a new time:")
    if st.button("Submit Suggestion"):
        readable = new_time.strftime("%I:%M %p")
        response = f"🔁 Suggested a new time: {readable} instead of {appointment_time}."
        save_response(response)
        st.success("Suggestion saved! Refresh to see it permanently.")
        st.stop()
