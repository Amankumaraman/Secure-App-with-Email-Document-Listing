
# 📩 Secure Email Viewer

A **secure** and **feature-rich** Streamlit application that allows users to **register, log in, and fetch emails** from their inbox, including listing email documents and attachments.

---

## 🚀 Features

✅ **User Authentication** (Registration & Login)  
✅ **Secure Token-based Access** using JWT  
✅ **Fetch & Display Emails** (Sender, Subject, Date)  
✅ **Download Attachments** (if available)  
✅ **Logout functionality**  
✅ **Error Handling & Validation**  

---

## 🛠️ Tech Stack

- **Frontend**: Streamlit (Python-based UI Framework)  
- **Backend**: Flask (REST API for authentication & email retrieval)  
- **Database**: MongoDB (for user credentials & tokens)  
- **Email API**: IMAP (or Gmail API / Outlook API)  

---

## 🔧 Installation & Setup

### 1️⃣ Clone the Repository
```sh
git clone https://github.com/Amankumaraman/Secure-App-with-Email-Document-Listing.git
cd Secure-App-with-Email-Document-Listing
```

### 2️⃣ Install Dependencies
```sh
pip install -r requirements.txt
```

### 3️⃣ Run the Backend
Start your Flask server:
```sh
python backend/app.py
```
(Default runs at `http://127.0.0.1:5000`)

### 4️⃣ Run the Streamlit Frontend
```sh
streamlit run frontend/app.py
```
(Default runs at `http://localhost:8501`)

---

## 📌 API Endpoints

### **Authentication**
| Method | Endpoint  | Description |
|--------|----------|-------------|
| POST   | `/register` | Register a new user |
| POST   | `/login` | Authenticate user & return JWT token |

### **Email Fetching**
| Method | Endpoint  | Description |
|--------|----------|-------------|
| POST   | `/fetch_emails` | Fetch emails using IMAP (requires JWT authentication) |

---

## 🛠️ Environment Variables (Optional)

If using Gmail API or other third-party services, configure environment variables in a `.env` file:

```env
EMAIL_HOST=imap.gmail.com
EMAIL_PORT=993
EMAIL_USER=your-email@gmail.com
EMAIL_PASSWORD=your-app-password
JWT_SECRET=your-secret-key
MONGO_URI=mongodb://localhost:27017/email_db
```

---

## 🎯 Usage Guide

1️⃣ **Register an account** with an email & password.  
2️⃣ **Login** to receive an authentication token.  
3️⃣ **Enter your App Password** (for email access).  
4️⃣ **Fetch Emails** and view the list of received messages & attachments.  
5️⃣ **Download attachments** if available.  
6️⃣ **Logout** when done.  

---

## ❓ Troubleshooting

- **Invalid Credentials?** Ensure the correct email & password are used.  
- **Emails Not Fetching?** Check IMAP settings & App Password usage.  
- **Unexpected Response Format?** Run `print(response.text)` in API debugging mode.  

---

## 📜 License

This project is open-source under the **MIT License**.

---

## 🤝 Contributing

Feel free to submit **issues, feature requests, and pull requests** to improve the project!

📧 **Contact:** amanking177@gmail.com  

🔗 **GitHub Repository:** [Secure-App-with-Email-Document-Listing](https://github.com/Amankumaraman/Secure-App-with-Email-Document-Listing/blob/main/Readme.md)
```
