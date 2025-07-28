import streamlit as st
import smtplib
from email.message import EmailMessage

# === CONFIG ===
YOUR_EMAIL = st.secrets["YOUR_EMAIL"]
YOUR_EMAIL_PASSWORD = st.secrets["YOUR_EMAIL_PASSWORD"]
SMTP_SERVER = "smtp.gmail.com"
SMTP_PORT = 587

# === Appointment Info ===
appointment_time = "Tonight at 10:00 PM 💫"
rejection_reasons = [
    "I'm busy practicing my Oscar speech in the mirror 🏆",
    "I have a super urgent meeting with my blanket 😴",
    "Sorry, it's national ignore-your-boyfriend day 🙈",
    "Netflix > Suhail tonight, sorry not sorry 🍿",
    "My cat said no. I trust her judgment 🐱"
]

# === UI ===
st.set_page_config(page_title="Suhail’s Video Call Request 💖", page_icon="📞")
st.title("🌸 Video Call Request from Suhail")
st.subheader("✨ He wants to video call you...")
st.write(f"🕒 **Requested Time:** {appointment_time}")

st.markdown("---")
st.write("What do you want to do?")

# Accept
if st.button("✅ Accept Appointment"):
    try:
        msg = EmailMessage()
        msg["Subject"] = "💖 Your Appointment Was Accepted!"
        msg["From"] = YOUR_EMAIL
        msg["To"] = YOUR_EMAIL
        msg.set_content(f"Your girlfriend accepted the video call for {appointment_time} 🥰")

        with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
            server.starttls()
            server.login(YOUR_EMAIL, YOUR_EMAIL_PASSWORD)
            server.send_message(msg)

        st.success("Yay! Suhail has been notified via email 💌")
    except Exception as e:
        st.error(f"Failed to send email: {e}")

# Rejection with reason dropdown
st.markdown("### Or reject the call politely 👀")
selected_reason = st.selectbox("Choose a reason for rejecting:", rejection_reasons)

if st.button("❌ Reject Appointment"):
    st.error("She said no! 😭")
    st.info(f"💬 Reason: *{selected_reason}*")
