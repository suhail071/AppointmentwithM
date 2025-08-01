import streamlit as st
import os
from datetime import datetime

# === Constants ===
RESPONSE_FILE = "response.txt"
LOG_FILE = "response_log.txt"
appointment_time = "Tonight at 10:00 PM 💫"
rejection_reasons = [
        "I'm Still Pissed at you!",
    "I have a super urgent meeting with my blanket",
    "Sorry, You are last on the Priority List.",
    "Everything else > Suhail, sorry not sorry",
    "Fatu's cat said no. I trust his judgment ",
    "You don't deserve my attention",
    "I Hate YOU!~ You don't deserve to see my face."
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

def log_response(text):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open(LOG_FILE, "a") as f:
        f.write(f"[{timestamp}] {text}\n")

def clear_response():
    if os.path.exists(RESPONSE_FILE):
        os.remove(RESPONSE_FILE)

# === UI Setup ===
st.set_page_config(page_title="Suhail’s Video Call Request 💖", page_icon="📞")
st.title("🌸 Video Call Request from Suhail")
st.subheader("✨ Hi Mariyam, Suhail wants to video call you...")
st.write(f"🕒 **Requested Time:** {appointment_time}")
st.markdown("---")

# === CSS for formatting dropdown ===
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

# === Existing response logic ===
previous_response = load_response()

if previous_response:
    st.markdown("### 📝 Your Response Has Been Recorded:")
    st.info(previous_response)

    col_refresh, col_clear = st.columns([1, 2])

    with col_refresh:
        if st.button("🔄 Refresh"):
            st.rerun()

    with col_clear:
        if st.button("😅 Sorry, I changed my mind"):
            clear_response()
            st.success("Response cleared! You can now choose again.")
            st.rerun()

    st.stop()

# === First Row: Accept ===
st.markdown("### ✅ Accept the Call")
if st.button("✅ Accept"):
    response = f"✅ Accepted the video call at {appointment_time}."
    save_response(response)
    log_response(response)
    st.success("Response saved! Refresh to see your answer permanently.")
    st.rerun()

# === Divider ===
st.markdown("---")

# === Second Row: Reject & Suggest ===
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
        log_response(response)
        st.success("Rejection saved! Refresh to see it permanently.")
        st.rerun()

with col2:
    st.markdown("### 🔁 Suggest Time:")
    new_time = st.time_input("Suggest a new time:")
    if st.button("Submit Suggestion"):
        readable = new_time.strftime("%I:%M %p")
        response = f"🔁 Suggested a new time: {readable} instead of {appointment_time}."
        save_response(response)
        log_response(response)
        st.success("Suggestion saved! Refresh to see it permanently.")
        st.rerun()

# === Hidden Admin Section ===
st.markdown("---")
with st.expander("🔒 Admin Log Access (Private)"):
    password = st.text_input("Enter admin password:", type="password")

    if password == "suhail071":
        if os.path.exists(LOG_FILE):
            with open(LOG_FILE, "rb") as f:
                st.download_button(
                    label="⬇️ Download response_log.txt",
                    data=f,
                    file_name="response_log.txt",
                    mime="text/plain"
                )
        else:
            st.warning("No log file found yet.")
    elif password:
        st.error("Incorrect password.")
