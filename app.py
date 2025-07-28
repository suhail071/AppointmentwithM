import streamlit as st
import random
import smtplib
from email.message import EmailMessage

# ==== CONFIGURATION ====
YOUR_EMAIL = "your_email@example.com"
YOUR_EMAIL_PASSWORD = "your_app_password"  # Use App Password if Gmail
SMTP_SERVER = "smtp.gmail.com"
SMTP_PORT = 587

# ==== APPOINTMENT DETAILS ====
appointment_time = "Tonight at 10:00 PM 💫"
rejection_reasons = [
    "I'm busy practicing my Oscar speech in the mirror 🏆",
    "I have a super urgent meeting with my blanket 😴",
    "Sorry, it's national ignore-your-boyfriend day 🙈",
    "Netflix > Suhail tonight, sorry not sorry 🍿",
    "My cat said no. I trust her judgment 🐱"
]

# ==== UI ====
st.set_page_config(page_title="Suhail’s Video Call Request 💖", page_icon="📞")
st.title("🌸 Video Call Request from Suhail 💻💞")
st.subheader("✨ He wants to video call you...")
st.write(f"🕒 **Requested Time:** {appointment_time}")

st.markdown("---")

col1, col2 = st.columns(2)

with col1:
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

            st.success("Yay! Suhail has been notified. 💌")
        except Exception as e:
            st.error(f"Oops! Couldn't send email: {e}")

with col2:
    if st.button("❌ Reject Appointment"):
        reason = random.choice(rejection_reasons)
        st.error("She said no! 😭")
        st.info(f"💬 Reason: *{reason}*")
