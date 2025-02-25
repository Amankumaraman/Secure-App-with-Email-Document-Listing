import streamlit as st
import requests

st.title("📩 Secure App with Email Document Listing")

if "jwt_token" not in st.session_state:
    st.session_state["jwt_token"] = None

st.subheader("Register")
register_email = st.text_input("Email", key="register_email")
register_password = st.text_input("Password", type="password", key="register_password")

if st.button("Register"):
    if register_email and register_password:
        response = requests.post("http://127.0.0.1:5000/register", json={"email": register_email, "password": register_password})
        if response.status_code == 201:
            st.success(response.json().get("message", "User registered successfully!"))
        else:
            st.error(response.json().get("error", "Registration failed!"))
    else:
        st.warning("⚠️ Please fill in all fields.")

st.subheader("Login")
login_email = st.text_input("Email", key="login_email")
login_password = st.text_input("Password", type="password", key="login_password")

if st.button("Login"):
    if login_email and login_password:
        response = requests.post("http://127.0.0.1:5000/login", json={"email": login_email, "password": login_password})
        if response.status_code == 200:
            st.session_state["jwt_token"] = response.json()["token"]
            st.success("✅ Login successful!")
        else:
            st.error("❌ Invalid credentials.")
    else:
        st.warning("⚠️ Please fill in all fields.")

if st.session_state["jwt_token"]:
    if st.button("Logout"):
        st.session_state["jwt_token"] = None
        st.success("✅ Logged out successfully!")

if st.session_state["jwt_token"]:
    st.subheader("Fetch Emails")
    app_password = st.text_input("App Password", type="password")

    if st.button("Fetch Emails"):
        if not app_password:
            st.error("⚠️ Please enter your email app password.")
        else:
            headers = {"Authorization": f"Bearer {st.session_state['jwt_token']}"}
            response = requests.post("http://127.0.0.1:5000/fetch_emails", json={"email": login_email, "password": app_password}, headers=headers)

            try:
                emails = response.json()
                st.write("DEBUG:", emails)  

                if isinstance(emails, list):  
                    for email in emails:
                        with st.expander(f"{email.get('subject', 'No Subject')} - {email.get('sender', 'Unknown')} ({email.get('date', 'No Date')})"):
                            st.write(f"**From:** {email.get('sender', 'Unknown')}")
                            st.write(f"**Subject:** {email.get('subject', 'No Subject')}")
                            st.write(f"**Received on:** {email.get('date', 'No Date')}")
                            
                            attachments = email.get("attachments", [])
                            if attachments:
                                st.write("📎 Attachments:")
                                for attachment in attachments:
                                    st.write(f"- {attachment}")
                            else:
                                st.write("No attachments found.")
                else:
                    st.error("❌ Unexpected response format.")
            except Exception as e:
                st.error(f"⚠️ Error parsing response: {e}")
else:
    st.warning("⚠️ Please log in to view emails.")
