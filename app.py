import streamlit as st
import os
import datetime

# File to store the response
RESPONSE_FILE = "response.txt"

# Appointment info
appointment_time = "Tonight at 10:00 PM 💫"
rejection_reasons = [
    "I'm busy practicing my Oscar speech in the mirror 🏆",
    "I have a super urgent meeting with my blanket 😴",
    "Sorry, it's national ignore-your-boyfriend day 🙈",
    "Netflix > Suhail tonight, sorry not sorry 🍿",
    "My cat said no. I trust her judgment 🐱"
]

# Load previous response if exists
def load_response():
    if os.path.exists(RESPONSE_FILE):
        with open(RESPONSE_FILE, "r") as f:
            return f.read()
    return None

# Save response permanently
def save_response(response_text):
    with open(RESPONSE_FILE, "w") as f:
        f.write(response_text)

# UI Setup
st.set_page_config(page_title="Suhail’s Video Call Request 💖", page_icon="📞")
st.title("🌸 Video Call Request from Suhail")
st.subheader("✨ He wants to video call you...")
st.write(f"🕒 **Requested Time:** {appointment_time}")
st.markdown("---")

# Check if already responded
previous_response = load_response()

if previous_response:
    st.markdown("### 📝 Your Response Has Been Recorded:")
    st.info(previous_response)
    st.warning("You already responded. Thank you! 😇")
else:
    # Let user choose
    action = st.selectbox(
        "What would you like to do?",
        ["Choose an option", "✅ Accept", "❌ Reject", "🔁 Suggest another time"]
    )

    if action == "✅ Accept":
        if st.button("Submit"):
            response_text = f"✅ Accepted the video call at {appointment_time}."
            save_response(response_text)
            st.success("Response saved! Refresh to see your answer permanently.")

    elif action == "❌ Reject":
        reason = st.selectbox("Pick a reason to reject:", rejection_reasons)
        if st.button("Submit"):
            response_text = f"❌ Rejected the call.\n**Reason:** {reason}"
            save_response(response_text)
            st.success("Response saved! Refresh to see your answer permanently.")

    elif action == "🔁 Suggest another time":
        new_time = st.time_input("Suggest a different time for the call:")
        if st.button("Submit"):
            readable_time = new_time.strftime("%I:%M %p")
            response_text = f"🔁 Suggested a new time: {readable_time} instead of {appointment_time}."
            save_response(response_text)
            st.success("Response saved! Refresh to see your answer permanently.")
